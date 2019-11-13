from html.parser import HTMLParser
from common.parser import try_add_field, format


vacancy_fields = {
    'Employer Name',
    'Location',
    'Wage',
    'Job code',
    'Date Posted',
    'Category'
}


class JobSpiderHTMLVacancyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.field_map = dict()
        self.inner_table_number = 0
        self.body = []


    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'table':
            self.inner_table_number += 1

    def handle_endtag(self, tag):
        if tag.lower() == 'table':
            self.inner_table_number -= 1
        if self.inner_table_number == 0:
            self.inner_table_number = -1

    def handle_data(self, data):
        if self.inner_table_number <= 0:
            return
        try_add_field(data, self.field_map)
        if self.inner_table_number == 1:
            self.body.append(format(data))

    def get_vacancy(self):
        return self.field_map.copy(), self.body

