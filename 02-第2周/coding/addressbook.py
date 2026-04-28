import json,re

class AddressBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, *contact):
        for c in contact:
            self.contacts[c.name] = c
    def extend_contacts(self, contacts):
        for contact in contacts:
            self.contacts[contact.name] = contact
    def add_phone_number(self, name, phone_number):
        if name in self.contacts:
            self.contacts[name].add_phone_number(phone_number)
        else:
            self.contacts[name] = Contact(name, phone_number)
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print(f"Contact {name} not found")
    def delete_phone_number(self, name, phone_number):
        if name in self.contacts:
            contact = self.contacts[name]
            if phone_number in contact.phone_numbers:
                contact.phone_numbers.remove(phone_number)
                if not contact.phone_numbers:
                    del self.contacts[name]
            else:
                print(f"Phone number {phone_number} not found for contact {name}")
        else:
            print(f"Contact {name} not found")
    def modify_contact(self, name, new_name=None, new_phone_numbers=None):
        if new_name is None and new_phone_numbers is None:
            print("No changes provided")
            return
        if name in self.contacts:
            contact = self.contacts[name]
            if new_name:
                contact.name = new_name
                self.contacts[new_name] = contact
                del self.contacts[name]
            if new_phone_numbers is not None:
                contact.phone_numbers = new_phone_numbers
        else:
            print(f"Contact {name} not found")
    def search_contact(self, name, phone_number=None):
        if re.match(r'\d{3}-\d{3}-\d{4}',name) and not phone_number:
            phone_number = name
            name = None
            for result in self.contacts.values():
                if phone_number in result.phone_numbers:
                    return result
            print(f"Contact with phone number {phone_number} not found")
            return None
        else:
            contact = self.contacts.get(name, None)
            if contact and phone_number:
                return contact if phone_number in contact.phone_numbers else None
            return contact
    def __str__(self):
        return f"AddressBook(contacts={self.contacts})"
    def download_json(self, filename):
        with open(filename, 'w') as f:
            json.dump({name: contact.phone_numbers for name, contact in self.contacts.items()}, f, indent=4)
    def __iter__(self):
        self.names = list(sorted(self.contacts.keys()))
        return self
    def __next__(self):
        if self.names:
            return self.contacts[self.names.pop(0)]
        raise StopIteration


class Contact:
    def __init__(self, name, *phone_numbers):
        self.name = name
        self.phone_numbers = []
        for phone_number in phone_numbers:
            self.phone_numbers.append(phone_number)
    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)
    def __str__(self):
        return f"Contact(name={self.name}, phone_numbers={self.phone_numbers})"
    def __repr__(self):
        return self.__str__()

contact1 = Contact("Alice", "123-456-7890")
contact2 = Contact("Bob", "987-654-3210")
contact3 = Contact("Charlie", "555-555-5555")
address_book = AddressBook()
address_book.add_contact(contact1, contact2, contact3)
print("before modification:", address_book)
address_book.modify_contact("Alice", new_phone_numbers=["333-444-5555"])
print("Search result for Bob:", address_book.search_contact("Bob"))
address_book.add_phone_number("Alice", "111-222-3333")
print("Search result for phone number 333-444-5555:", address_book.search_contact("333-444-5555"))
address_book.delete_phone_number("Bob", "987-654-3210")
print("after modification:", address_book)
address_book.download_json("02-第2周/coding/contacts.json")

for contact in address_book:
    print(contact)