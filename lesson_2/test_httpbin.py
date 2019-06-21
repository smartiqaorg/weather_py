from http_request import HTTP
import pytest


class TestHttpbin:

    HOST = 'httpbin.org'
    PROTOCOL = 'https'
    URL_PARAM_NAME = 'param'
    URL_PARAM_VALUE = 'value'
    JSON_DATA = {'key': 'value'}

    # ---- Fixtures -----
    @pytest.fixture(scope='class')
    def http_manager(self, request):
        """
        Return HTTP class object for HTTP requests handling.
        More specifically, create HTTP manager for working with httpbin.org site.
        Tests use this object for GET/POST requests sending. The object is the same for all tests.
        """
        print(f'HTTP manager for {self.HOST} creation')

        def http_manager_teardown():
            print(f'HTTP manager for {self.HOST} destroyed')
        request.addfinalizer(http_manager_teardown)
        return HTTP(self.HOST, self.PROTOCOL)

    # ------ Tests ------
    def test_site_is_up(self, http_manager):
        """
        Check if httpbin.org address is available
        """
        assert(http_manager.site_is_up())

    def test_get_request_url(self, http_manager):
        """
        Test GET request handling.
        GET request is sent to 'httpbin.org/get' address.
        """
        expected_url = f'{self.PROTOCOL}://{self.HOST}/get'
        response = http_manager.send_request('GET', '/get')
        assert(response['url'] == expected_url)

    def test_get_request_params(self, http_manager):
        """
        Test GET request with params handling.
        GET request is sent to 'httpbin.org/get?param=value' address.
        """
        response = http_manager.send_request('GET', '/get', {self.URL_PARAM_NAME: self.URL_PARAM_VALUE})
        assert(response['headers'][self.URL_PARAM_NAME.capitalize()] == self.URL_PARAM_VALUE)

    def test_post_request_url(self, http_manager):
        """
        Test POST request(empty body) handling.
        POST request is sent to 'httpbin.org/post' address.
        """
        expected_url = f'{self.PROTOCOL}://{self.HOST}/post'
        response = http_manager.send_request('POST', '/post')
        assert(response['url'] == expected_url)

    def test_post_request_body(self, http_manager):
        """
        Test POST request(with body) handling.
        POST request is sent to 'httpbin.org/post' address. Request body is {'key': 'value'}.
        """
        response = http_manager.send_request('POST', '/post', data=self.JSON_DATA)
        assert(response['form'] == self.JSON_DATA)