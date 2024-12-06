# Створюємо фунцію
def get_cats_info(path):
    try:
        # Відриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Пустий список для збереження інформації
            cats = []
            # Зчитуємо файл
            for line in file:
                # Видаляємо зайві пробіли і розділові знаки
                parts = line.strip().split(',')
                # Робимо три елементи
                if len(parts) == 3:
                    try:
                        cat_info = {
                            "id": parts[0],
                            "name": parts[1],
                            "age": int(parts[2]) # Перетворюємо вік у чисо
                        }
                        cats.append(cat_info) # Додаємо у пустий список cats

                    except ValueError:
                        print(f"Помилка: Вік кота не є числом у рядку '{line.strip()}'")

            return cats
    # помилки які можуть бути
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
# Приклад
cats_info = get_cats_info("cet.txt")
print(cats_info)
