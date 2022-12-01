"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. 
If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""

import random

class Shortener:
    
    def __init__(self):
        self.UrlDict = dict()
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.alphanumericList = list(letters+letters.upper()+"0123456789") 
        
    def generateShortUrl(self):
        short = ""
        while short == "":
            while len(short) < 6:
                short += random.choice(self.alphanumericList)
            if short in self.UrlDict.keys():
                short = ""
        return short
    
    def shorten(self, url):
        if url not in self.UrlDict.keys():
            self.UrlDict[url] = self.generateShortUrl()   
        return self.UrlDict[url]
    
    def restore(self, short):
        for url in self.UrlDict:
            if self.UrlDict[url] == short:
                return url
        return None
            
            
shortener = Shortener()         

fb_short = shortener.shorten("www.facebook.com")
print(fb_short)
print(shortener.restore(fb_short))
print()
yt_short = shortener.shorten("www.youtube.com")
print(yt_short)
print(shortener.restore(yt_short))
print()
fb_short = shortener.shorten("www.facebook.com")
print(fb_short)
print(shortener.restore(fb_short))
print()

