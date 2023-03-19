# Fichiers fournis par le challenge

![File listing](https://user-images.githubusercontent.com/106856367/226144187-acd3aa1d-94cd-4dd5-9736-d7ab581830d1.png)


# Solution 

En vérifiant le contenu de l'application, nous observons que ces une database MySQL en arrière et selon le commentaire, le code serait vulnérable a du SQL injection.

![Database py](https://user-images.githubusercontent.com/106856367/226148819-7cce3e44-78ef-492e-bbd6-0b8f07c90be4.png)

Pour testé, nous pouvons soit faire l'injection manuellement ou utilisé un outils comme Sqlmap pour le testé automatiquement: 

**"' OR 1=1 --"**


![sqli](https://user-images.githubusercontent.com/106856367/226150292-f6d9c17c-6ef8-4076-acad-d4847a306c3b.png)

![flag](https://user-images.githubusercontent.com/106856367/226150296-33875fb5-2902-4a0a-864e-e778cfbb2b5b.png)

___
