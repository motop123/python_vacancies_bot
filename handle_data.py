def handle_vacancies(data):
    lst = []
    for item in data:
        s = f"id {item['id']}\n "\
            f"Вакансия {item['name']}\n " \
            f"{item['published_at']}\n" \
            f"{item['alternate_url']}"

        lst.append(s)
    return lst
