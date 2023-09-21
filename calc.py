
def calc_pavel():


    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    def power(x, y):
        return x ** y

    def square_root(x):
        return x ** 0.5


    print("Выберите операцию.Пожалуйста")
    print("1.Сложить")
    print("2.Вычесть")
    print("3.Умножить")
    print("4.Разделить")
    print("5.Возвести в степень")
    print("6.Найти корень.")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4/5/6): ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == '5':
                print(num1, "**", num2, "=", power(num1, num2))

            elif choice == '6':
                print(num1, "**", "0.5", "=", square_root(num1))
