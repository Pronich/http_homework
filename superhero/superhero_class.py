import requests

class superhero:
    def __init__(self, name):
        self.name = name
        self.intelligence = 0

    def Intelligence(self):
        id = self._get_id()
        url = f'https://www.superheroapi.com/api/2619421814940190/{id}/powerstats'
        req = requests.get(url)
        return req.json()['intelligence']

    def _get_id(self):
        url = f'https://www.superheroapi.com/api/2619421814940190/search/{self.name}'
        reqst = requests.get(url)
        return reqst.json()['results'][0]['id']