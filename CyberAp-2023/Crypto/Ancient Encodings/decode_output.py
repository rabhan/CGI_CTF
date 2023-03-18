from Crypto.Util.number import long_to_bytes
from base64 import b64decode
import sys

file_to_decode = sys.argv[1]

f = open(file_to_decode,'r')
FLAG = f.readline()
f.close()

def decode(message):
    return b64decode(long_to_bytes(int(message,16)))


def main():
    decoded_flag = decode(FLAG)
    print(decoded_flag)


if __name__ == "__main__":
    main()
