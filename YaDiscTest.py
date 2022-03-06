from tok import TOKEN
import requests
import unittest


class TestCreateFolderInYandexDisc(unittest.TestCase):
    URL = 'https://cloud-api.yandex.net/v1/disk/'
    api_token = TOKEN
    headers = {'Authorization': 'OAuth ' + api_token}

    def test_add_folder(self):
        create_folder_url = self.URL + 'resources'
        params = {'path': r'disk:/test_folder'}
        response = requests.put(create_folder_url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 201)

    def test_check_folder_created(self):
        create_folder_url = self.URL + 'resources'
        params = {'path': r'disk:/test_folder'}
        response = requests.get(create_folder_url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 200)


