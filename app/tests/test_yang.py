from yang import Create_app
import pytest

@pytest.fixture
def app():
    app = Create_app({'TESTING': True})

    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)

def test_login(auth):
    auth.logout()
    print('auth')
    # assert 0

if __name__=='__main__':
    pytest.main()