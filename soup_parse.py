import csv
from bs4 import BeautifulSoup

with open("FB_rubhewtookyang_11_03_2021_16-49-51.html", "r") as fp:
    soup = BeautifulSoup(fp, "html.parser")


for link in soup.find_all("a", attrs={"class": ['oajrlxb2','g5ia77u1','qu0x051f','esr5mh6w','e9989ue4','r7d6kgcz','rq0escxv','nhd2j8a9','nc684nl6','p7hjln8o','kvgmc6g5','cxmmr5t8','oygrvhab','hcukyx3x','jb3vyjys','rz4wbd8a','qt6c0cv9','a8nywdso','i1ao9s8h','esuyzwwr','f1sip0of','lzcic4wl','oo9gr5id','gpro0wi8','lrazzd5p'],"aria-hidden":"true","role":"link","tabindex":"-1"}):
    print(link.get('href'))
    print("complete one loop")
    #print(link)
    #print(link.attrs['href'])

for time_posted in soup.find_all("span", attrs={"class": ['b6zbclly','myohyog2','l9j0dhe7','aenfhxwr','l94mrbxd','ihxqhq3m','nc684nl6','t5a262vz','sdhka5h4']}):
    print(time_posted.html())
