from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import csv
import time

input_link = "FB_rubhewtookyang_23_03_2021_22:35:39.html"
#input_link = sys.argv[1]+".html"
print(input_link)

fields = ['Number','Name','Link']
data_official = []
data_personal = []
num = 1


with open(input_link, "r") as fp: #automate the file name
    soup = BeautifulSoup(fp, "html.parser")

# A function to distinguish if it is a personal or official page
def distinguish(raw_link):
    obj = urlparse(raw_link)
    path = obj[2]
    if path[-1] == '/':
        return(data_official)
    else:
        return(data_personal)

#check if the profile is already add
def check_repetition(type,to_add):
    count_repeat = 0
    for info in type:
        if info["Name"] == profile_name:
            #print("This is info: \n")
            count_repeat += 1
            #print(info)

    if count_repeat == 0:
        type.append(to_add)
        global num
        num+=1


#export data as csv
def export_csv(name,type):
    export_file_name = name + '_link_1.csv'
    with open(export_file_name,'w') as f:
        write = csv.DictWriter(f, fieldnames = fields)
        write.writeheader()
        for num in type :
            write.writerow(num)



def collect_link():
    for link in soup.find_all("a", attrs={"class": ['oajrlxb2','g5ia77u1','qu0x051f','esr5mh6w','e9989ue4','r7d6kgcz','rq0escxv','nhd2j8a9','nc684nl6','p7hjln8o','kvgmc6g5','cxmmr5t8','oygrvhab','hcukyx3x','jb3vyjys','rz4wbd8a','qt6c0cv9','a8nywdso','i1ao9s8h','esuyzwwr','f1sip0of','lzcic4wl','oo9gr5id','gpro0wi8','lrazzd5p'],"aria-hidden":"true","role":"link","tabindex":"-1"}):
        global href
        global profile_name

        href = link.get('href')
        print(href)
        profile_name = link.a.get('aria-label')

        Dic = {"Number":num,"Name":profile_name,"Link":href}
        link_type = distinguish(href)
        check_repetition(link_type,Dic)

'''
#get name and link to profile page
for link in soup.find_all("a", attrs={"class": ['oajrlxb2','g5ia77u1','qu0x051f','esr5mh6w','e9989ue4','r7d6kgcz','rq0escxv','nhd2j8a9','nc684nl6','p7hjln8o','kvgmc6g5','cxmmr5t8','oygrvhab','hcukyx3x','jb3vyjys','rz4wbd8a','qt6c0cv9','a8nywdso','i1ao9s8h','esuyzwwr','f1sip0of','lzcic4wl','oo9gr5id','gpro0wi8','lrazzd5p'],"aria-hidden":"true","role":"link","tabindex":"-1"}):
    href = link.get('href')
    profile_name = link.a.get('aria-label')
    fields = ['Number','Name','Link']
    Dic = {"Number":num,"Name":profile_name,"Link":href}

    link_type = distinguish(href)
    print(link_type)


'''
collect_link()
print(data_official)
print('\n')
print(data_personal)

time_1 = str(int(time.time()))


export_csv("data_personal_" + time_1,data_personal)
export_csv("data_official_" + time_1,data_official)









#&sk=about
#^^^ append at the link to go to about page
