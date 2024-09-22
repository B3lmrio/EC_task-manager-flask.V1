import pytest
from todo_project import app, db

@pytest.fixture
def test_client():
    app_instance.config['TESTING'] = True
    app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app_instance.config['WTF_CSRF_ENABLED'] = False  # CSRF desativado para testes

    with app_instance.app_context():  # Garantir que o contexto da aplicação seja criado
        database.create_all()
        test_client = app_instance.test_client()
        yield test_client
        database.drop_all()

def test_basic_workflow(test_client):
    """Teste básico para criação de usuário, login e criação de tarefa"""

    # 1. Criar um novo usuário
    response = test_client.post('/register', data={
        'username': 'basicuser',
        'password': 'Basic@1234',
        'confirm_password': 'Basic@1234'
    }, follow_redirects=True)
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida

    # 2. Fazer login com o novo usuário
    response = test_client.post('/login', data={
        'username': 'basicuser',
        'password': 'Basic@1234'
    }, follow_redirects=True)
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida
    assert b'Task List' in response.data  # Verifica se o login foi bem-sucedido

    # 3. Adicionar uma nova tarefa
    response = test_client.post('/create_task', data={
        'task_name': 'Comprar pão'
    }, follow_redirects=True)
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida

    # 4. Verificar se a tarefa aparece na lista de tarefas
    response = test_client.get('/tasks_list', follow_redirects=True)  # Seguir redirecionamentos
    assert response.status_code == 200
    # 4. Verificar se a tarefa aparece na lista de tarefas
    response = client.get('/all_tasks', follow_redirects=True)  # Seguir redirecionamentos
    assert response.status_code == 200
