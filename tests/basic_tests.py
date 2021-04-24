# basic_test.py   
import requests
import unittest
import json
import urls
import sys
sys.path.append('../main')
import queries


class BasicTests(unittest.TestCase):
    # test suite
    def test_get_request_pos_test_1(self):
        response = requests.get(urls.BASE_URL)
        assert response.status_code == 200

    def test_getid_request_pos_test_1(self):
        success, token = queries.get_token()
        response = requests.get(urls.GET_POS_TEST_URL.format(token))
        assert response.status_code == 200

    def test_getid_request_neg_test_1(self):
        success, token = queries.get_token()
        response = requests.get(urls.GET_NEG_TEST_URL.format(token))
        assert response.status_code == 404

    def test_filter_request_pos_test_1(self):
        success, token = queries.get_token()
        response = requests.get(urls.FILTER_POS_TEST_URL.format(token))
        assert response.status_code == 200

    def test_filter_request_neg_test_1(self):
        success, token = queries.get_token()
        response = requests.get(urls.FILTER_NEG_TEST_URL.format(token))
        assert response.status_code == 400

    def test_create_request_pos_test_1(self):
        success, token = queries.get_token()
        url = urls.CREATE_API_URL.format(token)
        body = json.dumps(urls.CREATE_POS_jSON)
        headers = {
                'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=body)
        assert response.status_code == 201

    def test_create_request_neg_test_1(self):
        success, token = queries.get_token()
        url = urls.CREATE_API_URL.format(token)
        body = json.dumps(urls.CREATE_NEG_JSON)
        headers = {
                'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=body)
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
