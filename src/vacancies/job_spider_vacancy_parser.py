from html.parser import HTMLParser
from common.parser import try_add_field, format


vacancy_fields = {
    'employer name',
    'location',
    'wage',
    'job code',
    'date posted',
    'category'
}

satisfying_desc_chars_n = 100

class JobSpiderHTMLVacancyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.field_map = dict()
        self.processing_description = False
        self.body_chars_read = 0
        self.body = []


    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'table' and self.body_chars_read > satisfying_desc_chars_n:
            self.processing_description = False

    def handle_endtag(self, tag):
        if tag.lower() == 'table' and self.body_chars_read > satisfying_desc_chars_n:
            self.processing_description = False

    def handle_data(self, data):
        if data.isspace():
            return

        succeeded = try_add_field(data, self.field_map, vacancy_fields)
        if succeeded:
            self.processing_description = True
        if not succeeded and self.processing_description:
            formatted = format(data)
            self.body.append(formatted)
            self.body_chars_read += len(formatted)

    def get_vacancy(self):
        return self.field_map.copy(), self.body

