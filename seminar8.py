from tabulate import tabulate

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
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
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def get_file_name():
    return "phon.txt"

def write_txt(filename: str, data: list):
    write_csv(filename, data)

def print_result(phone_book):
    print(tabulate(list(map(lambda x: [x[0] + 1] + [y for y in x[1].values()], list(enumerate(phone_book)))),
                   headers=["N", "Фамилия", "Имя", "Телефон", "Описание"],
                   tablefmt="rounded_grid"))
    
def print_serch_result(search_result):
    print_result(search_result) if search_result else print("Абонент не найден")

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

def get_new_user():
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    user = dict()
    for field in fields:
        user[field] = input(field + "\n")
    return user

def add_user(phone_book: list, user_data):
    phone_book.append(user_data)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 6):
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
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

work_with_phonebook()