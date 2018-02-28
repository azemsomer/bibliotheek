#!/usr/bin/python3
#
#Program to add library members

class member:
    """class of library members"""
    memCount = 0
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        member.memCount += 1
        
    def printMemInfo(self):
        print( "Name: ", self.name, ", Address: ", self.address)
        
#function to add new member
def addNewMembers():
   name = input("Give name: ")
   address = input("Give address: ")
   newMember = member(name, address)
   return newMember

#function to show number of members
#def dispNumb(self):
#    print("Aantal leden: ", memCount)

#empty list
membersList = []

#set answer
answer = 'y'

#while-loop to fill membersList
while answer == 'y':
    membersList.append(addNewMembers())
    answer = input("Do you want to add new member?")

#print member list
for lid in range(len(membersList)):
    membersList[lid].printMemInfo()

#printer mumber of members in list
total = len(membersList)
print("Aantal leden: ", total)

#write added members to file
with open("azemsomer/testFile2.txt", 'w', encoding = 'utf-8') as f:
    for lid in range(len(membersList)):
        dataLine = membersList[lid].name + ', ' + membersList[lid].address + '\n'
        f.write(dataLine)

#close file
f.close
