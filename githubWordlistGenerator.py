from bs4 import BeautifulSoup
import sys
import requests
import json

if(sys.argv.__len__() < 4):
    print("Usage: python3 githubWordlistGenerator.py -u <url> -o <output file>")
    print("Usage: python3 githubWordlistGenerator.py -u https://github.com/ipfire/ipfire-2.x/ -o ipfireWordlist")
    print("Usage: python3 githubWordlistGenerator.py -u https://github.com/ipfire/ipfire-2.x/tree/master/html/cgi-bin -o ipfireWordlist")
else:
    url = sys.argv[2]
    outputFile = sys.argv[4]
    req = requests.get(url)
    wordlist = []
    if(url.split('/').__len__() < 8):
        if(req.status_code == 200):
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            a_tags = soup.find_all('a',class_="Link--primary")
            for tag in a_tags:
                
                if(tag.attrs['class'].__len__() == 2):
                    if('js-navigation-open' in tag.attrs['class']):
                        wordlist.append(tag.text)
            
        else:
            print("Error -> status code %s" %(req.status_code))
    else:
        ret = req.text
        obj = json.loads(ret)
        for item in obj['payload']['tree']['items']:
            wordlist.append(item['name'])
        pass
    with open("./%s" %(outputFile), 'w') as file:
        for i in wordlist:
            file.write("%s\n" %(i))
