def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []

            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 3:
                    try:
                        cat_info = {
                            "id": parts[0],
                            "name": parts[1],
                            "age": int(parts[2])
                        }
                        cats.append(cat_info)

                    except ValueError:
                        print(f"Помилка: Вік кота не є числом у рядку '{line.strip()}'")

            return cats

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

cats_info = get_cats_info("cet.txt")
print(cats_info)
