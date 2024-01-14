from AddressBook import *


class Command:
    """
    The base class for all command classes.

    Attributes:
        None

    Methods:
        execute(bot): 
            Abstract method to be implemented by subclasses. Executes the command with the given bot instance.
    """    
    def execute(self, bot):
        pass


class AddCommand(Command):
    """
    A command class for adding a record to the address book.

    Attributes:
        None

    Methods:
        execute(bot): 
            Adds a new record to the address book using user input.
    """    
    def execute(self, bot):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        bot.book.add(record)


class SearchCommand(Command):
    """
    A command class for searching records in the address book.

    Attributes:
        None

    Methods:
        execute(bot): 
            Searches for records in the address book based on user input for category and pattern.
    """    
    def execute(self, bot):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = bot.book.search(pattern, category)
        birth = ''
        print('This is SearchBot()')
        print(result)
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
            result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
            print(result)


class EditCommand(Command):
    """
    A command class for editing a specific parameter of a contact in the address book.

    Attributes:
        None

    Methods:
        execute(bot): 
            Edits a specified parameter of a contact in the address book based on user input.
    """
    def execute(self, bot):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        bot.book.edit(contact_name, parameter, new_value)


class RemoveCommand(Command):
    """
    A command class for removing a record from the address book.

    Attributes:
        None

    Methods:
        execute(bot): 
            Removes a record from the address book based on user input for the contact name or phone number.
    """
    def execute(self, bot):
        pattern = input("Remove (contact name or phone): ")
        bot.book.remove(pattern)


class SaveCommand(Command):
    """
    A command class for saving the address book to a file.

    Attributes:
        None

    Methods:
        execute(bot): 
            Saves the current state of the address book to a specified file.
    """
    def execute(self, bot):
        file_name = input("File name: ")
        bot.book.save(file_name)


class LoadCommand(Command):
    """
    A command class for loading the address book from a file.

    Attributes:
        None

    Methods:
        execute(bot): 
            Loads the address book with data from a specified file.
    """
    def execute(self, bot):
        file_name = input("File name: ")
        bot.book.load(file_name)


class CongratulateCommand(Command):
    """
    A command class for printing a congratulatory message based on the address book data.

    Attributes:
        None

    Methods:
        execute(bot): 
            Prints a congratulatory message based on the current state of the address book.
    """
    def execute(self, bot):
        print(bot.book.congratulate())


class ViewCommand(Command):
    """
    A command class for printing the entire address book.

    Attributes:
        None

    Methods:
        execute(bot): 
            Prints the entire content of the address book.
    """
    def execute(self, bot):
        print(bot.book)


class ExitCommand(Command):
    """
    A command class for exiting the program.

    Attributes:
        None

    Methods:
        execute(bot): 
            Exits the program.
    """
    def execute(self, bot):
        pass


class Bot:
    """
    A class representing a bot that interacts with an address book using various commands.

    Attributes:
        book (AddressBook): 
            An instance of the AddressBook class to store contact information.
        commands (dict): 
            A dictionary mapping command names to their corresponding Command class instances.

    Methods:
        handle(action): 
            Executes the specified command action using the corresponding Command class.
    """
    def __init__(self):
        self.book = AddressBook()
        self.commands = {
            'add': AddCommand(),
            'search': SearchCommand(),
            'edit': EditCommand(),
            'remove': RemoveCommand(),
            'save': SaveCommand(),
            'load': LoadCommand(),
            'congratulate': CongratulateCommand(),
            'view': ViewCommand(),
            'exit': ExitCommand(),
        }

    def handle(self, action):
        if action in self.commands:
            self.commands[action].execute(self)
        else:
            print("There is no such command!")
