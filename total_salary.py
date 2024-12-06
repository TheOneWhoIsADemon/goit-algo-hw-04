def total_salary(path):
    try:

        with open(path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:

                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:

                        salaries.append(float(parts[1]))
                    except ValueError:
                        print(f"Помилка в обробці рядка: {line.strip()} - зарплата не є числом.")


            if not salaries:
                return (0, 0)


            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)



total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")