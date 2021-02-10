"""
Brock Francom
A02052161
CS-1440
Erik Falor
12/8/2018
Recursive web crawler
"""
import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import time

def run():
    start = time.time()
    if len(sys.argv) < 1:
        print("Usage: python recursiveWebCrawler.py absoluteURL [maxDepth] [file]")
    try:
        url = sys.argv[1]
        if (url.startswith('http://') == False) and (url.startswith('https://') == False):
            print("Error: Invalid URL supplied.\nPlease supply an absolute URL to this program")
            sys.exit()
    except IndexError:
        print("Error: no URL supplied")
        sys.exit()
    try:
        maxdepth = int(sys.argv[2])
    except IndexError:
        maxdepth = 3
    try:
        file = sys.argv[3]
        print("Printing results to " + file)
    except IndexError:
        print("No file specified, printing to screen")
        file = sys.stdout

    if file != sys.stdout:
        with open(file, "w") as m:
            print("Crawling " + url + " to a maximum depth of " + maxdepth)
            m.write("Crawling " + str(url) + " to a maximum depth of " + str(maxdepth) + "\n")
            m.write(url + "\n")
            crawlFile(url, depth, maxdepth, visited, numberFound, m, variable)
            m.write("After crawling " + str(url) + " to a maximum depth of " + str(maxdepth) + "\n")
            m.write("Searched " + str(len(visited)) + " websites.\n")
            m.write("Found " + str(len(numberFound)) + " urls.\n")
            end = time.time()
            time1 = str(end - start)
            m.write("The program took " + time1 + " seconds to run.\n")
            print("Done")
    else:        
        print("Crawling " + url + " to a maximum depth of " + str(maxdepth))
        print(url)
        crawl(url, depth, maxdepth, visited, numberFound)   
        end = time.time()
        time2 = str(end - start)
        print("After crawling " + str(url) + " to a maximum depth of " + str(maxdepth))
        print("Searched " + str(len(visited)) + " websites.")
        print("Found " + str(len(numberFound)) + " urls.")
        print("The program took " + time2 + " seconds to run.")

numberFound = []   
depth = 1    
visited = []
variable = 0
passwords = []
def crawlFile(url, depth, maxdepth, visited, numberFound, m, variable):
    if (depth == maxdepth) or (url in visited):
        return
    try:
        response = requests.get(url)
    except Exception as e:
        m.write(str('    '*(depth)) + "Failed to get " + url + " because " + str(e) + "\n")
        return
    try:
        urls = []
        oParsed = urlparse(url)
        visited.append(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        links = soup.find_all('a')
        if links:
            for a in links:
                i = a.get('href')                                    
                parsed = urlparse(i)
                if ((parsed.scheme != 'http') and (parsed.scheme != 'https')):
                    continue
                if ((parsed.scheme == '') and (parsed.netloc != '')):
                    i = oParsed.scheme + "://" + parsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme != '') and (parsed.netloc == '')):
                    i = parsed.scheme + "://" + oParsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme == '') and (parsed.netloc == '')):
                    i = oParsed.scheme + "://" + oParsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme != '') and (parsed.netloc != '')):
                    if i != None:
                        urls.append(i)
        else:
            m.write(str('    '*(depth)) + "No hyperlinks were found in this document" + "\n")
    except Exception as e:
        m.write(str('    '*(depth)) + "An exception occurred: " + str(e) + "\n")      
    for url in urls:
        if url not in visited:
            if (url not in numberFound):
                numberFound.append(url)
                m.write(str('    '*(depth)) + url + "\n")
                if ((variable % 500) == 0):
                    print("Working...")
                variable += 1
                forms = soup.find_all('form')
                for form in forms:
                    a = form.find('Password')
                    print(a)
                    passwords.append(a)

            crawlFile(url, depth+1, maxdepth, visited, numberFound, m, variable)

def crawl(url, depth, maxdepth, visited, numberFound):
    if (depth == maxdepth) or (url in visited):
        return
    try:
        response = requests.get(url)
    except Exception as e:
        print(str('    '*(depth)) + "Failed to get " + url + " because " + str(e))
        return
    try:
        urls = []
        oParsed = urlparse(url)
        visited.append(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        links = soup.find_all('a')
        if links:
            for a in links:
                i = a.get('href')
                parsed = urlparse(i)
                if ((parsed.scheme != 'http') and (parsed.scheme != 'https')):
                    continue
                if ((parsed.scheme == '') and (parsed.netloc != '')):
                    i = oParsed.scheme + "://" + parsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme != '') and (parsed.netloc == '')):
                    i = parsed.scheme + "://" + oParsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme == '') and (parsed.netloc == '')):
                    i = oParsed.scheme + "://" + oParsed.netloc + parsed.path
                    if i != None:
                        urls.append(i)
                elif ((parsed.scheme != '') and (parsed.netloc != '')):
                    if i != None:
                        urls.append(i)
        else:
            print(str('    '*(depth)) + "No hyperlinks were found in this document")
    except Exception as e:
        print(str('    '*(depth)) + "An exception occurred: " + str(e))        
    for url in urls:
        if (url not in visited):
            if (url not in numberFound):
                numberFound.append(url)
                print(str('    '*(depth)) + str(url))
                forms = soup.find_all('form')
                for form in forms:
                    a = form.action
                    print(a)
                    passwords.append(form)

            crawl(url, depth+1, maxdepth, visited, numberFound)

