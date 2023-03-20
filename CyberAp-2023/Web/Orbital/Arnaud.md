# Fichiers fournis par le challenge





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


# Solution

Avec Burp Suite, j'ai capturé le POST lors du login que j'ai ensuite copié dans un fichier **post.txt** sur ma machine : 


J'ai utilisé Sqlmap pour faire des scans sur la machine cible.

Commande utilisé :  **sqlmap -r post.txt -dbs**

Résultats obtenus : 



En prenant compte de ces résultats, j'ai lancé un 2e scan qui ma permis de rertouvé le mot de passe d'un compte **admin**

Commande utilisé : **sqlmap -r post.txt -D orbital --tables --dump**

Résultats obtenus : 



Une fois connecté sur le site, nous pouvons exploité la 2e faille identifié en interceptant le traffic dans Burp Suite et modifier la requête pour que le contenue de **flag.txt** soit exporté a la place de **communication.mp3**


___

