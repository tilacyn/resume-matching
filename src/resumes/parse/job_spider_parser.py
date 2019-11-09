from html.parser import HTMLParser


field_set = {
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

special_fields = {
    'Education',
    'Experience',
    'Objective',
    'Skills',
    'Additional Information',
    'Candidate Contact Information'
}


def make_prefix_by_special_field(s):
    return s + ':'


class JobSpiderHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.field_map = dict()
        self.wait_for_special_fields = dict()
        for field in special_fields:
            self.wait_for_special_fields[field] = False
            self.field_map[field] = []

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        #if not data.isspace():
            #print(data)
            #print()
        for key in field_set:
            if data.startswith(key):
                value_start_index = len(key) + 2
                self.field_map[key] = data[value_start_index:]

        for field in special_fields:
            if data.startswith(make_prefix_by_special_field(field)):
                for other_special_field in special_fields:
                    if other_special_field != field:
                        self.wait_for_special_fields[other_special_field] = False
                self.wait_for_special_fields[field] = True
                return

        if data.isspace():
            return

        for field in special_fields:
            if self.wait_for_special_fields[field]:
                self.field_map[field].append(data)


    def process_special_fields(self):
        pass

    def get_resume(self):
        return self.field_map.copy()

