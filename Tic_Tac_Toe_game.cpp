#include <iostream>
#include <array>
using namespace std;

class TicTacToe {
private:
    array<array<char, 3>, 3> board;
    char currentPlayer;

public:
    TicTacToe() { resetGame(); }

    void resetGame() {
        for (auto& row : board) {
            row.fill(' ');
        }
        currentPlayer = 'X';
    }

    void displayBoard() const {
        cout << "\n";
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                cout << board[i][j];
                if (j < 2) cout << " | ";
            }
            cout << "\n";
            if (i < 2) cout << "---------\n";
        }
        cout << "\n";
    }

    bool makeMove(int row, int col) {
        if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
            cout << "Invalid move. Try again.\n";
            return false;
        }
        board[row][col] = currentPlayer;
        return true;
    }

    bool checkWin() const {
        for (int i = 0; i < 3; ++i) {
            if (board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) return true;
            if (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer) return true;
        }
        if (board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) return true;
        if (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) return true;
        return false;
    }

    bool isDraw() const {
        for (const auto& row : board) {
            for (char cell : row) {
                if (cell == ' ') return false;
            }
        }
        return true;
    }

    void switchPlayer() { currentPlayer = (currentPlayer == 'X') ? 'O' : 'X'; }

    void playGame() {
        while (true) {
            resetGame();
            while (true) {
                displayBoard();
                int row, col;
                cout << "Player " << currentPlayer << ", enter row and column (0-2): ";
                cin >> row >> col;
                if (!makeMove(row, col)) continue;
                if (checkWin()) {
                    displayBoard();
                    cout << "Player " << currentPlayer << " wins!\n";
                    break;
                }
                if (isDraw()) {
                    displayBoard();
                    cout << "It's a draw!\n";
                    break;
                }
                switchPlayer();
            }
            char playAgain;
            cout << "Do you want to play again? (y/n): ";
            cin >> playAgain;
            if (playAgain != 'y' && playAgain != 'Y') break;
        }
    }
};

int main() {
    TicTacToe game;
    game.playGame();
    return 0;
}
