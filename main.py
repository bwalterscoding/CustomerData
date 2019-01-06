from customer import Customer


def main():

    email1 = get_email1()
    customer1 = Customer(email1)
    customer1.input_info()
    email2 = get_email2()
    customer2 = Customer(email2)
    customer2.input_info()

    run_verify = input('Would you like to verify Customer Info? [any button for YES or [n] for NO] ')
    run_verify = run_verify.upper()

    while run_verify != 'N':
        which_customer = input('Which customer? 1 or 2: ')
        if which_customer == '1':
            print('\nPlease verify Customer 1', customer1)
            customer1.verify_info()
        elif which_customer == '2':
            print('\nPlease verify Customer 2', customer2)
            customer2.verify_info()

        run_verify = input('Would you like to verify Customer Info? [y/n]')
        run_verify = run_verify.upper()

    print('\nUPDATED INFO CUSTOMER 1:', customer1)
    print('\nUPDATED INFO CUSTOMER 2:', customer2)

    write_to_text(customer1, customer2)


def get_email1():

    # Enter email address for 2 customers

    email = input("Enter Customer 1 email: ")

    return email


def get_email2():
    # Enter email address for 2 customers
    email = input("\nEnter Customer 2 email: ")

    return email


def write_to_text(c1, c2):
    output_file = open('Customer Info.txt', 'w')
    output_file.write('Customer Data\n')
    output_file.write('-------------------------------------\n\n')
    output_file.write(c1.output_info())
    output_file.write(c2.output_info())


main()
