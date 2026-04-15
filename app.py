from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon App Docker - Fops</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
        }

        .container {
            text-align: center;
            padding: 60px 40px;
            max-width: 700px;
            width: 90%;
        }

        .badge {
            display: inline-block;
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 50px;
            padding: 8px 20px;
            font-size: 0.85rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #a0d8ef;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }

        .docker-icon {
            width: 90px;
            height: 90px;
            background: linear-gradient(135deg, #0db7ed, #086a8a);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 30px auto;
            box-shadow: 0 8px 32px rgba(13, 183, 237, 0.4);
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-10px); }
        }

        .docker-icon svg {
            width: 55px;
            height: 55px;
            fill: white;
        }

        h1 {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(90deg, #a0d8ef, #ffffff, #0db7ed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            font-size: 1.1rem;
            color: rgba(255,255,255,0.75);
            margin-bottom: 40px;
            line-height: 1.6;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 40px;
        }

        .card {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 16px;
            padding: 24px 16px;
            backdrop-filter: blur(10px);
            transition: transform 0.2s, background 0.2s;
        }

        .card:hover {
            transform: translateY(-4px);
            background: rgba(255,255,255,0.12);
        }

        .card .icon { font-size: 2rem; margin-bottom: 10px; }
        .card .label { font-size: 0.8rem; color: #a0d8ef; text-transform: uppercase; letter-spacing: 1px; }
        .card .value { font-size: 1.1rem; font-weight: 600; margin-top: 4px; }

        .status-bar {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            background: rgba(13, 183, 237, 0.1);
            border: 1px solid rgba(13, 183, 237, 0.3);
            border-radius: 50px;
            padding: 12px 28px;
            font-size: 0.95rem;
            color: #a0d8ef;
        }

        .dot {
            width: 10px;
            height: 10px;
            background: #2ecc71;
            border-radius: 50%;
            animation: pulse 1.5s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(46,204,113,0.6); }
            50%       { box-shadow: 0 0 0 8px rgba(46,204,113,0); }
        }

        footer {
            margin-top: 50px;
            font-size: 0.8rem;
            color: rgba(255,255,255,0.35);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">🎓 Keyce Informatique &amp; IA — CC1 DevOps</div>

        <div class="docker-icon">
            <!-- Docker whale icon SVG -->
            <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg">
                <path d="M349.9 236.3h-66.1v-59.4h66.1v59.4zm0-204.3h-66.1v59.4h66.1V32zm78.2 144.8H362v59.4h66.1v-59.4zm-156.3-72.1h-66.1v59.4h66.1v-59.4zm239.6 0h-66.1v59.4H511v-59.4zm-317.7 0H128v59.4h65.5v-59.4zM512 268.3H384v59.4h128v-59.4zm-351.5 0H96v59.4h64.5v-59.4zM630.4 286c-5.2-3.1-24.8-5.7-43.9-2.8-4.9-23.3-20.5-44.1-48.6-62.5l-16.5-11-10.7 16.8c-13.5 21.4-20.2 51-17.9 79.2 1.1 11.9 4.9 33.3 17.4 52.4-8.1 4.5-24.9 10.7-46.4 10.4H40.5c-7.3 41.4 3.8 105.6 43.3 148.7 36.8 40.1 92 60.3 164.2 60.3 148.5 0 262.5-67.2 315.7-189.6 20.6.4 65.1 0 88.1-43.7 1.4-2.4 5.3-9.8 6.5-12.1l-27.9-16.7z"/>
            </svg>
        </div>

        <h1>Application Dockerisée</h1>
        <p class="subtitle">
            Bonjour à tous ! Ceci est une application Flask conteneurisée avec Docker.<br>
            Développée par <strong>Fops</strong> dans le cadre du CC1 — Conduite de Projet.
        </p>

        <div class="card-grid">
            <div class="card">
                <div class="icon">🐳</div>
                <div class="label">Plateforme</div>
                <div class="value">Docker</div>
            </div>
            <div class="card">
                <div class="icon">🐍</div>
                <div class="label">Runtime</div>
                <div class="value">Python 3.9</div>
            </div>
            <div class="card">
                <div class="icon">⚡</div>
                <div class="label">Framework</div>
                <div class="value">Flask</div>
            </div>
        </div>

        <div class="status-bar">
            <span class="dot"></span>
            Conteneur opérationnel — Port 5000 actif
        </div>

        <footer>
            Matrix Télécoms / GFC S.A. &nbsp;|&nbsp; DSI &nbsp;|&nbsp; Keyce 2026
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
