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


def print_contacts(book):
	for e in book:
		print e


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
	count = 2
	count += 1
	person = "name" + str(count)
	person = Contact()
	person.name = name
	person.number = number
	person.email = email
				
def is_phonenumber(text):
	return "".join(text.split("-")).isdigit()	

if __name__ == "__main__":
	# Actual program
	print "This is the address book"
	while True:
		
		choice = get_choice()	
		
		if choice == "1":
			print name1.__dict__	
			
						
			
			
			
		if choice == '2':
			contactlist = []
			print "These are the contacts"
			print ""
			contactlist.append(name1.__dict__)
			contactlist.append(name2.__dict__)
			for e in contactlist:
				if e == 'name':
					print e
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
			
		
	
	
	
		