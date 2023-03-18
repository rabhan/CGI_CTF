# Drobots
### Julien

## Examination du code

### challenge/application/templates/login.html

Lorsqu'on clique sur le bouton, une fonction ``` login() ``` est éxecutée. Cette fonction se trouve dans challenge/application/static/js/script.js

### challenge/application/static/js/script.js

La fonction ``` login() ``` fait appel à un api défini dans challenge/application/blueprints/routes.py et nous redirige vers /home lorsque le login est effectué correctement (code 200).

### challenge/application/blueprints/routes.py

La route login fait appel à la fonction ``` login() ``` importée de application.database, soit le fichier challenge/application/database.py et retourne un code 200 lorsque la fonction ``` login() ``` retourne ``` True ```. 

### challenge/application/database.py

ligne 17:
```python
user = query_db(f'SELECT password FROM users WHERE username = "{username}" AND password = "{password}" ', one=True)
```

La ligne est vulnérable à une attaque de type SQL injection

Il suffit de taper quelque chose comme ``` test" OR 1=1 OR " ``` dans les deux champs pour être redirigé vers la page d'accueil, où le flag peut être trouvé, car 1=1 sera toujours vrai.