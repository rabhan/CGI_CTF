# Fichiers fournis par le challenge

* wrapper.py : script python pour bof, modifier les valeurs requires (IP, Port, nombre de A's) et installer pwntools (pip3 install pwntools) 
* flag.txt : Exemple de flag invalide
* gs (ghostscript) : binary instrumenting tool
* ld-linux-x86-64.so.-2 : dynamic linker/loader for Linux systems
* libc.so.6 : shared library 

# Solution 

Après quelques recherches j'ai exécuté : 

**LD_PRELOAD=./libc.so.6 ./ld-linux-x86-64.so.-2 ./GS**

et ma donner le output suivant : 

![GettingStarted1](https://user-images.githubusercontent.com/106856367/226144320-92190489-be20-4f6b-9e94-bd84b357c931.png)


![GettingStarted2](https://user-images.githubusercontent.com/106856367/226144326-fb4d1e38-36e7-44e9-8e28-ae2cfbcc8e9d.png)


J'ai vérifier le nombre de bytes a inséré pour le bof, après quelques essaies en commencant par 38, 40 est le nombre magique et a donner ce output :

![GettingStarted3](https://user-images.githubusercontent.com/106856367/226144374-912b8969-425f-4bec-96c3-9660ded0b0da.png)

___________________________________________________________________________________________________________________________________________________
