# Fichiers fournis par le challenge

![file listing](https://user-images.githubusercontent.com/106856367/226188012-76890304-eabc-4b37-ab12-7304dc04a60e.png)




# Solution 

Sur le site, nous avons accès a un terminal qui permet d'exécuter des commandes : 

![1 siteterminal](https://user-images.githubusercontent.com/106856367/226188155-7a9c458c-9e74-4c26-a15d-374eb7eb4952.png)

En vérifiant les fichiers fournis, nous trouvons **ReconModle.php** dans **web_gunhead/models/** qui contient le code suivant : 


![reconmodel](https://user-images.githubusercontent.com/106856367/226188346-06d28cdd-6264-4bb2-b66e-415aafe99dcc.png)

Puisque le user input n'est pas "sanitized" nous pouvons testé d'injecter nos propres commandes lorsque nous utilisons **/ping** :

![reconmodel2](https://user-images.githubusercontent.com/106856367/226188713-bd1043ac-649b-4ac0-a6fb-544b6eb78ba3.png)


Nous pouvons donc se prommener dans le système et peut-être trouver le flag? :

![reconmodel3](https://user-images.githubusercontent.com/106856367/226188802-8fde7958-367a-4a3e-9084-50795efcdd31.png)

Une fois le fichier **flag.txt** trouver, reste plus qu'a le "cat" :

![reconmodel4](https://user-images.githubusercontent.com/106856367/226189134-135b5760-9c60-43bf-b8f6-7eddc7749b2a.png)

___
