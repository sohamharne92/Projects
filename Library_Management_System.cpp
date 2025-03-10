#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <ctime>
using namespace std;

class Book {
public:
    string title;
    string author;
    string ISBN;
    bool available;

    Book(string t, string a, string i) : title(t), author(a), ISBN(i), available(true) {}
};

class Borrower {
public:
    string name;
    int id;
    unordered_map<string, time_t> borrowedBooks;
    
    Borrower(string n, int i) : name(n), id(i) {}
};

class Library {
private:
    vector<Book> bookCollection;
    unordered_map<int, Borrower> borrowerRecords;
    const double finePerDay = 2.0;

public:
    void addBook(string title, string author, string ISBN) {
        bookCollection.emplace_back(title, author, ISBN);
    }
    
    void searchBook(const string &query) {
        bool found = false;
        for (const auto &book : bookCollection) {
            if (book.title.find(query) != string::npos || book.author.find(query) != string::npos || book.ISBN == query) {
                cout << "Book: " << book.title << " | Author: " << book.author << " | ISBN: " << book.ISBN;
                cout << (book.available ? " | Available\n" : " | Checked Out\n");
                found = true;
            }
        }
        if (!found) cout << "No matching books found.\n";
    }
    
    void addBorrower(string name, int id) {
        borrowerRecords.emplace(id, Borrower(name, id));
    }
    
    void checkoutBook(int borrowerID, const string &ISBN) {
        for (auto &book : bookCollection) {
            if (book.ISBN == ISBN && book.available) {
                book.available = false;
                borrowerRecords[borrowerID].borrowedBooks[ISBN] = time(0);
                cout << "Book successfully checked out.\n";
                return;
            }
        }
        cout << "Sorry, this book is not available.\n";
    }
    
    void returnBook(int borrowerID, const string &ISBN) {
        if (borrowerRecords.find(borrowerID) != borrowerRecords.end()) {
            auto &borrowed = borrowerRecords[borrowerID].borrowedBooks;
            if (borrowed.find(ISBN) != borrowed.end()) {
                time_t borrowedTime = borrowed[ISBN];
                time_t currentTime = time(0);
                int daysElapsed = (currentTime - borrowedTime) / (60 * 60 * 24);
                double fineAmount = (daysElapsed > 14) ? (daysElapsed - 14) * finePerDay : 0.0;
                
                for (auto &book : bookCollection) {
                    if (book.ISBN == ISBN) {
                        book.available = true;
                        break;
                    }
                }
                borrowed.erase(ISBN);
                cout << "Book returned successfully. Fine: Rs. " << fineAmount << "\n";
                return;
            }
        }
        cout << "Invalid return attempt.\n";
    }
};

int main() {
    Library librarySystem;
    librarySystem.addBook("Programming with C++", "Bjarne Stroustrup", "111222333");
    librarySystem.addBook("Data Science Essentials", "Hadley Wickham", "444555666");
    
    librarySystem.addBorrower("John Doe", 1);
    librarySystem.addBorrower("Jane Smith", 2);
    
    int choice;
    while (true) {
        cout << "\nLibrary Management System\n";
        cout << "1. Search Book\n2. Checkout Book\n3. Return Book\n4. Exit\nChoice: ";
        cin >> choice;
        if (choice == 1) {
            string searchQuery;
            cout << "Enter book title, author, or ISBN: ";
            cin.ignore();
            getline(cin, searchQuery);
            librarySystem.searchBook(searchQuery);
        } else if (choice == 2) {
            int userId;
            string ISBN;
            cout << "Enter Borrower ID and Book ISBN: ";
            cin >> userId >> ISBN;
            librarySystem.checkoutBook(userId, ISBN);
        } else if (choice == 3) {
            int userId;
            string ISBN;
            cout << "Enter Borrower ID and Book ISBN: ";
            cin >> userId >> ISBN;
            librarySystem.returnBook(userId, ISBN);
        } else if (choice == 4) {
            cout << "Exiting...\n";
            break;
        } else {
            cout << "Invalid selection, please try again.\n";
        }
    }
    return 0;
}
