


class Resume:
    def __init__(self, field_map):
        self.experience = field_map['Experience']
        self.skills = field_map['Skills']
        self.education = field_map['Education']
        self.desired_wage = field_map['Desired Wage']
        self.us_work_authorization = field_map['U.S. Work Authorization']
        self.desired_industry = field_map['Desired Industry']
        self.id = field_map['id']