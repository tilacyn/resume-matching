

class Vacancy:
    def __init__(self, fmap, body, fname):
        self.id = fname
        self.employer_name = fmap['employer name']
        self.location = fmap['location']
        self.wage = fmap['wage']
        self.job_code = fmap['job code']
        self.date_posted = fmap['date posted']
        self.category = fmap['category']
        self.fmap = fmap
        self.body = body

    def print(self):
        print("Vacancy #" + self.id)
        for key in self.fmap.keys():
            print(key + ":", self.fmap[key])
        print(self.body)