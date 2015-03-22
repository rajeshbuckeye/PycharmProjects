__author__ = 'Rajesh'

import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar()
opener = urllib2.build_opener((urllib2.HTTPCookieProcessor(cj)))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
      page = 'http://www.huffingtonpost.com/feeds/index.xml'

      sourceCode = opener.open(page).read()
      #print(sourceCode)
      try:
          titles = re.findall(r'<title>(.*?)></title>', sourceCode)
          #print(titles)
          links = re.findall(r'<link>(.*?)</link>', sourceCode)
          print(links)
          for title in titles:
              title = re.findall(r'<!\[CDATA\[(.*?)\]\]', title)
              #print(re.findall(r'<!\[CDATA\[(.*?)\]\]', title))
              #print(title)
          i = 0
          for link in links:
              #print(link)
              if not 'http' in link:
                  pass
              else:
                  print(i)
                  i = i+1
                  linkSource = opener.open(link).read()
                  #print(linkSource)
                  contents = re.findall(r'<p>(.*)</p>', linkSource)
                  print contents
                  # for linesOfContents in contents:
                  #     linesOfContent = re.findall(r'<p>(*.)</p>', linesOfContents)
                  #     print(linesOfContent)

      except Exception, e:
          print str(e)

    except Exception, e:
        print str(e)


main()