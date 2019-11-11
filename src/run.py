from resumes.fetch.resume_fetcher import JobSpiderResumeFetcher
from vacancy_fetcher import JobSpiderVacancyFetcher
from resumes.parse.job_spider_parser import JobSpiderHTMLResumeParser
import resumes.parse.job_spider_parser as sp
from os import listdir


def fetch_resumes():
    fetcher = JobSpiderResumeFetcher()
    for page_number in range(1, 10):
        fetcher.fetch_resumes_page(page_number)
        fetcher.fetch_resume_files()


def fetch_vacancies():
    fetcher = JobSpiderVacancyFetcher()
    for page_number in range(1, 2):
        fetcher.fetch_vacancy_page(page_number)
        fetcher.fetch_vacancy_files()


def print_resume(resume):
    print("RESUME #" + resume['id'], '\n')
    for field in sp.field_set:
        print(field + ':', resume[field])
    print('\n', '\n')


def parse_resumes():
    resumes = []
    for fname in listdir('resumes'):
        parser = JobSpiderHTMLResumeParser()
        print(fname)
        f = open('resumes/' + fname)
        parser.feed(f.read())

        resume = parser.get_resume()
        resume['id'] = fname
        resumes.append(resume)

    return resumes


fetch_resumes()

resumes = parse_resumes()

for r in resumes[:20]:
    print_resume(r)