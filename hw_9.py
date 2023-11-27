USERS = {}
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'No user with given name.'
        except ValueError:
            return 'Give me name and phone, please.'
        except IndexError:
            return 'Give me name and phone, please.'
    return inner
def greeting(_):
    return 'How can I help you?'
def good_bye(_):
    return 'Good bye!'
@input_error
def add_contact(data):
    name, phone, *_ = data
    USERS[name] = phone
    return f'The user with name {name} and phone {phone} was added!'
@input_error
def change_phone(data):
    name, phone, *_ = data
    for key in USERS.keys():
        if key == name:
            USERS[name] = phone
    return f'The phone number for name {name} was changed!'
@input_error
def show_phone(data):
    return f'The phone number is: {USERS[data[0]]}'
@input_error
def show_all(_):
    result = []
    for name, phone in USERS.items():
        result.append(f'{name} - {phone}')
    return result
def unknown_command(_):
    return 'This command is unknown!'
def get_handler(user_input):
    action = user_input.split()[0].lower()
    data = user_input.split()[1:]
    try:
        handler = COMMANDS[action]
    except KeyError:
        handler = unknown_command
        if not action or action == '.':
            handler = good_bye
    return handler, data
COMMANDS = {
    'hello': greeting,
    'add': add_contact,
    'change': change_phone,
    'phone': show_phone,
    'show_all': show_all,
    'good_bye': good_bye,
    'exit': good_bye,
    'close': good_bye
    }
def main():
    flag = True
    while flag:
        user_input = input('>>> ')
        if user_input in ('good_bye', 'exit', 'close', '.'):
            flag = False
        handler, data = get_handler(user_input)
        try:
            result = handler(data)
            print(result)
        except KeyError:
            print('Unknown command')
if __name__ == '__main__':
    main()

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    

class Phone(Field):
    
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    

    class Record:
    
        de
    def __init__(self, name, value):
        self.name = name
        self.value = value


        self.name = name
    

        self.na
class AddressBook:
    
 
def __init__(self):
        self.data = {}

    
        self.data =

     
def add_record(self, record):
        self.data[record.name.value] = record.value

    
        self.data[record.name.value] = record.value

   

        self.data[record.name.value] = rec

        self.data[record.name

   
def find(self, name):
        
     
if name.value in self.data:
            
           
return self.data[name.value]
        
   
else:
            
            r

 
return None

    

 
def delete(self, name):
        if name.value in self.data:
            
        
del self.data[name.value]
            
            

  
print(f"Запис {name.value} видалено.")
        
        el

  
else:
            
            

    
print(f"Запис з ім'ям {name.value} не знайдено.")

# Приклад використання
if __name__ == "__main__":
    
  
# Створюємо об'єкт AddressBook
    address_book = AddressBook()

    
    address_book = AddressBook()

  

    address_book = A

    address_

    a
# Додаємо запис
    record1 = Record(name=
    record1 = Reco

    recor
"John", value="123-456-789")
    address_book.add_record(record1)

    
    address_book.add_record(record

    address_boo

    ad
# Знаходимо запис
    found_record = address_book.find(name=Record(name=
    found_record = address_book.find(name=Record(name=

    found_record = address_book.find(name=R

    found_record = address_book.

    found_record = ad

    found_
"John", value=""))
    
 
if found_record:
        
        
print(f"Знайдено запис: {found_record}")
    
   
else:
        
        

   
print("Запис не знайдено.")

    

   
# Видаляємо запис
    address_book.delete(name=Record(name=
    address_book.delete(name=Record(nam

    address_book.delete(nam

    address_book.dele

    address_bo

    add
"John", value=""))

    

  
# Перевіряємо, чи запис був видалений
    found_record = address_book.find(name=Record(name=
    found_record = address_book.find(name=Record(name

    found_record = address_book.find(name=Rec

    found_record = address_book.find(

    found_record = address_bo

    found_record = addr

    found_reco

    f
"John", value=""))
    
    
if found_record:
        
       
print(f"Знайдено запис: {found_record}")
    
 
else:
        
      
print("Запис не знайдено.")


# Видаляємо запис
    address_book.delete(name=Record(name=
    address_book.delete(name=Record(nam

    address_book.delete(nam

    address_book.dele

    address_bo

    add
"John", value=""))

    

  
# Перевіряємо, чи запис був видалений
    found_record = address_book.find(name=Record(name=
    found_record = address_book.find(name=Record(name

    found_record = address_book.find(name=Rec

    found_record = address_book.find(

    found_record = address_bo

    found_record = addr

    found_reco

    f
"John", value=""))
    
    
if found_record:
        
       
print(f"Знайдено запис: {found_record}")
    
 
else:
        
      
print("Запис не знайдено.")





# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)


    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john) 

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")
