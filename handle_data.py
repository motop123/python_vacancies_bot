def handle_vacancoes(data):
    lst = []
    for item in data:
        s = f"id {item['id']}\n "\
            f"Вакансия {item['name']}\n " \
            f"{item['published_at']}\n" \
            f"{item['url']}"
        lst.append(s)
    return lst
