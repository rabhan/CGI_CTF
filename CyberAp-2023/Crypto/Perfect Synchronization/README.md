# fichiers fournis par le challenge
* output.txt : contient les blocks du cipher en hexadécimal. Un block par ligne.
* source.py : script qui a chiffré le cipher et qui contient la méthode à étudier.

# solution 1
**étude de la méthode de chiffrement**
* Le plaintext ne comporte que des majuscules (on le sait grâce à l'assert en début de script). Il n'a pas de minuscules ou chiffres, mais peut quand même posséder des caractères spéciaux et espace.
* Le plaintext est sûrement en anglais.
* Le plaintext est chiffré avec la méthode AES-128 ECB.
* Chaque block fait 16 octets.
* On remarque que chaque caractère du plaintext est 'salt' puis chiffré. On a donc un block chiffré par caractère.
* Vu que le salt et la clef sont les mêmes, plus le fait qu'ils aient utilisés AES-ECB, on en déduit que les blocks chiffrés identiques correspondent à un même caractère. On a donc 'juste' affaire à un chiffrement par substitution.

**méthode de résolution (moitié script/moitié manuelle)**
* analyse statistique pour découvrir un premier mot afin de nous aider dans la découverte du texte entier.
  * transformation de l'output en une suite de caractères aléatoires dans l'ensemble des majuscules + les caractères {}_ et l'espace (c'est un texte tout en majuscule, on suppose qu'il va y avoir des espaces pour séparer les mots, les {}_ sont ajoutés à l'ensemble car le format des flags HTB les utilisent en général)
  * utilisation du site suivant pour l'étude statistique : https://quipqiup.com/
    * en mettant ma suite de caractères aléatoires générée, le site me propose plusieurs solutions possible de déchiffrement, selon les statistiques d'apparition de chaque caractère, en se basant sur le taux d'apparition des lettres dans un texte en anglais. 
    * Ici ça me permet de déterminer que le texte commence sûrement par FREQUENCY
  * Utilisation du script pour substituer chaque bloc par les caractères connus. Les autres sont assignés aléatoirement.
    * Je recommence cette étape en réarangeant les lettres substituées dans le script dans la variable "printables" jusqu'à obtenir l'ensemble du texte en clair, et le flag.

**utilisation du script** 

python decode_output.py output.txt

___
