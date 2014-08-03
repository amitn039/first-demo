# This program is an address book
import json
import os.path

contact_book = {}
contact_book["Amit"] = {"phone" : "123-4567" , "email" : "amit@gmail.com"}
contact_book["John"] = {"phone" : "123-4566" , "email" : "john@gmail.com"}
contact_book["Adam"] = {"email" : "adam@gmail.com"}

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
	print "6 - Load a contact book"
	print "7 - Save contact book"
	choice = raw_input()
	return choice

def make_contact():
	print "What is the name of your new contact?"
	name = raw_input()
	print "What is " + name + "'s phone number?"
	number = raw_input()
	print "What is " + name + "'s email?"
	email = raw_input()
	contact_book[name] = {"phone" : number , "email" : email}
				
def load_addressbook():
	print "What is the file name?"
	filename = raw_input()
	if os.path.isfile(filename):
		file = open(filename)
		data = json.load(file)
		global contact_book 
		contact_book = data	
		print "Contact book successfuly loaded"
	else:
		print "Could not find the file"


def save_addressbook():
	print "Please type a filename"
	filename = raw_input()
	json.dump(contact_book, open(filename, 'w'))

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
					if contact == contact_book[i]["phone"]:
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
		if choice == "6":
			load_addressbook()
		if choice == "7":
			save_addressbook()
		if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
			print "That is not a valid choice"
			
		
	
	
	
		