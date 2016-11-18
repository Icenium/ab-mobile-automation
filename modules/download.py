import sys
from modules.request_helpers import *
from modules.constants import *

def download_resources(resources, settings):
	http = httplib2.Http()
	printf('Downloading resources ...')
	for r in resources:
		filename = settings.configuration['filenames'][r['type']][r['platform']]

		resp, content = http.request(r['url'], "GET")
		with open(filename, 'wb') as f:
			f.write(content)