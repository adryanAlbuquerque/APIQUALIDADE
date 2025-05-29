import requests

def test_get():
    resposta = requests.get("http://127.0.0.1:5000/api")
    assert resposta.status_code == 200

def test_post():
    dados = {"nome": "João"}
    resposta = requests.post("http://127.0.0.1:5000/api", json=dados)
    assert resposta.status_code == 200
    assert resposta.json()["dados"]["nome"] == "João"
