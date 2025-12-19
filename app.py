from flask import Flask, render_template_string

app = Flask(__name__)

# Message spécial avec ton URL exacte
HTML_FINAL = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Oxydal Rat READY</title>
    <style>
        body {background: linear-gradient(135deg,#000,#0f0020); color: #00ffaa; font-family: 'Courier New', monospace; text-align: center; padding-top: 10%;}
        h1 {font-size: 5rem; text-shadow: 0 0 40px #00ffaa; margin-bottom: 20px;}
        .url {font-size: 2.5rem; background: rgba(0,255,170,0.1); padding: 20px; border-radius: 20px; display: inline-block; margin: 30px; border: 2px dashed #00ffaa;}
        p {font-size: 1.6rem; max-width: 800px; margin: 20px auto; line-height: 1.8;}
        .blink {animation: blink 1.5s infinite;}
        @keyframes blink {0%,100%{opacity:1} 50%{opacity:0.4}}
        a {color: #ffcc00; font-weight: bold;}
    </style>
</head>
<body>
    <h1 class="blink">DEPLOIEMENT REUSSI !</h1>
    <div class="url">https://e1ax449x.up.railway.app</div>
    <p>Ton rat est maintenant hébergé 24/7 sur Railway</p>
    <p>Tu peux maintenant remplacer ce fichier par la <strong>vrai version complète Oxydal Rat</strong> (avec SocketIO, kick, troll, etc.)</p>
    <p>Dès que tu push la vraie version sur GitHub → elle sera automatiquement en ligne sur <strong>cette même URL</strong> :</p>
    <h2 style="color:#ff3366;">https://e1ax449x.up.railway.app</h2>
    <br><br>
    <p>Envoie-moi « go full » quand tu veux que je te donne la vraie version prête à coller</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_FINAL)

# Pour Railway
if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
