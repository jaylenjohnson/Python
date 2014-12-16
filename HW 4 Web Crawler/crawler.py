import urllib.request
from urllib.error import  URLError
import re
import pickle

webcontent = []
def visit_url(url, domain):
    global crawler_backlog

    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")

            # Use headers <h1> for search
            regexp_header = re.compile('>(?P<text>(.*))</h1>')           
            regexp_url = re.compile("http://"+domain+"[/\w+]*")

            result = regexp_header.search(content_string, re.IGNORECASE)
            
            if result:
                text = result.group("text")
                webcontent.append((url, text))

            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")

#Pickle the web content
f = open('web_data.pickle', 'bw')
pickle.dump(webcontent, f)
f.close()