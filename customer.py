# check password again
# work on verify_info


class Customer:

    def __init__(self, email):
        self.__first_name = ""
        self.__last_name = ""
        self.__age = 0
        self.__email = email
        self.__password = ""
        self.__card_number = ""
        self.__security_code = ""

    def input_age(self):
        self.__age = 0  # If I don't have this here, it will keep adding during an update
        age = (input('Enter age: '))
        while not age.isdigit() or int(age) < 0:
            print('Error!  Must be a non-negative number only!')
            age = (input('Enter age: '))
        self.__age += int(age)

    def input_password(self):

        lower_letters = (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w',
            'x', 'y', 'z')
        upper_letters = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W',
            'X', 'Y', 'Z')
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        upper_count = 0
        lower_count = 0
        num_count = 0

        self.__password = input('Enter a Password.  1 lower, 1 upper, 1 number:')

        for i in self.__password:
            if i in lower_letters:
                lower_count += 1
            elif i in upper_letters:
                upper_count += 1
            elif i in numbers:
                num_count += 1

        while len(self.__password) > 12 \
                or len(self.__password) < 8 \
                or lower_count < 1 \
                or upper_count < 1 \
                or num_count < 1:

            upper_count = 0
            lower_count = 0
            num_count = 0

            self.__password = ''
            self.__password = input('Try again (length error): ')

            for i in self.__password:
                if i in lower_letters:
                    lower_count += 1
                elif i in upper_letters:
                    upper_count += 1
                elif i in numbers:
                    num_count += 1

        print('PASSWORD ACCEPTED', self.__password)

    def input_card_number(self):
        card_num = input('Enter 16-digit only card number: ')
        while not card_num.isdigit() or len(card_num) > 16 or len(card_num) < 16:
            card_num = input('Input Error. Enter 16-digits exactly.')

        self.__card_number = card_num

    def input_security_code(self):
        sec_code = input('Enter 3-digit security code: ')
        while not sec_code.isdigit() or len(sec_code) > 3 or len(sec_code) < 3:
            sec_code = input('INPUT ERROR! TRY AGAIN: Enter 3-digit security code: ')

        self.__security_code = sec_code

    def input_info(self):
        self.__first_name = input('Enter first name: ')
        self.__last_name = input('Enter last name: ')
        Customer.input_age(self)
        Customer.input_password(self)
        Customer.input_card_number(self)
        Customer.input_security_code(self)

    def verify_info(self):

        choice = input(
            "To correct any entry, enter the entry's number and press RETURN. If everything is correct, press 0: "
        )

        while choice != '0':
            if choice == '1':
                self.__first_name = input('Enter new name:')
                while not self.__first_name.isalpha():
                    self.__first_name = input('Error! Enter new name: ')

            elif choice == '2':
                self.__last_name = input('Enter new last name: ')
                while not self.__last_name.isalpha():
                    self.__last_name = input('Error! Enter new last name: ')

            elif choice == '3':
                Customer.input_age(self)

            elif choice == '4':
                self.__email = input('Enter new Email: ')

            elif choice == '5':
                Customer.input_password(self)

            elif choice == '6':
                Customer.input_card_number(self)

            elif choice == '7':
                Customer.input_security_code(self)

            choice = input(
                "\nTo correct any entry, enter the entry's number and press RETURN. If everything is correct, press 0: "
            )

        print('REGISTRATION FINISHED')

    def output_info(self):
        return self.__first_name + ' ' + self.__last_name + ' ' + str(
            self.__age) + ' ' + self.__email + ' ' + self.__password + ' ' + self.__card_number + ' ' + self.__security_code + '\n'

    def __str__(self):
        return '\n1: First Name: ' + self.__first_name + ' ' \
                                                         '\n2: Last Name: ' + self.__last_name + ' ' \
                                                                                                 '\n3: Age: ' + str(
            self.__age) + \
               '\n4: Email: ' + self.__email + ' ' \
                                               '\n5: Password: ' + self.__password + ' ' \
                                                                                     '\n6: Card Number: ' + self.__card_number + ' ' \
                                                                                                                                 '\n7: Security Code: ' + self.__security_code

