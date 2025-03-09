#include <iostream>
#include <random>

class NumberGuessingGame {
private:
    int secretNumber;
    int attempts;

    int generateRandomNumber(int min, int max) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<int> dist(min, max);
        return dist(gen);
    }

public:
    NumberGuessingGame() : attempts(0) {
        secretNumber = generateRandomNumber(1, 100);
    }

    void start() {
        int guess;
        std::cout << "Try to guess the number between 1 and 100.\n";

        while (true) {
            std::cout << "Your guess: ";

            if (!(std::cin >> guess)) {
                std::cin.clear();
                std::cin.ignore(10000, '\n');
                std::cout << "Invalid input. Enter a valid number.\n";
                continue;
            }

            attempts++;

            if (guess < secretNumber) {
                std::cout << "Too low. Try again.\n";
            } else if (guess > secretNumber) {
                std::cout << "Too high. Try again.\n";
            } else {
                std::cout << "You got it in " << attempts << " attempts!\n";
                break;
            }
        }
    }
};

int main() {
    char choice;

    do {
        NumberGuessingGame game;
        game.start();

        std::cout << "Play again? (y/n): ";
        std::cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    std::cout << "Goodbye!\n";
    return 0;
}
