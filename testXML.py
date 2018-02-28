#!/usr/bin/python3
#
#program to import member info from XML

from xml.dom.minidom import parse
import xml.dom.minidom

#open xml document using minidom parser
domTree = xml.dom.minidom.parse("/media/azem/B839-34C6/Programmeren/library/ledenlijst.xml")
lijst = domTree.documentElement

#put all members into a list
membersList = lijst.getElementsByTagName("lid")

#print member info
for member in membersList:
    print("***Lid***")
    name = member.getElementsByTagName("naam")[0]
    print("Naam: %s" % name.childNodes[0].data)
    dateOfBirth = member.getElementsByTagName("geboorteDatum")[0]
    print("Geboorte datum: %s" % dateOfBirth.childNodes[0].data)
    address = member.getElementsByTagName("adres")[0]
    print("Adres: %s" % address.childNodes[0].data)
    mail = member.getElementsByTagName("email")[0]
    print("E-mail: %s" % mail.childNodes[0].data)
