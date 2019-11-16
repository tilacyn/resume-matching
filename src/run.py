import itertools
import numpy as np
from os import listdir

import metrics
import resumes.job_spider_resume_parser as sp
from resumes.job_spider_resume_parser import JobSpiderHTMLResumeParser
from resumes.resume import Resume
from resumes.resume_fetcher import JobSpiderResumeFetcher
from vacancies.job_spider_vacancy_parser import JobSpiderHTMLVacancyParser
from vacancies.vacancy import Vacancy
from vacancies.vacancy_fetcher import JobSpiderVacancyFetcher


def fetch_resumes():
    fetcher = JobSpiderResumeFetcher()
    for page_number in range(1, 20):
        fetcher.fetch_resumes_page(page_number)
        fetcher.fetch_resume_files()


def fetch_vacancies():
    fetcher = JobSpiderVacancyFetcher()
    for page_number in range(1, 20):
        fetcher.fetch_vacancy_page(page_number)
        fetcher.fetch_vacancy_files()


def parse_resumes():
    resumes = []
    observed_resumes = listdir('resumes')
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
    observed_vacancies = listdir('vacancies')
    for fname in observed_vacancies:
        parser = JobSpiderHTMLVacancyParser()
        f = open('vacancies/' + fname)
        parser.feed(f.read())
        print(fname)

        fmap, body = parser.get_vacancy()
        vacancies.append(Vacancy(fmap, body, fname))
    return vacancies

def calculate_stats(all_matches, n):
    stats = np.zeros(n)
    for i in range(n):
        for x in all_matches:
            if len(x[2]) == i:
                stats[i] += 1
    return stats


def count_metrics(resumes, vacancies):
    resumes_kws = list(map(lambda r: [r.id, metrics.analyze_resume(r)], resumes))
    vacancies_kws = list(map(lambda v: [v.id, metrics.analyze_vacancy(v)], vacancies))

    all_matches = []

    for r, v in itertools.product(resumes_kws, vacancies_kws):
        all_matches.append([r[0], v[0], metrics.matches(r[1], v[1])])

    all_matches = sorted(all_matches, key=lambda x: len(x[2]))

    stats = calculate_stats(all_matches, 20)
    return all_matches, stats

#fetch_resumes()

#resumes = parse_resumes()

#vacancies = parse_vacancies()

#for v in vacancies:
    #v.print()
    #print('\n')

#for r in resumes:
#    print_resume(r)

#all_matches, stats = count_metrics(resumes, vacancies)