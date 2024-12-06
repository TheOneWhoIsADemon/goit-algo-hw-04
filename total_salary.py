# Створюємо функцію
def total_salary(path):
    try:
        # Вілкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Створюємо пустий список для зберігання зарплати
            salaries = []

            # Зчитужмо файт
            for line in file:
                # Видаляємо зайві пробіли та розділяємо рядокк на прізвище і зарплату
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        # Додаємо зарплату до списку та перетворюємо в число
                        salaries.append(float(parts[1]))
                    except ValueError:
                        print(f"Помилка в обробці рядка: {line.strip()} - зарплата не є числом.")

            # Преревіряємо чи є зарплата
            if not salaries:
                return (0, 0)

            # Розраховуємо загальну та середню зарплату
            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)


# Приклад
total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")