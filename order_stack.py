class OrderStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push_order(self, order):
        self.stack.append(order)
        print(f"Замовлення '{order}' додано до стеку.")

    def pop_order(self):
        if self.is_empty():
            print("Стек пустий. Немає замовлень для видалення.")
            raise IndexError("Стек порожній.")
        else:
            order = self.stack.pop()
            print(f"Замовлення '{order}' видалено зі стеку.")
            return order

    def peek_order(self):
        if self.is_empty():
            print("Стек пустий. Немає замовлень для перегляду.")
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def display_menu():
    print("\nМеню:")
    print("1. Додати замовлення")
    print("2. Видалити останнє замовлення")
    print("3. Переглянути останнє замовлення")
    print("4. Перевірити, чи порожній стек")
    print("5. Переглянути кількість замовлень")
    print("6. Вийти\n")


def main():
    orders = OrderStack()

    while True:
        display_menu()
        choice = input("Виберіть опцію (1-6): ")

        if choice == "1":
            order = input("Введіть назву замовлення: ")
            orders.push_order(order)

        elif choice == "2":
            try:
                orders.pop_order()
            except IndexError:
                pass

        elif choice == "3":
            order = orders.peek_order()
            if order:
                print(f"Останнє замовлення: {order}")

        elif choice == "4":
            if orders.is_empty():
                print("Стек порожній.")
            else:
                print("У стеці є замовлення.")

        elif choice == "5":
            print(f"Кількість замовлень: {orders.size()}")

        elif choice == "6":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
