from http_request import Http

TEST_USER = 'smartiqa-test'
# GitHub restricts pushing Authentication Token to public repo
# That's why it's necessary to update it with valid token before running
AUTH_TOKEN = '<Please change me for b4a1d07f32....c5ca8594f>'
TEST_REPO = 'test_repository_2'
TEST_ISSUE_NUM = 3
TEST_COMMIT_SHA = '063b6dde79957b9f34a0a5f74f4febe0e34cbba5'


class API:

    HOST = 'api.github.com'
    PROTOCOL = 'https'

    def __init__(self):
        self.http = Http(self.HOST, self.PROTOCOL)

    def call(self, method, relative_url, headers=None, json=None):
        return self.http.send_request(method, relative_url, headers=headers, json=json)


class User:

    def __init__(self, auth_token=None):
        self.api = API()
        # Majority of the API requests need Authentication Token but not all
        if auth_token is not None:
            self.headers = {'Authorization': f'token {auth_token}'}

    # ------ Get User info without Authentication ------
    def get(self, user_name):
        return self.api.call('GET', f'/users/{user_name}')

    def get_bio(self, user_name):
        return self.get(user_name)['bio']

    # -- Get additional User info with Authentication --
    def get_authenticated(self):
        return self.api.call('GET', f'/user', headers=self.headers)

    # --------------- Update User info -----------------
    def update_bio(self, new_bio):
        return self.api.call('PATCH', f'/user', headers=self.headers, json={'bio': new_bio})


class Issue:

    def __init__(self, auth_token):
        self.api = API()
        self.headers = {'Authorization': f'token {auth_token}'}

    # ------- List Issues -------------
    def list(self):
        return self.api.call('GET', '/issues', headers=self.headers)

    def list_for_repository(self, owner, repo):
        return self.api.call('GET', f'/repos/{owner}/{repo}/issues', headers=self.headers)

    # ------- Get Issue info ----------
    def get(self, owner, repo, number):
        return self.api.call('GET', f'/repos/{owner}/{repo}/issues/{number}', headers=self.headers)

    # ------- Edit Issues -------------
    def edit_title(self, owner, repo, number, new_title):
        return self._edit(owner, repo, number, json={'title': new_title})

    def edit_body(self, owner, repo, number, new_body):
        return self._edit(owner, repo, number, json={'body': new_body})
    # ---------------------------------

    def _edit(self, owner, repo, number, json):
        return self.api.call('PATCH', f'/repos/{owner}/{repo}/issues/{number}', headers=self.headers, json=json)


if __name__ == '__main__':
    # Check GitHub User API functionality
    user = User(AUTH_TOKEN)
    user.get(TEST_USER)
    user.get_bio(TEST_USER)
    user.get_authenticated()
    user.update_bio('New Test bio')

    # Check GitHub Issue API functionality
    issue = Issue(AUTH_TOKEN)
    issue.list()
    issue.list_for_repository(TEST_USER, TEST_REPO)
    issue.get(TEST_USER, TEST_REPO, TEST_ISSUE_NUM)
    issue.edit_title(TEST_USER, TEST_REPO, TEST_ISSUE_NUM, 'Smartiqa Test issue 3')
    issue.edit_body(TEST_USER, TEST_REPO, TEST_ISSUE_NUM, 'Smartiqa Test body 3')