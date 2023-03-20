# Fichiers fournis par le challenge


![file listing](https://user-images.githubusercontent.com/106856367/226227255-52b95d6d-7a01-4ffd-b6c9-2755adff1672.png)



# Solution 

En vérifiant les configurations, l'utilisateur **restricted** est configuré avec un shell restricté **rbash**

Une recherche sur google permet rapidement de trouver des trucs pour "sortir" de l'environnement restraint :

https://www.hacknos.com/rbash-escape-rbash-restricted-shell-escape/

**ssh restricted@IPADDRESS -p PORT -t "bash --noprofile"**


Une fois sortie du shell restraint, le flag se trouve asser facilement : 

![flag](https://user-images.githubusercontent.com/106856367/226227306-2dd8db1a-b451-401a-a825-86538b0fde38.png)

___
