# fournis par le challenge
* un container avec lequel il va falloir communiquer
* README.md : Explication de comment se connecter au serveur 
* server.py : script qui permet de simuler le fonctionnement du serveur pour tests en local.
* solver.py: script pour aider à la simulation ou connexion en remote

# solution 1

Le principe est 'simple' :
* Le serveur nous donne l'exposant, le modulo et le cipher (texte chiffré) du flag.
* L'algorithme utilisé est RSA
* RSA est particulièrement vulnérable si l'exposant est petit, ce qui est le cas ici, e=3
* on voit la façon dont le cipher est créé : plaintext**3 modulo n
  * le problème d'un petit exposant est que plaintext**3 a de forte chance d'être plus petit que le modulo, on a donc juste à retrouver la racine pour retrouver le texte en clair sans se préoccuper du modulo. C'est ce qu'on va faire ici.

La formule pour retrouver le texte en clair va être donc (en python avec la fonction qui transforme le string en bytes):
long_to_bytes(cipher**(1/3))


Devant mon incapacité à trouver des outils assez précis pour effectuer ce calcul, je suis passée par ce site : https://www.dcode.fr/chiffre-rsa

Je vous mets quand même le script server.py ou j'ai ajouté la fonction decode, si quelqu'un trouve une librairie de math assez précise, ça devrait finir par fonctionner.
___
