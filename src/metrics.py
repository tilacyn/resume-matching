from resumes.resume import Resume
from vacancies.vacancy import Vacancy
import spacy


nlp = spacy.load('en_core_web_sm')

def format(word):
    return word.lower()

def words_map(resume):
    #for key in resume.fmap.keys:
    pass


#def words_match(resume, vacancy):


def analyze_resume(resume):
    experience = " ".join(resume.experience)
    doc = nlp(experience)
    org_entities = []
    for entity in doc.ents:
        if entity.label_ == "ORG":
            org_entities.append(entity.text.lower())
    return org_entities

def analyze_vacancy(vacancy):
    body = " ".join(vacancy.body)
    doc = nlp(body)
    org_entities = []
    for entity in doc.ents:
        if entity.label_ == "ORG":
            org_entities.append(entity.text.lower())
    return org_entities

def matches(resume_kws, vacancy_kws):
    return set(resume_kws).intersection(vacancy_kws)