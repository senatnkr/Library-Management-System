from datetime import datetime #tarih ve saatle ilgili işlemleri yapmak için datetime modülü tanımlaması
import random #rastgele sayı üretmek için
class Library: #Library clası tanımlanması
    def __init__(self):
        self.file = open("book.txt", "a+", encoding="utf-8") # book.txt dosyasını a+ modunda ve türkçe karakter desteği ile açılması
        #self.file.write("Book,Author,Year, Page")
    def __del__(self):
        self.file.close()

    def addBook(self): #kitapların kullanıcıdan alınarak book.txt ekleneceği fonksiyon
            bookName = input("Book Namae : ")
            bookAuthorName = input("Author Name : ")
            while True:
             bookYear = input("Publication Year Of The Book : ")
             if not bookYear.isdigit():
                 print("Enter The Year Only As a Number ")
             elif len(bookYear) != 4:
                 print("You Entered The Date Wrong ")
             else:
                 year = datetime.now().year #kitabın basım yılı girilirken mevcut bulunan yılın kontrol edilmesi için year tanımlaması
                 if int(bookYear) > year:
                     print("You Cannot Enter Future Years ")
                 else:
                    break

            while True:
             bookPageNumber = input("Number Of Pages Of The Book : ")
             if not bookPageNumber.isdigit():
                 print("Enter Only As a Number.")
             else:
                 break
            self.file.write( bookName + " , " + bookAuthorName + "," + bookYear + "," + bookPageNumber + " \n")
            print("Book Added Successfully. Select The New Transaction You Want To Perform.")
    def listBooks(self): #book.txt içinde bulunan kitapların listelenmesi için fonksiyon
        self.file.seek(0)
        book = self.file.read().splitlines()
        if not book:
            print("There Are No Books İn The Library. Select The New Transaction You Want to Perform.")
        else:
            for libBook in book:
                listBook = libBook.split(",")
                print("Book Name : " + listBook[0] + "     Author : " + listBook[1])



    def deleteBook(self): #kitap.txt içinde bulunan kullanıcının belirttiği kitabın silinmesi için fonksiyon
        # Kitap silme
        bookName = input("Enter The Name Of The Book You Want To Delete: ")
        self.file.seek(0)
        updateBooks = [book for book in self.file.readlines()
                       if bookName.strip() != book.strip().split(",")[0].strip()]  # silinecek kitap isminin tam eşleşmesi için
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updateBooks)
        print("Book Deleted Successfully. Select The New Transaction You Want To Perform.")


    def adviceBook(self): #book.txt içinde bulunan kitaplardan rastgele bir kitap seçilerek önerilmesi için
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
           print("There Are No Books İn The Library. ")
        else:
            booksNum = len(books) #book.txt içinde bulunan kitapların sayısını al
            randomBookIndex = random.randint(0, booksNum-1) #random sayı seç
            randomBook = books[randomBookIndex].strip().split(",") #random seçilen kitabı yazdır
            print("Book Selected from the Library for You to Read : ", randomBook[0])


if __name__ == '__main__':

        lib = Library() # menü ile etkileşimli lib nesnesi
        while True:
            print("\n--- MENU ---")
            print("1. List Books ")
            print("2. Add Book ")
            print("3. Remove Book ")
            print("4. Exit ")
            print("A  Book Advice ")
            choice = input("Please Enter An Option (1-4 , A): ")
            if choice == "1":
                lib.listBooks()
            elif choice == "2":
                lib.addBook()
            elif choice == "3":
                lib.deleteBook()
            elif choice == "4":
                print("You Logged Out.")
                break
            elif choice == "A" or choice == "a":
                lib.adviceBook()
            else:
                print("Please Make a Valid Selection.")



