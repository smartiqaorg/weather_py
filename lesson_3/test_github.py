from http_request import HTTP
import pytest

# GitHub restricts pushing Authentication Token to public repo
# That's why it's necessary to update it with valid token before running
AUTH_TOKEN = '<Please change me for f1a3e0c13....a2b8dc4d3>'


class GitHubAPI:

    HOST = 'api.github.com'
    PROTOCOL = 'https'

    def __init__(self, host=HOST, protocol=PROTOCOL, auth_token=AUTH_TOKEN):
        self.http = HTTP(host, protocol)
        self.headers = {'Authorization': f'token {auth_token}'}

    def call(self, method, relative_url, params=None, json=None):
        return self.http.send_request(method, relative_url, headers=self.headers, params=params, json=json)


class GitHubUser:

    def __init__(self, api):
        self.api = api

    # ------------ Get User info -------------
    def get(self, user_login):
        return self.api.call('GET', f'/users/{user_login}')

    def get_bio(self, user_login):
        return self.get(user_login)['bio']

    def get_name(self, user_login):
        return self.get(user_login)['name']

    # ----------- Update User info ------------
    def update(self, json):
        return self.api.call('PATCH', f'/user', json=json)

    def update_bio(self, new_bio):
        return self.update({'bio': new_bio})

    # ------- Reset User info to Default ------
    def reset(self):
        return self.update({'bio': 'Default bio', 'name': 'Smartiqa Online Courses'})


class TestGitHub:

    TEST_USER = 'smartiqa-test'
    TEST_USER_INFO = {
        'login': TEST_USER,
        'id': 50556714,
        'name': 'Smartiqa Online Courses',
        'public_repos': 3,
        'bio': 'Default bio'
    }

    # ------ Fixtures ------
    @pytest.fixture()
    def api_manager(self):
        api_manager = GitHubAPI()
        GitHubUser(api_manager).reset()
        return api_manager

    # ----- Get Tests -------
    def test_get_user_info_all(self, api_manager):
        """
        Get info about GitHub User by their login and check
        """
        user_info = GitHubUser(api_manager).get(self.TEST_USER)
        assert(self.TEST_USER_INFO.items() <= user_info.items())

    def test_get_user_info_name(self, api_manager):
        """
        Get GitHub User name by their login and check
        Example name: 'smartiqa-test'
        """
        user_name = GitHubUser(api_manager).get_name(self.TEST_USER)
        assert(self.TEST_USER_INFO['name'] == user_name)

    def test_get_user_info_bio(self, api_manager):
        """
        Get GitHub User biography by their login and check
        Example biography: 'Default bio'
        """
        user_bio = GitHubUser(api_manager).get_bio(self.TEST_USER)
        assert(self.TEST_USER_INFO['bio'] == user_bio)

    # ----- Update Tests ------
    def test_update_user_info_bio(self, api_manager):
        """
        Change GitHub User biography and check the result
        Example: from 'Default bio' to 'New Test bio'
        """
        new_bio = 'New Test bio'
        result = GitHubUser(api_manager).update_bio(new_bio)
        assert(result['bio'] == new_bio)