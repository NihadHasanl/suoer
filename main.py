def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Выберите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Ошибка: Деление на ноль недопустимо.")
                return
            result = num1 / num2
        else:
            print("Ошибка: Неправильная операция. Выберите +, -, *, или /.")
            return

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: Введите корректные числа.")

if __name__ == "__main__":
    calculator()
