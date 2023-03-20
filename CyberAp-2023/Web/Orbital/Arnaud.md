# Fichiers fournis par le challenge

![file listing](https://user-images.githubusercontent.com/106856367/226231820-2467c289-b8c7-45a4-90f3-3a1562772d08.png)




# Observations 

Pour commencer, en vérifiant chacun des fichiers fournis, il semble avoir 2 vulnérabilités évidentes qui resortent : 

1 - Dans **/challenge/application/database.py**, ligne 15 :

```python
def login(username, password):
    # I don't think it's not possible to bypass login because I'm verifying the password later.
    user = query(f'SELECT username, password FROM users WHERE username = "{username}"', one=True)

    if user:
        passwordCheck = passwordVerify(user['password'], password)

        if passwordCheck:
            token = createJWT(user['username'])
            return token
    else:
        return False

def getCommunication():
    return query('SELECT * from communication')
```

2 - Dans **/challenge/application/blueprints/routes.py**, ligne 52 : 

```python
    try:
        # Everyone is saying I should escape specific characters in the filename. I don't know why.
        return send_file(f'/communications/{communicationName}', as_attachment=True)
    except:
        return response('Unable to retrieve the communication'), 400
```
De plus, dans le fichier fournis **Dockerfile** nous pouvons identifier l'emplacement du flag pour plus tard : 

![flag location](https://user-images.githubusercontent.com/106856367/226231770-907cb1dd-9c4c-42fe-bd8b-ab6850815d4d.png)


# Solution

Avec Burp Suite, j'ai capturé le POST lors du login que j'ai ensuite copié dans un fichier **post.txt** sur ma machine : 

![burp1](https://user-images.githubusercontent.com/106856367/226231882-95569e71-5361-43f6-93e7-09c208704a85.png)

![burp2](https://user-images.githubusercontent.com/106856367/226231983-f0905bf6-d0b2-47f7-8e33-c3dc995e4229.png)


J'ai utilisé Sqlmap pour faire des scans sur la machine cible.

Commande utilisé :  **sqlmap -r post.txt -dbs**

Résultats obtenus : 

![sqlmap1](https://user-images.githubusercontent.com/106856367/226232030-66a337f0-8d60-4cd2-8f91-cfea8d197415.png)




En prenant compte de ces résultats, j'ai lancé un 2e scan qui ma permis de rertouvé le mot de passe d'un compte **admin**

Commande utilisé : **sqlmap -r post.txt -D orbital --tables --dump**

Résultats obtenus : 

![sqlmap2](https://user-images.githubusercontent.com/106856367/226232056-0d7c3344-a705-40ca-aec1-69e1c70515a3.png)


Une fois connecté sur le site, nous pouvons exploité la 2e faille identifié en interceptant le traffic dans Burp Suite et modifier la requête pour que le contenue de **flag.txt** soit exporté a la place de **communication.mp3**

![directory1](https://user-images.githubusercontent.com/106856367/226232104-a1cc7a69-5e16-42eb-993f-3c9418d005f3.png)

![directory2](https://user-images.githubusercontent.com/106856367/226232147-4784608e-4dba-4188-8d43-4d1e3bafd577.png)

![directory3](https://user-images.githubusercontent.com/106856367/226232185-161c1472-8f37-4f16-a10c-d4a40261b6b6.png)

![download](https://user-images.githubusercontent.com/106856367/226232230-0f12db19-438f-45fe-b7a1-2e95d16bd4ca.png)

Et voila ! 

![flag](https://user-images.githubusercontent.com/106856367/226232277-320c8708-7de7-4353-ad12-a7651a5d3584.png)


___

