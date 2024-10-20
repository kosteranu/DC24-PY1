# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44 * 1024 * 1024
letter = 4
num_of_letters = 25
num_of_strings = 50
num_of_pages = 100
book_size = letter * num_of_letters * num_of_strings * num_of_pages
number_of_books = int(memory // book_size)

print("Количество книг, помещающихся на дискету:", number_of_books)
