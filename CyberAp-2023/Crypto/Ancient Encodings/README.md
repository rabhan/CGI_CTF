# fichiers fournis par le challenge
* output.txt : contient une chaine de caractère en hexadécimal (0x) 
* source.py : script qui a obsfuqué le flag et qui contient donc la méthode à inverser.

# solution 1

Il suffit d'inverser les fonctions appliquées au flag pour le retrouver.


Ici le flag est d'abord encodé en base64, transformé en long puis écrit dans l'output en hexadécimal.


Pour retrouver l'original il nous suffit de retranformer l'output en int, de le remettre en byte et de décoder le base64. C'est ce que fait le script decode_output.py

**utilisation du script** 

python decode_output.py output.txt

___
