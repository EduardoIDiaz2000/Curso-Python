class Book: # definición de la clase libro
    def __init__(self ,title ,author): # definicion del metodo constructor con los parametros (titulo, autor)
        self.title = title # asigna el parametro title al atributo de la instancia self.title
        self.author = author  # asigna el paramentro autor al atributo de la instancia self.author
        self.available = True # este atributo indica que el libro esta disponible desde el inicio   

    def borrow(self): # definición que el libro esta siendo prestado
        if self.available: # Verifica si el libro esta disponible 
            self.available = False # aqui da entender que el libro se presto y por eso es igual a falso
            print(f'El libro {self.title} ha sido prestado') #  Muestra que en efecto el libro ha sido prestado 

        else: # la otra opción en caso no este disponible 
            print(f'El libro {self.title} no se encuentra disponible') # Imprime que el libro no se encuentra disponible

    def return_book(self): # definición del retorno del libro 
        self.available = True # indica la disponibilidad del libro
        print(f'El libro {self.title} ha sido devuelto') # Imprime que el libro se ha devuelto


class User: # define la clase usuario
    def __init__(self, name, user_id): # defincion del metodo constructor con los paramentros (nombre, identificación del usuario)
        self.name = name # asigna el parametro name al atributo de la instancia self.name
        self.user_id = user_id # asigna el paramentro user.id al atributo de la instancia user.id
        self.borrowed_books = [] # inicializa el atributo libro prestado como una lista vacia, para almacenar los libros prestados por el usuario

    def borrow_book(self, book): # Se define la función libro prestado, y como parametro se tiene a book que es libro
        if book.available: # se pone la condicion if que si el libro se encuentra disponibles entonces:
            book.borrow() # si se encuentra disponible entonces llamara al metodo borrow
            self.borrowed_books.append(book) # y aqui se añade el libro a la lista borrowed_books de libros prestados

        else: # en caso esa condición no se cumpla se usa else para indicar lo siguiente:
            print(f'El libro {self.title}, no esta disponible') # Se imprime indicando como mensaje que el libro no esta disponible 
    
    def return_book(self, book): # Se define la función del retorno del libro, como parametro book, que es el libro
        if book in self.borrowed_books: # Se establece como condción que el libro se encuentra en la lista de borrowed_book, libros prestados
            book.return_book() # Si esta en la lista llamada al metodo return_book
            self.borrowed_books.remove(book) # Entonces lo elimina de la lista de borrowed_books

        else: # En caso no se cumpla esa condición, entonces else indicara lo siguiente.
            print(f'El libro {book.title} no esta en la lista de los prestados') # Se imprimira que el libro no esta en la lista de los libros prestados

class Library: # Se define la clase de biblioteca
    def __init__(self): # Llamado al metodo constructor
        self.books = [] # Se almacenara en un lista los libros de la biblioteca
        self.users = [] # Se almacenara e un lista los usuarios registrados en la biblioteca

    def add_book(self, book): # Define agrega libro como parametro libro
        self.books.append(book) # Añade un libro a la lista de books
        print(f'El libro {book.title}, ha sido agregado') # Y imprime que el libro ha sido agregado

    def register_user(self, user): # define el registro de usuario, como parametro usuario
        self.users.append(user) # añade un usuario a la lista de usuarios, users
        print(f'El usuario {user.name}, ha sido registrado') # Y imprime que el usuario ha sido agregado

    def show_available_books(self): # Define los libros disponibles
        print('Libros disponibles') # Imprime un encabezado a la lista de libros disponibles 
        for book in self.books: # Rcorre cada libro dentro de la lista de libros de la biblioteca
            print(f'{book.title} por {book.author}') # Imprime el titulo del libro con su autor

book1 = Book('El principito', 'Antoine de Saint-Exupéry') # Se crea primera instancia del libro, titulo y autor
book2 = Book('1984', 'George Orwell') # Se crea la segundo isntancia del libro, titulo y autor

# Crear usuario
user1 = User('Eduardo', '001') # Se crea la usuario 1 con su nombre y identificación de usuario

# Crear biblioteca
library = Library() # Se crea una isntancia llamada library o biblioteca
library.add_book(book1) # Se añede el libro uno a la biblioteca
library.add_book(book2) # Se añade el libro dos a la biblioteca
library.register_user(user1) # Se registra el usuario 1 a la biblioteca

# Mostrar libreria
library.show_available_books() # Muestra los libros disponibles

# Realizar prestamo
user1.borrow_book(book1) # Se realiza el prestamo del libro 1

# Mostrar libreria
library.show_available_books() # Se muestra los libros disponibles

# Devolver libro
user1.return_book(book1) # El usuario retorna el libro prestado 1

# Mostrar libreria
library.show_available_books() # Se muestra los libros disponibles