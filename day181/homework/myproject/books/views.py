from django.shortcuts import render
books_database = [
    {"id": 0, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 1, "title": "Animal Farm", "author": "George Orwell", "year": 1945},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"id": 5, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 6, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 7, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 8, "title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "year": 1998},
    {"id": 9, "title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003},
    {"id": 10, "title": "Angels & Demons", "author": "Dan Brown", "year": 2000},
    {"id": 11, "title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"id": 12, "title": "The Kite Runner", "author": "Khaled Hosseini", "year": 2003},
    {"id": 13, "title": "The Book Thief", "author": "Markus Zusak", "year": 2005},
    {"id": 14, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 15, "title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
    {"id": 16, "title": "The Chronicles of Narnia", "author": "C.S. Lewis", "year": 1950},
    {"id": 17, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 18, "title": "The Hunger Games", "author": "Suzanne Collins", "year": 2008},
    {"id": 19, "title": "The Fault in Our Stars", "author": "John Green", "year": 2012},
    {"id": 20, "title": "The Silent Patient", "author": "Alex Michaelides", "year": 2019},
]


# Create your views here.
def all_books(req):
    return render(req, 'index.html', {'books': books_database})

def book_detail(req, id):
    return render(req, 'book_detail.html', {'book': books_database[id]})