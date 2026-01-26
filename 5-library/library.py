books: dict[str, str] = {"Белая Гвардия": "А.C.Пушкин", "15-летний Капитан": "Жуль Верн", "1984": "Джордж Оруэлл", "Тихий Дон" : "Михаил Шолохов", "Собачье Сердце" : "Михаил Булгаков", "Мастер и Маргарита" : "Михаил Булгаков"}
uniq_books = []
uniq_authors = set()
for book, author in books.items():
    uniq_books.append(book)
    uniq_authors.add(author)
print(f"Список всех книг: {uniq_books}")
print(f"Список уникальных авторов: {uniq_authors}")

