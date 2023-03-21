import sys

file_to_decode = sys.argv[1]

f = open(file_to_decode,'r')
cipher_text = f.readlines()
f.close()

printables = 'FREQUNCY ALSIBDOTHGVWMPKXZJ{_}'
i = 0

known_blocks = {}
constructed_data = ""

for c in cipher_text:
    b = c.rstrip("\n")
    if b not in known_blocks.keys():
        known_blocks[b] = printables[i]
        i = i+1
        
    constructed_data = constructed_data + known_blocks[b]

print(constructed_data)    
