import requests
import re

url = 'https://api.hh.ru/vacancies'

def fetch_hh_vacancies(name, n):
	par = {'text': name, 'area': '113', 'per_page': str(n), 'page': 0}
	r = requests.get(url, params=par)
	whole_json = r.json()
	return whole_json['items']


proxies = {
	"https": "https://207.144.111.230:8080"
}


class JobSpiderVacancyFetcher:
	def __init__(self):
		self.jobs_spider_url = "http://www.jobspider.com/job/job-search-results.asp/words_java/searchtype_1"

	def fetch_vacancy_page(self, page_number):
		r = requests.get(self.jobs_spider_url + '/page_' + str(page_number), proxies=proxies)
		self.vacancies_page = r.text
		print("downloaded vacancy page:", page_number)

	def fetch_vacancy_files(self):
		vacancy_urls = re.findall('view-job-\\d+\\.html', self.vacancies_page)
		print("vacancy urls retrieved")

		for url_suffix in vacancy_urls:
			url = "http://www.jobspider.com/job/" + url_suffix
			print("connecting with", url)
			f = open("vacancies/" + url_suffix, "w", encoding='utf-8')
			r = requests.get(url, proxies=proxies)
			print("html", url, "downloaded, OK")
			f.write(r.text)
			f.close()
