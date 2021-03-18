from bs4 import BeautifulSoup
import csv
with open("FB_rubhewtookyang_16_03_2021_21:31:32.html", "r") as fp: #automate the file name
    soup = BeautifulSoup(fp, "html.parser")


data =[]
num = 1
#get name and link to profile page
for link in soup.find_all("a", attrs={"class": ['oajrlxb2','g5ia77u1','qu0x051f','esr5mh6w','e9989ue4','r7d6kgcz','rq0escxv','nhd2j8a9','nc684nl6','p7hjln8o','kvgmc6g5','cxmmr5t8','oygrvhab','hcukyx3x','jb3vyjys','rz4wbd8a','qt6c0cv9','a8nywdso','i1ao9s8h','esuyzwwr','f1sip0of','lzcic4wl','oo9gr5id','gpro0wi8','lrazzd5p'],"aria-hidden":"true","role":"link","tabindex":"-1"}):
    href = link.get('href')
    profile_name = link.a.get('aria-label')
    fields = ['Number','Name','Link']
    Dic = {"Number":num,"Name":profile_name,"Link":href}
    count_repeat = 0

    #check if the profile is already add
    for info in data:
        if info["Name"] == profile_name:
            #print("This is info: \n")
            count_repeat += 1
            #print(info)

    if count_repeat == 0:
        print(count_repeat)
        data.append(Dic)
        num+=1
        print(count_repeat)


print(data)

#export data as csv
def export_csv:
    with open('profile_link_3.csv','w') as f:
        write = csv.DictWriter(f, fieldnames = fields)
        write.writeheader()
        for num in data :
            write.writerow(num)

#&sk=about
#^^^ append at the link to go to about page
