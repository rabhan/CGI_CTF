# Fichiers fournis par le challenge




# Solution 

En vérifiant les configurations, l'utilisateur **restricted** est configuré avec un shell restricté **rbash**

Une recherche sur google permet rapidement de trouver des trucs pour "sortir" de l'environnement restraint :

https://www.hacknos.com/rbash-escape-rbash-restricted-shell-escape/

ssh hackNos@<IP-Adress> -t "bash --noprofile"
cd ../

Une fois sortie du shell restraint, le flag se trouve asser facilement : 


___
