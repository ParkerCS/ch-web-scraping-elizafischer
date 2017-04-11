# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect their twitter feed.
# You'll notice that the tweets are stored in a ordered list <ol></ol>,
# and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and urllib to grab the text contents of the tweets
# located on the twitter page you chose.  The .text attribute will supply the content of a soup object.
# Have fun.  Again, nothing explicit. (15pts)

import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/emmawatson?lang=en"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
soup.prettify()
data = [x.text.strip() for x in soup.findAll("p", {"class": "js-tweet-text"})]

print("Emma Watson's Most Recent Tweets: ")
for thing in data:
    print(thing, "\n")