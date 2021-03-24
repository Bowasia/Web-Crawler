from bs4 import BeautifulSoup
import csv
with open("11_personal.html", "r") as fp: #automate the file name
    soup = BeautifulSoup(fp, "html.parser")
    print(soup)

#url test case: https://www.facebook.com/neem.tomzii/about_contact_and_basic_info

for about_container in soup.find_all("div", attrs={"class":['dati1w0a','tu1s4ah4','f7vcsfb0','discj3wi']}):
    for contact_and_web_social_link in about_container.find_all("div", attrs={"class":'tu1s4ah4'}):
        content = contact_and_web_social_link.find_all("span", attrs={"class":['d2edcug0' 'hpfvmrgz','qv66sw1b','c1et5uql','gk29lw5a','a8c37x1j','keod5gw0','nxhoafnm','aigsh9s9','tia6h79c','fe6kdd0r','mau55g9w','c8b282yb','iv3no6db''a5q79mjw','g1cxx5fr','lrazzd5p','oo9gr5id'],"dir":'auto'})

        print(content)
        print('\n\n\n')








'''

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


'''



'''
with open('profile_contact.csv','w') as f:
    write = csv.DictWriter(f, fieldnames = fields)
    write.writeheader()
    for num in data :
        write.writerow(num)



    Big space | div class="dati1w0a tu1s4ah4 f7vcsfb0 discj3wi"
    Contact info & Website and social link use the same box class | div class"tu1s4ah4"

    -Contact info-

    No contact info to show [inside Contact info]| div class="rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr o8rfisnq p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt"


    -Website and social link-

    If have info [type per div eg. line and ig then have two div with this class ] | div class= rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw jifvfom9 gs1a9yip owycx6da btwxx1t3 jb3vyjys b5q2rw42 lq239pai mysgfdmx hddg9phg

    IG
    Instagram link and IG name | a class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8" rel="nofollow noopener" role="Link" tabindex="0" target="_blank"
    Tell that it is IG [IG holder] | span class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a sq6gx45u a3bd9o3v knj5qynh m9osqain hzawbc8m"
***The word "Instagram" is in div in span ^^^ without css***

    LINE







'''
