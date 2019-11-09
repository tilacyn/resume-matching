import requests



proxies = {
	"https": "https://207.144.111.230:8080"
}


livecareer_url = "https://www.livecareer.com/resume-search/r/software-engineer-1a723df48582480f91a70ffee2f8da7f"
jobs_spider_url = "http://www.jobspider.com/job/view-resume-82237.html"

def fetch_resumes(url):
	r = requests.get(url, proxies=proxies)
	return r



result = fetch_resumes(jobs_spider_url)

f = open("resume_response_job_spider", "w")

f.write(result.text)

f.close()