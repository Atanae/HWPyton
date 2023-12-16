
CONTACTS_COPY = 'contacts_copy.txt'

def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            i = 0
            for line in all_cont:
                i += 1
                print(str(i)+'. '+line.strip(), end='\n\n')
        else:
            print('Список контактов пустой')

def copy_contact(file_name):
    print_contacts(file_name)
    print()
    print('Выберите номер контакта для копирования')
    num = int(input())
    with open(file_name,'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) >= num :
            i = 0
            for cont in all_cont:
                if (i == num - 1):
                    with open(CONTACTS_COPY,'a', encoding='utf8') as file: 
                        file.write(cont) 
                    print(cont,'\nКонтакт скопирован\n')
                    return   
                i +=1
        else:
            print('Нет контакта с таким номером\n')

def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info


def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        new_cont = connect_with_user()
        all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)


def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

        print("Выберите критерий для поиска:\n" +
        '1 - Имя\n' +
        '2 - Фамилия\n' +
        '3 - Телефон\n'
        )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
    if data in cont_as_list[comm - 1]:
        print(*cont_as_list)   


        