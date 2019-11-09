import requests
import re


proxies = {
	"https": "https://207.144.111.230:8080"
}


livecareer_url = "https://www.livecareer.com/resume-search/r/software-engineer-1a723df48582480f91a70ffee2f8da7f"

class JobSpiderResumeFetcher:
	def __init__(self):
		self.jobs_spider_url = "http://www.jobspider.com/job/resume-search-results.asp/words_java/searchtype_1"

	def fetch_resumes_page(self, page_number):
		r = requests.get(self.jobs_spider_url + '/page_' + str(page_number), proxies=proxies)
		self.resumes_page = r.text
		print("downloaded resume page:", page_number)

	def fetch_resume_files(self):
		resume_urls = re.findall('view-resume-\\d+\\.html', self.resumes_page)
		print("resume urls retrieved")

		for url_suffix in resume_urls:
			url = "http://www.jobspider.com/job/" + url_suffix
			print("connecting with", url)
			f = open("resumes/" + url_suffix, "w", encoding='utf-8')
			r = requests.get(url, proxies=proxies)
			print("html", url, "downloaded, OK")
			f.write(r.text)
			f.close()
