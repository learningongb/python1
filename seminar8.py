from tabulate import tabulate

def bold_green(str):
    return "\033[1m\033[92m" + str +"\033[0m" 

def header_color(str):
    return "\033[95m" + str + "\033[0m"

def red(str):
    return "\033[91m" + str + "\033[0m" 

def show_menu():
    print("\nВыберите необходимое действие:",
          bold_green("1") + ". Отобразить весь справочник",
          bold_green("2") + ". Найти абонента по фамилии",
          bold_green("3") + ". Найти абонента по номеру телефона",
          bold_green("4") + ". Добавить абонента в справочник",
          bold_green("5") + ". Удалить абонента по номеру телефона",
          bold_green("6") + ". Изменить абонента по номеру телефона",
          bold_green("9") + ". Сохранить справочник в текстовом формате",
          bold_green("0") + ". Закончить работу",
          sep="\n")
    choice = int(input())
    return choice

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields(), line.strip().split(',')))
            data.append(record)
    return data

def write_phonebook(phone_book):
    write_csv('phonebook.csv', phone_book)

def fields():
    return ["Фамилия", "Имя", "Телефон", "Описание"]    

def get_file_name():
    return "phon.txt"

def write_txt(filename: str, data: list):
    write_csv(filename, data)

def headers_result():
    return [header_color("N")] + [header_color(x) for x in fields()]

def print_result(phone_book):
    print(tabulate(list(map(lambda x: [x[0] + 1] + [y for y in x[1].values()], list(enumerate(phone_book)))),
                   headers=headers_result(),
                   tablefmt="rounded_grid"))
    
def print_serch_result(search_result):
    print_result(search_result) if search_result else print(red("Абонент не найден"))

def get_search_name():
    return input("Введите фамилию\n").strip()

def get_search_number():
    return input("Введите номер телефона\n").strip()

def find_by_name(phone_book, name):
    return find_by_field(phone_book, "Фамилия", name)

def find_by_number(phone_book, number):
    return find_by_field(phone_book, "Телефон", number)

def find_by_field(phone_book, field, value):
    result = []
    for record in phone_book:
        if record[field].lower() == value.lower():
            result.append(record)
    return result

def find_index_by_number(phone_book, number):
    return find_index_by_field(phone_book, "Телефон", number)

def find_index_by_field(phone_book, field, value):
    for index in range(len(phone_book)):
        if phone_book[index][field].lower() == value.lower():
            return index
    return -1

def get_new_user():
    user = dict()
    for field in fields():
        user[field] = input(field + "\n")
    return user

def add_user(phone_book: list, user_data):
    phone_book.append(user_data)

def del_user(phone_book: list, index: int):
    if index < 0:
        print(red("Абонент не найден"))
        return False, phone_book
    return True, phone_book[:index] + phone_book[index + 1:]

def change_user(phone_book):
    index = find_index_by_number(phone_book, get_search_number())
    if index < 0:
        print(red("Абонент не найден"))
        return False, phone_book
    print("Введите новые данные абонента")
    return True, change_record(phone_book, index, get_new_user())

def change_record(phone_book, index, record):
    return phone_book[:index] + [record] +  phone_book[index + 1:]

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 0):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print_serch_result(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print_serch_result(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_phonebook(phone_book)
        elif choice == 5:
            number = get_search_number()
            modified, phone_book = del_user(phone_book, find_index_by_number(phone_book, number))
            if modified:
                write_phonebook(phone_book)
        elif choice == 6:
            modified, phone_book = change_user(phone_book)
            if modified:
                write_phonebook(phone_book)
        elif choice == 9:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

work_with_phonebook()