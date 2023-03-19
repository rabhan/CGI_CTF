from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from math import exp, log
import mpmath

FLAG = b"HTB{???????????????}"
assert len(FLAG) == 20
mpmath.dps=100


class RSA:

    def __init__(self):
        self.q = getPrime(256)
        self.p = getPrime(256)
        self.n = self.q * self.p
        self.e = 3

    def encrypt(self, plaintext):
        print('flag test: ',plaintext)
        plaintext = bytes_to_long(plaintext)
        print('flag en long: ',plaintext)
        print('flag puissance 3: ',plaintext**self.e)
        f = mpmath.root(plaintext**self.e, self.e)
        print('diff entre racine cubique et resultat premier: ',f-plaintext)
        print('flag en bytes si on traduit directement le long precedent: ',long_to_bytes(plaintext))
        return pow(plaintext, self.e, self.n)
        
    def decode(self, message):
    	f = round(mpmath.root(message, self.e))
    	# f = exp(log(message)/self.e)
    	# f = int(message**(1/self.e))
    	print('racine cubique calculee du cipher: ',f)
    	return long_to_bytes(f)


def menu():
    print('[E]ncrypt the flag.')
    print('[A]bort training.\n')
    return input('> ').upper()[0]


def main():
    print('This is the second level of training.\n')
    while True:
        rsa = RSA()
        choice = menu()

        if choice == 'E':
            encrypted_flag = rsa.encrypt(FLAG)
            print(f'\nThe public key is:\n\nN: {rsa.n}\ne: {rsa.e}\n')
            print(f'The encrypted flag is: {encrypted_flag}\n')
            decrypted_flag = rsa.decode(encrypted_flag)
            print(f'The decrypted flag is: {decrypted_flag}\n')
        elif choice == 'A':
            print('\nGoodbye\n')
            exit(-1)
        else:
            print('\nInvalid choice!\n')
            exit(-1)

if __name__ == '__main__':
    main()
