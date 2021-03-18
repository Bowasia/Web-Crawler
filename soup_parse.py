from bs4 import BeautifulSoup
import csv
with open("FB_rubhewtookyang_11_03_2021_16-49-51.html", "r") as fp: #automate the file name
    soup = BeautifulSoup(fp, "html.parser")



data =[]

for link in soup.find_all("a", attrs={"class": ['oajrlxb2','g5ia77u1','qu0x051f','esr5mh6w','e9989ue4','r7d6kgcz','rq0escxv','nhd2j8a9','nc684nl6','p7hjln8o','kvgmc6g5','cxmmr5t8','oygrvhab','hcukyx3x','jb3vyjys','rz4wbd8a','qt6c0cv9','a8nywdso','i1ao9s8h','esuyzwwr','f1sip0of','lzcic4wl','oo9gr5id','gpro0wi8','lrazzd5p'],"aria-hidden":"true","role":"link","tabindex":"-1"}):
    href = link.get('href')
    profile_name = link.a.get('aria-label')
    #print(link.get('href')) #Profile link
    #print(link.a.get('aria-label')) #Profile name
    fields = ['Name','Link']
    Dic = {"Name":profile_name,"Link":href}
    data.append(Dic)
print(data)

with open('profile_link_1.csv','w') as f:
    write = csv.DictWriter(f, fieldnames = fields)
    write.writeheader()
    for num in data :
        write.writerow(num)

#&sk=about
#^^^ append at the link to go to about page
