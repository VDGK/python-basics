import sys

books: dict[str, str] = {"Белая Гвардия": "Михаил Булгаков", "15-летний Капитан": "Жуль Верн", "1984": "Джордж Оруэлл", "Тихий Дон" : "Михаил Шолохов", "Собачье Сердце" : "Михаил Булгаков", "Мастер и Маргарита" : "Михаил Булгаков"}


if sys.argv[1] == "filter":
    target_author = sys.argv[2]
    filtered_books = {title: author for title, author in books.items() if author == target_author}
    print(list(map(lambda item: f"{item[0]} - {item[1]}" , filtered_books.items())))

if sys.argv[1] == "sort":
    sorted_books = list(map(lambda item: f"{item[0]} - {item[1]}" , books.items()))
    if sys.argv[2] == "book":
        print(list(sorted(sorted_books, key=lambda item: item[0])))
    if sys.argv[2] == "author":
        print(list(sorted(sorted_books, key=lambda item: item[1])))