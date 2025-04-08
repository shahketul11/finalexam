from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to Wild Rydes DevOps App!",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"health": "ok"})

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Stranger')
    return jsonify({"greeting": f"Hello, {name}!"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
