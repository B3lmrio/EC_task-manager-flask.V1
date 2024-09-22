from todo_project import db, app as create_app  # Importação correta
from todo_project.models import User, Task
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app  # Usando 'create_app' como a instância de 'app'
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    # Adicionar dados de teste
    user1 = User(username='testuser1', password='password1')
    user2 = User(username='testuser2', password='password2')
    db.session.add(user1)
    db.session.add(user2)

    task1 = Task(content='Test task 1', user_id=1)
    task2 = Task(content='Test task 2', user_id=2)
    db.session.add(task1)
    db.session.add(task2)

    db.session.commit()

    yield  # Para rodar os testes

    db.drop_all()

def test_new_user():
    user = User(username='testuser', password='testpassword')
    assert user.username == 'testuser'
    assert user.password == 'testpassword'

def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Todo App" in response.data
