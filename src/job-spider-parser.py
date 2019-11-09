import html.parser


class JobSpiderHTMLParser(HTMLParser):
	def set_props():
		self.field_set = {'Desired industry', 'U.S. Work Authorization'}
		self.field_map = map()


	def handle_starttag(self, tag, attrs):
		pass

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		for key in self.field_set:
			if data.startswith(key):
				field_map[key] = data