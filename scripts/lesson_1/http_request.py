import requests
from requests.exceptions import HTTPError
import json


class Http:

    def __init__(self, host, protocol, auth_cred=None):
        self.base_url = f'{protocol}://{host}'
        self.auth_cred = auth_cred

    def send_request(self, method, relative_url, headers=None, params=None, data=None, json=None):
        url = ''.join([self.base_url, relative_url])
        result = None
        try:
            if method is 'GET':
                result = self.get_request(url, params, headers)
            elif method is 'POST':
                result = self.post_request(url, data, headers)
            elif method is 'PATCH':
                result = self.patch_request(url, json, headers)
            else:
                raise Exception(f"Request type is not defined! Provided type: {method}")
            result.raise_for_status()
        except HTTPError as err:
            print(f'HTTP error occurred: {err}')
        return Http.parse_result(result.text)

    def get_request(self, url, params, headers=None):
        return requests.get(url, params=params, headers=headers, auth=self.auth_cred)

    def post_request(self, url, data, headers=None):
        return requests.post(url, data=data, headers=headers, auth=self.auth_cred)

    def patch_request(self, url, json, headers=None):
        return requests.patch(url, json=json, headers=headers, auth=self.auth_cred)

    @staticmethod
    def parse_result(result):
        return json.loads(result) if Http.is_json(result) else result

    @staticmethod
    def is_json(str):
        try:
            json.loads(str)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    http = Http('httpbin.org', 'https')
    print(f'Sending HTTP requests to {http.base_url}...')
    http.send_request('GET', '/get')
    http.send_request('POST', '/post', data={'test_key': 'test_value'})
    print(f'HTTP requests to {http.base_url} are successful!')