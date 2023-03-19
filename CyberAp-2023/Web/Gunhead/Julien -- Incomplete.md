# Drobots
### Julien

## Examination de la page web

Il y a un terminal qui peut exécuter 3 commandes (/ping, /storage et /clear). Cela semble intéressant

## Examination du code
** Disclaimer: j'ai jamais fait de PHP avant **

L'application semble être faite en suivant le principe du MVC (Model, View Controller)

### challenge/views/index.php

ligne 48: ``` <div> ``` du terminal

### challenge/static/js/script.js

Fonction ping du terminal fait un POST API avec un json ``` { 'ip': host } ```

### challenge/index.php

Le routeur redirige le POST de la route ``` /api/ping ``` vers ``` ReconController@ping ```

### challenge/controllers/ReconController.php

Pourvu que l'information reçue ait le bon format (un json avec un paramêtre 'ip'), le contrôleur crée un objet ReconModel avec la valeur de l'attribut 'ip' passée en paramètre. 

### challenge/controllers/ReconModel.php

La fonction exécute une commande ``` ping -c 3 {{ip}} ``` sans sanitisation. Il faut donc trouver une commande que l'on pourrait utiliser pour faire afficher des données autres que la réponse du ping. J'ai d'abord tapé ``` /ping localhost ```, qui me répond avec ``` PING localhost (::1): 56 data bytes```, mais pas avec les paquets. Je me suis dit qu'il était possible que seule la première ligne retournée est écrite dans le terminal de l'app web et j'ai pensé à taper ``` /ping localhost > ping.txt && ls ``` pour voir si je pourrais voir le résultat du ``` ls ```. Par contre, je ne me retrouve avec rien du tout... J'ai fait un petit script php avec la commande exacte pour tester sur mon ordinateur et ça fonctionne sans problème.

Le script: 
```php 
<?php
$output = shell_exec*'ping -c 3 localhost > ping.txt && ls');
echo "$output";
?>
```