import timeit
from main import Zoo, Employee, Animal, Mammal, Bird, Reptile

# Создаем экземпляр зоопарка для проверки времени выполнения операций
my_zoo = Zoo("Зоопарк имени Ивана Ивановича")

# Функция для линейной сложности O(n)
def linear_complexity(n):
    start_time = timeit.default_timer()
    for i in range(n):
        pass  # Простая операция
    end_time = timeit.default_timer()
    print(f"Линейная сложность O(n) для n={n}: {end_time - start_time:.8f} секунд")

# Функция для логарифмической сложности O(log n)
def logarithmic_complexity(n):
    start_time = timeit.default_timer()
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    end_time = timeit.default_timer()
    print(f"Логарифмическая сложность O(log n) для n={steps} (шагов): {end_time - start_time:.8f} секунд")

# Функция для константной сложности O(1)
def constant_complexity():
    start_time = timeit.default_timer()
    result = 42  # Простая операция, не зависящая от входных данных
    end_time = timeit.default_timer()
    print(f"Константная сложность O(1): {end_time - start_time:.8f} секунд")

# Функции для проверки сложности методов Zoo
def check_load_employees():
    load_time = timeit.timeit(my_zoo.load_employees, number=1)
    print(f"Время работы загрузки сотрудников: {load_time:.6f} секунд")

def check_add_animal():
    animal = Mammal("Лев", 5, "Золотистый")
    add_animal_time = timeit.timeit(lambda: my_zoo.add_animal(animal), number=1)
    print(f"Время добавления животного в зоопарк: {add_animal_time:.6f} секунд")

def check_add_employee():
    employee = Employee("Иван Иванович", 10, "Дрессировщик")
    add_employee_time = timeit.timeit(lambda: my_zoo.add_employee(employee), number=1)
    print(f"Время добавления сотрудника в зоопарк: {add_employee_time:.6f} секунд")

def check_list_animals():
    list_animals_time = timeit.timeit(my_zoo.list_animals, number=1)
    print(f"Время отображения списка животных: {list_animals_time:.6f} секунд")

def check_list_employees():
    list_employees_time = timeit.timeit(my_zoo.list_employees, number=1)
    print(f"Время отображения списка сотрудников: {list_employees_time:.6f} секунд")

# Запуск всех тестов
if __name__ == "__main__":
    print("Тест сложности алгоритмов:")
    check_load_employees()
    check_add_animal()
    check_add_employee()
    check_list_animals()
    check_list_employees()

    print("\nОценка временной сложности:")
    # Пример значения n для линейной и логарифмической оценки
    n_linear = 10**6
    linear_complexity(n_linear)

    n_logarithmic = 10**6
    logarithmic_complexity(n_logarithmic)

    # Оценка константной сложности
    constant_complexity()


