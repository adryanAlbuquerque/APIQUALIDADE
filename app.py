from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify({"mensagem": "GET funcionando"})

@app.route('/api', methods=['POST'])
def post_api():
    dados = request.json
    return jsonify({"mensagem": "POST recebido", "dados": dados})

if __name__ == '__main__':
    app.run(debug=True)
