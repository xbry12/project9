from peewee import *

db = PostgresqlDatabase('contactlist', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()

# contact list:
# first name, last name, email, phone number
# table is called 'contacts'


class BaseModel(Model):
    class Meta:
        database = db


class Contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    number = CharField()

 # do CRUD IN PYTHON

 # enter option 1 to create - done
 # option2 list -> read - done
 # option 3 edit contact - UPDATE
 # option 4 delete contact - DELETE
 # option 5 exit - code will run a loop


print("Hello and Welcome to My Contact List!")

all_contacts = Contacts.select()
for c in all_contacts:
    print(c.first_name)

search_name = input("Enter a name to search: ")



# Read
search_result = Contacts.get(Contacts.first_name == search_name)
print(search_result.email)

print("Now we will create a new Contact!")

new_firstname = input("Enter first name: ")
new_lastname = input("Enter last name: ")
new_email = input("Enter email: ")
new_fnumber = input("Enter number: ")

# Create
new_contact = Contacts(first_name=new_firstname,
                       last_name=new_lastname, email=new_email, number=new_fnumber)
new_contact.save()

# Update
update_name = input("Which name do you want to update? ")

object_b = Contacts.get(Contacts.first_name == update_name)
new_name = input("Enter new first name for this contact: ")
print("The nme has been updated!")

object_b.first_name = new_name
object_b.save()

# Delete
delete_name = input("Enter first name to delete: ")
object_c = Contacts.get(Contacts.first_name == delete_name)
object_c.delete_instance()
print("The name has been deleted!")

