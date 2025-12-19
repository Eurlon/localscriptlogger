from flask import Flask, render_template_string

app = Flask(__name__)

# Page d'accueil toute simple pour tester
HTML_TEST = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Test Local Oxydal Rat</title>
    <style>
        body {background: #000; color: #00ffaa; font-family: Arial; text-align: center; padding-top: 15%;}
        h1 {font-size: 4rem; text-shadow: 0 0 30px #00ffaa;}
        p {font-size: 1.5rem;}
        a {color: #ffcc00; font-size: 2rem; text-decoration: none;}
        a:hover {text-decoration: underline;}
    </style>
</head>
<body>
    <h1>✓ Test réussi !</h1>
    <p>Ton serveur Flask tourne parfaitement en local</p>
    <p>Port : 5000</p>
    <br>
    <p>Quand tu seras prêt à mettre la vraie interface,<br>
    remplace simplement ce fichier par la version complète que je t’ai donnée avant.</p>
    <br>
    <a href="https://www.roblox.com" target="_blank">Aller sur Roblox →</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEST)

if __name__ == "__main__":
    print("🚀 Serveur local démarré !")
    print("Ouvre ton navigateur et va à cette adresse → http://localhost:5000")
    print("Pour arrêter : appuie sur Ctrl + C")
    app.run(host="0.0.0.0", port=5000, debug=True)
