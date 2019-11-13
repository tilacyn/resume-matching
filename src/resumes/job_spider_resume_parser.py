from html.parser import HTMLParser
from common.parser import format, try_add_field, related


resume_fields = {
    'Desired Industry',
    'U.S. Work Authorization',
    'Desired Job Location',
    'Type of Position',
    'Desired Wage',
    'Job Level',
    'Highest Degree Attained',
    'Willing to Travel',
    'Willing to Relocate',
    'Date Posted'
}

special_resume_fields = {
    'Education',
    'Experience',
    'Objective',
    'Skills',
    'Additional Information',
    'Candidate Contact Information'
}



class JobSpiderHTMLResumeParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.field_map = dict()
        self.wait_for_special_fields = dict()
        for field in special_resume_fields:
            self.wait_for_special_fields[field] = False
            self.field_map[field] = []


    def handle_data(self, data):
        try_add_field(data, self.field_map, resume_fields)

        for field in special_resume_fields:
            if related(data, field):
                for other_special_field in special_resume_fields:
                    if other_special_field != field:
                        self.wait_for_special_fields[other_special_field] = False
                self.wait_for_special_fields[field] = True
                return

        if data.isspace():
            return

        for field in special_resume_fields:
            if self.wait_for_special_fields[field]:
                #print(field, self.field_map[field])
                self.field_map[field].append(format(data))


    def get_resume(self):
        return self.field_map.copy()



