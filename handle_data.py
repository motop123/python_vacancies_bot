def handle_vacancoes(data):
    lst = []
    for item in data:
        s = f"Вакансия {item['name']}\n " \
            f"{item['published_at']}\n" \
            f"{item['url']}"
        lst.append(s)
    return lst
