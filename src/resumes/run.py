from fetch.resume_fetcher import JobSpiderResumeFetcher
from parse.job_spider_parser import JobSpiderHTMLParser
from os import listdir


#fetcher = JobSpiderResumeFetcher()
#fetcher.fetch_resumes_page()
#fetcher.fetch_resume_files()


resumes = []

parser = JobSpiderHTMLParser()
for fname in listdir('resumes'):
	print(fname)
	f = open('resumes/' + fname)
	parser.set_props()
	parser.feed(f.read())
	resumes.append(parser.field_map)
