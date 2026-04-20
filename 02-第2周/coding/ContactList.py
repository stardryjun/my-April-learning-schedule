class ContactList:
    def __init__(self,names,phone_numbers):
        self.dicts = dict(zip(names, phone_numbers))
        self._iter = iter(self.dicts.items())
    def __iter__(self):
        self._iter = iter(self.dicts.items())
        return self
    def __next__(self):
        return next(self._iter)
    def print_contacts(self):
        i = len(self.dicts)
        while i > 0:
            name, phone = next(iter(self.dicts.items()))
            print(f"{name}: {phone}")
            i -= 1

names = ["Alice", "Bob", "Charlie"]
phone_numbers = ["123-456-7890", "987-654-3210", "555-555-5555"]
contact_list = ContactList(names, phone_numbers)
contact_list.print_contacts()