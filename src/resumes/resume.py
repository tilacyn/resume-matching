



class Resume:
    def __init__(self, field_map):
        self.experience = field_map['Experience']
        self.skills = field_map['Skills']
        self.education = field_map['Education']
        self.desired_wage = field_map['Desired Wage']
        self.us_work_authorization = field_map['U.S. Work Authorization']
        self.desired_industry = field_map['Desired Industry']
        self.id = field_map['id']
        self.fmap = field_map
        self.label = None

    def print(self):
        print("Resume #" + self.id)
        for key in self.fmap.keys():
            print(key + ":", self.fmap[key], '\n')

    def set_label(self, label):
        self.label = label