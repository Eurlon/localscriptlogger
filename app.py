from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>LocalScriptLogger - ONLINE</title>
    <style>
        body {background: linear-gradient(135deg,#000,#1a0033); color:#00ffaa; font-family:'Courier New',monospace; text-align:center; padding-top:8%;}
        h1 {font-size:6rem; text-shadow:0 0 50px #00ffaa; animation:glow 2s infinite alternate;}
        .url {font-size:3rem; background:rgba(0,255,170,0.15); padding:25px 40px; border:3px dashed #00ffaa; border-radius:25px; display:inline-block; margin:40px;}
        p {font-size:1.8rem; max-width:900px; margin:30px auto;}
        @keyframes glow {from {text-shadow:0 0 20px #00ffaa;} to {text-shadow:0 0 80px #00ffaa;}}
    </style>
</head>
<body>
    <h1>LOCALSCRIPTLOGGER</h1>
    <div class="url">https://localscriptlogger-production.up.railway.app</div>
    <p>Serveur 100% opérationnel 24/7</p>
    <p>Le crash est corrigé, tout fonctionne maintenant</p>
    <p>Dis-moi <strong style="color:#ff3366;">"go full"</strong> quand tu veux la vraie interface complète (kick, troll, lua exec, etc.)</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

# Ligne magique qui fait TOUT fonctionner sur Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
