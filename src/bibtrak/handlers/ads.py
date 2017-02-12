import urllib.request
import json
import pprint

#def fetch(id):
auth_token = input("Enter Authorization Code: ")
bibcode= input("Bibcode: ")

#def set_up(auth_, id_)
url = (
	"https://api.adsabs.harvard.edu/v1/search/query?q=" +
	bibcode + 
	"&fl=" +
	",".join([
		"author",
		"title",
		"id",
		"keyword",
		"pubdate",
		"year",
	])
)
req = urllib.request.Request(url)
req.add_header("Authorization", "Bearer " + auth_token)
response = urllib.request.urlopen(req)
res = response.read()
paper = json.loads(res.decode())
bib_info = paper['response']['docs'][0]

#def mod_dir()
bib_info["bibcode"] = bibcode
bib_info["adsurl"] = "http://adsabs.harvard.edu/abs/" + bibcode

pprint.pprint(bib_info)






 
