from todo_project.todo_project.forms import RegistrationForm

def test_registration_form_username_required():
    form = RegistrationForm(username='', password='password123', confirm_password='password123')
    assert not form.validate()
    assert 'This field is required.' in form.username.errors
