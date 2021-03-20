import csv
from urllib.parse import urlparse
obj_personal = urlparse('https://www.facebook.com/jaeng.meesomsin.9?__cft__[0]=AZVXPchyZj4VSjARcx7HQV-wgt7lbOX3e1uzUZwnhK-BAjbYIk3Ii63-cTsCsE1kUsD3uky10lAujBsvE-jhx1wo9BOVIWuSCj1KnwHOlAOf1I9O3bQiK99-ykCYuBdZXdk&__tn__=%3C%2CP-R')
obj_official = urlparse('https://www.facebook.com/linghiwkhong/?__cft__[0]=AZX5DCBtFFb3yMkjorLrSPS2-NZZanM1eDxtvm0Km5W5kw8gALj1bVa5F_J-O4xlFl0qyrAXojpUV4VHHSNyZpxiqQ7O5lM5Q_PlkLyftLNEDgzE_uwcMnwF8ickYyEOvCk&__tn__=%3C%2CP-R')

path = obj_official[2]
print(obj_personal[2])
print(obj_official[2])

if path[-1] == "/":
    print("This is an official page")
