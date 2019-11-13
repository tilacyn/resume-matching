

class Vacancy:
    def __init__(self, fmap, body, fname):
        self.id = fname
        self.employer_name = fmap['Employer Name']
        self.location = fmap['Location']
        self.wage = fmap['Wage']
        self.job_code = fmap['Job code']
        self.date_posted = fmap['Date Posted']
        self.category = fmap['Category']

    def