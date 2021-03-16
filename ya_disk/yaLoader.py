import requests
from pprint import pprint
import os

token = '/тут ваш токен/'

class yaUpLoader:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return {'Content-Type': 'Application/json', 'Authorization': 'OAuth ' + self.token}

    def _get_path_by_file(self, path):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.headers()
        params = {'path': path, 'overwrite': 'true'}
        resp = requests.get(url, params=params, headers=headers)
        return resp.json()

    def upload(self, file_to, file_from):
        href = self._get_path_by_file(file_to).get('href')
        response = requests.put(href, data=open(file_from, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    uploader = yaUpLoader(token)
    os_path = os.getcwd()
    file_name = 'homework.txt'
    file_from = os.path.join(os_path, file_name)
    file_to = f'netology/{file_name}'
    uploader.upload(file_to, file_from)