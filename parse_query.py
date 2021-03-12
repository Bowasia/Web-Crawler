#!/usr/bin/python3

from pyquery import PyQuery as pq
from lxml import etree
import urllib
with open("FB_rubhewtookyang_11_03_2021_16-49-51.html", "r") as f:

    contents = f.read()

    doc = pq(contents)
    text = doc('a').html()
    time = doc('div.du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0')

    for b in time:
        print(time.children("a.ajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p").text())


    #print(doc)
    #print(time)
    #class of span time
    #.b6zbclly.myohyog2.l9j0dhe7.aenfhxwr.l94mrbxd.ihxqhq3m.nc684nl6.t5a262vz.sdhka5h4

    #class of link
    #.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p

    #print(html_href)
