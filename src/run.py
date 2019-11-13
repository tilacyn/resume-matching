from os import listdir
from vacancies.vacancy import Vacancy

import resumes.job_spider_resume_parser as sp
from resumes.job_spider_resume_parser import JobSpiderHTMLResumeParser
from resumes.resume import Resume
from resumes.resume_fetcher import JobSpiderResumeFetcher
from vacancies.job_spider_vacancy_parser import JobSpiderHTMLVacancyParser
from vacancies.vacancy_fetcher import JobSpiderVacancyFetcher


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
    observed_resumes = listdir('resumes')[:5]
    for fname in observed_resumes:
        parser = JobSpiderHTMLResumeParser()
        print(fname)
        f = open('resumes/' + fname)
        parser.feed(f.read())

        resume_field_map = parser.get_resume()
        resume_field_map['id'] = fname
        resumes.append(Resume(resume_field_map))

    return resumes

def parse_vacancies():
    vacancies = []
    observed_vacancies = listdir('vacancies')[:5]
    for fname in observed_vacancies:
        parser = JobSpiderHTMLVacancyParser()
        print(fname)
        f = open('vacancies/' + fname)
        parser.feed(f.read())

        fmap, body = parser.get_vacancy()
        vacancies.append(Vacancy(fmap, body, fname))



#fetch_resumes()

resumes = parse_resumes()

#for r in resumes:
#    print_resume(r)