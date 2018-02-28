#!/usr/bin/python3
class member:
    """class of library members"""
    memCount = 0
    
    def _init_(self, name, address):
        self.name = name
        self.address = address
        member.memCount += 1
        
    def printMemInfo(self):
        print( "Naam: ", self.name, ", Adres: ", self.address)

def printLedenLijst(ledenlijst):
	"""This function prints member list"""
	for lid in range(len(ledenlijst)):
		ledenlijst[lid].printMemInfo()

def addNewMembers():
   name = input("Geef naam: ")
   address = input("Geef adres: ")
   newMember = member(name, address)
   return newMember

def addLeden(ledenlijst):
	"""This function adds members"""
	answer = 'y'
    while answer == 'y':
        ledenlijst.append(addNewMembers())
        answer = input("Do you want to add new member?")


def assignID(ledenlijst):
	"""This function assigns ID to member"""
	pass

def menu(ledenlijst):
	"""This function enables interactive mode"""
	option = ''
	while option != 'q':
		print('Welkom bij de bieb!')
		print('Kies uit de volgende opties:')
		print('Print ledenlijst: p')
		print('Voeg nieuw lid toe: a')
		print('Sluit af: q')
		option = input('keuze: ')

		#process user input
		if option == 'p':
			printLedenLijst(ledenlijst)
		elif option == 'a':
			addLeden(ledenlijst)
		elif option == 'q':
			continue
		else:
			print('Invalid option!!!')

#function call: menu()

menu(ledenlijst)

print('Program exit, bye!')
