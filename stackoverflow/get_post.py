import requests
from pprint import pprint
from datetime import datetime

class stack_api:
    def __init__(self):
        pass

    def get_headers(self):
        return {'Content-Type': 'Application/json'}

    def get_all_news(self, datefrom):
        headers = self.get_headers()
        params = {'fromdate': datefrom, 'site': 'stackoverflow'}
        url = 'https://api.stackexchange.com/2.2/questions'
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
        if resp.status_code == 200:
            return resp.json()

    def get_news(self, datefrom, tag):
        all_news = self.get_all_news(datefrom).get('items')
        tag_news = []
        for news in all_news:
            if tag in news['tags']:
                tag_news.append(news['title'])

        return tag_news


if __name__ == '__main__':
    stack = stack_api()
    datefrom = int(datetime.timestamp(datetime.strptime(input('Введите дату от которой искать в формате год-месяц-день: '), '%Y-%m-%d')))
    tag = input('Введите тэг, по котрому искать: ')
    pprint(stack.get_news(datefrom, tag))