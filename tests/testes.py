import pytest
from flask import Flask
from todo_project import create_app  # Substitua pelo nome correto do módulo onde está a aplicação

@pytest.fixture
def app():
    """Cria a aplicação Flask para os testes."""
    app = create_app()  # Substitua por sua função real de criar a app
    app.config.update({
        "TESTING": True,  # Ativar modo de teste
        "WTF_CSRF_ENABLED": False  # Desabilitar CSRF em testes, se aplicável
    })
    return app

@pytest.fixture
def client(app):
    """Cria um cliente de teste."""
    return app.test_client()

def test_homepage(client):
    """Verifica se a homepage carrega corretamente."""
    response = client.get("/")  # Ajuste essa rota para a rota principal da sua aplicação
    assert response.status_code == 200

def test_task_page(client):
    """Verifica se a página de tarefas carrega corretamente."""
    response = client.get("/tasks")  # Ajuste essa rota conforme o seu sistema de tarefas
    assert response.status_code == 200

def test_add_task(client):
    """Testa a adição de uma tarefa (POST request)."""
    response = client.post("/tasks/add", data={
        "task_name": "Test Task",
        "description": "This is a test task",
    })
    assert response.status_code == 200  # Ou ajuste conforme o resultado esperado
    # Adicionalmente, verifique se a tarefa foi realmente criada
    assert b"Test Task" in response.data
