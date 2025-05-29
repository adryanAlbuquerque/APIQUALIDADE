import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get(client):
    resposta = client.get('/api')
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "GET funcionando"}

def test_post(client):
    dados = {"nome": "João"}
    resposta = client.post('/api', json=dados)
    assert resposta.status_code == 200
    assert resposta.json["dados"]["nome"] == "João"
