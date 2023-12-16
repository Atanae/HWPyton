from alldefs import print_contacts, add_contact, find_contact, copy_contact

CONTACTS = 'contacts.txt'

def interface():
    while True:
        print('Выберете действие:\n' +
        '1 - Добавить контакт\n' +
        '2 - Вывести все контакты\n' +
        '3 - Найти контакт\n' +
        '4 - Копировать контакт\n' +
        '0 - Выйти')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                copy_contact(CONTACTS)    
            case _:
                print("Неверная команда!")


if __name__ == '__main__':
    interface()         
