from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor de Juegos Telegram activo 🎮"

@app.route('/tragamonedas')
def tragamonedas():
    return send_from_directory('games/tragamonedas', 'index.html')

@app.route('/tragamonedas/<path:filename>')
def tragamonedas_files(filename):
    return send_from_directory('games/tragamonedas', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
