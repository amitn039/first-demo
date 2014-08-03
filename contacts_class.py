# This program is an address book
import json
import os.path

class Contact:
	name = ""
	phone = ""
	email = ""

name1 = Contact()
name1.name = "Amit"
name1.phone = "123-4567"
name1.email = "amit@gmail.com"

name2 = Contact()
name2.name = "George"
name2.phone = "123-4566"
name2.email = "george@gmail.com"


contact_book = {}
contact_book[name1.name] = name1
contact_book[name2.name] = name2        
	

def print_contacts(book):
	for key in book:
		print key


# This function gives the user the choices, and takes the users input
def get_choice():
	print "The options are;"
	print "1 - Get information"
	print "2 - List contacts"
	print "3 - Quit"
	print "4 - Create new contact"
	print "5 - Update information"
	choice = raw_input()
	return choice

def make_contact():
	print "What is the name of your contact?"
	name = raw_input()
	print "What is " + name + 's phone number?'
	number = raw_input()
	print "What is " + name + 's email?'
	email = raw_input()
	person = Contact()
	person.name = name
	person.number = number
	person.email = email
	contact_book[name] = person
	
	
				
def is_phonenumber(text):
	return "".join(text.split("-")).isdigit()	

if __name__ == "__main__":
	# Actual program
	print "This is the address book"
	while True:
		
		choice = get_choice()	
		
		if choice == "1":
			string = ''
			list = []
			print "Whose information do you want?"
 			contact = raw_input()	
			contact_number = []
			if is_phonenumber(contact): 
				for i in contact_book:
					contact_number.append(i)
					if contact == contact_book[i].phone:
						print i						 
			else:
				for e in contact_number:
						if contact != e:
							print "Could not find the contact"			
			
			if is_phonenumber(contact) == False:
				if contact in contact_book:
					print contact_book[contact]			 
				else:
 					print contact + ' is not in the contact book'
						
			
			
			
		if choice == '2':
			contactlist = []
			print "These are the contacts"
			print ""
			print_contacts(contact_book)
			print ""
		if choice == '3':
			break	
		if choice == '4':
			make_contact()
		if choice == '5':
			print "Whose information do you want to update?"
			update = raw_input()
			person = contact_book.find[update]
			print person
		if choice not in ["1", "2", "3", "4", "5"]:
			print "That is not a valid choice"
			
		
	
	
	
		