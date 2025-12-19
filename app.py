from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>LocalScriptLogger - LIVE</title>
    <style>
        body {background: linear-gradient(135deg,#000,#1a0033); color:#00ffaa; font-family:'Courier New',monospace; text-align:center; padding-top:8%;}
        h1 {font-size:6rem; text-shadow:0 0 50px #00ffaa; animation:glow 2s infinite alternate;}
        .url {font-size:3rem; background:rgba(0,255,170,0.15); padding:25px 40px; border:3px dashed #00ffaa; border-radius:25px; display:inline-block; margin:40px; letter-spacing:2px;}
        p {font-size:1.8rem; max-width:900px; margin:30px auto; line-height:1.8;}
        @keyframes glow {from {text-shadow:0 0 20px #00ffaa;} to {text-shadow:0 0 80px #00ffaa, 0 0 120px #00ffaa;}}
        a {color:#ff3366; font-weight:bold;}
    </style>
</head>
<body>
    <h1>LOCALSCRIPTLOGGER</h1>
    <div class="url">https://localscriptlogger-production.up.railway.app</div>
    <p>Serveur hébergé 24/7 sur Railway</p>
    <p>Le build a réussi à 100% grâce à Railpack</p>
    <p>Dès que tu veux la vraie interface Oxydal Rat complète (avec kick, troll, lua exec, etc.)<br>
    dis-moi juste <strong style="color:#ff3366;">"go full"</strong> et je te donne le code à coller en 5 secondes</p>
    <p>En attendant, ton serveur est déjà en ligne et stable</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
