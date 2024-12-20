class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def display_info(self):
        print(f'title:{self.title},author:{self.author},year:{self.year}')

        
book1=Book('python crash course' ,'eric mattesh',1949)
book1.display_info()


class Library:
    library_name="central library"
    def __init__(self):
        self.books=[]
        
        
    def add_book(self,book):
        self.books.append(book)

        
    def show_books(self):
        print(f'books in {Library.library_name}')
        for book in self.books:
            book.display_info()

            
    def find_book(self,title):
        for book in self.books:
            if book.title==title:
             print('found the book')
             book.display_info()
             return
        print(f'the book:{title}  not found')


    def remove_book(self,title):
        for book in self.books:
            if book.title==title:
                self.books.remove(book)
                print(f"the book {title} has been removed")
                return
            print(f'the book:{title}  not found')

            
            
library=Library()
book1=Book('python crash course' ,'eric mattesh',1949)
book2=Book('to kill mockingbird' ,'harper lee',1960)
library.add_book(book1)
library.add_book(book2)
library.show_books()

library.find_book("1984")
library.remove_book('python crash course' )
library.show_books()

