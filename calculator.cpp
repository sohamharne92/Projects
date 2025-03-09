#include <iostream>
#include <limits>
using namespace std;

double compute(double a, double b, char op) {
    double result = 0;
    switch (op) {
        case '+': result = a + b; break;
        case '-': result = a - b; break;
        case '*': result = a * b; break;
        case '/': result = (b != 0) ? a / b : throw runtime_error("Error: Cannot divide by zero");
        default: throw invalid_argument("Unknown operation");
    }
    return result;
}

void flushInput() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

int main() {
    int c = 0;
    while (++c) {
        cout << "\n[ Calculator ] Choose an operation:\n";
        cout << "(1) Add\n(2) Subtract\n(3) Multiply\n(4) Divide\n(5) Quit\n";
        cout << "Select: ";
        
        int selection;
        cin >> selection;
        
        if (cin.fail()) {
            cout << "Oops! Invalid input, try again.\n";
            flushInput();
            continue;
        }
        
        if (selection == 5) {
            cout << "Session ended. Goodbye!" << endl;
            break;
        }
        
        double x, y;
        cout << "Enter first number: ";
        cin >> x;
        cout << "Enter second number: ";
        cin >> y;
        
        char ops[] = {'+', '-', '*', '/'};
        try {
            if (selection >= 1 && selection <= 4) {
                cout << "Result: " << compute(x, y, ops[selection - 1]) << endl;
            } else {
                cout << "Invalid choice! Try again." << endl;
            }
        } catch (const exception &ex) {
            cout << ex.what() << endl;
        }
    }
    return 0;
}
