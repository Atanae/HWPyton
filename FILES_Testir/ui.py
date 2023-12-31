from logger import *

def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '0':
        print(
        'Возможные варианты действия:\n'
        '1. Добавить контакт\n'
        '2. Вывод списка контактов\n'
        '3. Поиск контакта\n'
        '4. Копировать контакт\n'
        '0. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '0'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()    
                pass
            case '0':
                break