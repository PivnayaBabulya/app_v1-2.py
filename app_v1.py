books_issued = 0

while True:
    print("\nМеню:")
    print("1 — выдать одну книгу")
    print("2 — показать количество выданных книг")
    print("3 — сбросить счётчик до 0")
    print("0 — завершить работу")
    
    command = input("Введите команду: ")

    if command == "1":
        books_issued += 1
        print("Книга выдана. Теперь выдано книг: ", books_issued)
    elif command == "2":
        print("Выдано книг: ", books_issued)
    elif command == "3":
        books_issued = 0
        print("Счётчик сброшен. Выдано книг: ", books_issued)
    elif command == "0":
        print("Программа завершена.")
        break
    else:
        print("Неизвестная команда")