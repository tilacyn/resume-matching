from html.parser import HTMLParser


field_set = {
    'Desired Industry',
    'U.S. Work Authorization',
    'Desired Job Location',
    'Type of Position',
    'Desired Wage'
}


class JobSpiderHTMLParser(HTMLParser):
    def set_props(self):
        self.field_map = dict()

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

