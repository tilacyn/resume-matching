import requests

url = 'https://api.hh.ru/vacancies'

def fetch_vacancies(name, n):
	par = {'text': name, 'area': '113', 'per_page': str(n), 'page': 0}
	r = requests.get(url, params=par)
	whole_json = r.json()
	return whole_json['items']

vacancy = fetch_vacancies('software engineer', 1)
