import requests

url = 'https://api.hh.ru/vacancies'

def fetch_vacancies(name, n):

    for i in range(n):
        par = {'text': name, 'area': '113', 'per_page': '1', 'page': i}
        r = requests.get(url, params=par)
        e = r.json()
        print(e)
        return e

e = fetch_vacancies('software engineer', 1)