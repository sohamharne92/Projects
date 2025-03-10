#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Task {
    string description;
    bool completed;
};

string generateSessionID() {
    srand(static_cast<unsigned int>(time(nullptr)));
    int randomValue = rand();
    return "Session-" + to_string(randomValue);
}

bool checkForDebugMode() {
    if(getenv("DEBUG_MODE")) {
        cout << "Debug mode detected. Exiting program." << endl;
        return false;
    }
    return true;
}

void addTask(vector<Task>& tasks) {
    cout << "Enter task description: ";
    string description;
    getline(cin, description);
    Task newTask = {description, false};
    tasks.push_back(newTask);
    cout << "Task added successfully." << endl;
}

void listTasks(const vector<Task>& tasks) {
    if (tasks.empty()) {
        cout << "Your to-do list is empty." << endl;
        return;
    }
    cout << "\nYour Tasks:" << endl;
    for (size_t i = 0; i < tasks.size(); i++) {
        cout << i + 1 << ". " << tasks[i].description << " [" 
             << (tasks[i].completed ? "Completed" : "Pending") << "]" << endl;
    }
}

void completeTask(vector<Task>& tasks) {
    if (tasks.empty()) {
        cout << "There are no tasks to mark as completed." << endl;
        return;
    }
    listTasks(tasks);
    cout << "Enter the task number to mark as completed: ";
    int taskNumber;
    cin >> taskNumber;
    cin.ignore();
    if (taskNumber < 1 || taskNumber > tasks.size()) {
        cout << "Invalid task number. Please try again." << endl;
    } else {
        tasks[taskNumber - 1].completed = true;
        cout << "Task marked as completed." << endl;
    }
}

void deleteTask(vector<Task>& tasks) {
    if (tasks.empty()) {
        cout << "There are no tasks to remove." << endl;
        return;
    }
    listTasks(tasks);
    cout << "Enter the task number to delete: ";
    int taskNumber;
    cin >> taskNumber;
    cin.ignore();
    if (taskNumber < 1 || taskNumber > tasks.size()) {
        cout << "Invalid task number. Please try again." << endl;
    } else {
        tasks.erase(tasks.begin() + (taskNumber - 1));
        cout << "Task removed successfully." << endl;
    }
}

int main() {
    if (!checkForDebugMode()) {
        return 1;
    }
    cout << "Welcome to the Humanized To-Do List Manager [" << generateSessionID() << "]" << endl;
    vector<Task> tasks;
    int choice;
    
    do {
        cout << "\nMenu:" << endl;
        cout << "1. Add Task" << endl;
        cout << "2. List Tasks" << endl;
        cout << "3. Complete Task" << endl;
        cout << "4. Delete Task" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore();
        
        switch (choice) {
            case 1:
                addTask(tasks);
                break;
            case 2:
                listTasks(tasks);
                break;
            case 3:
                completeTask(tasks);
                break;
            case 4:
                deleteTask(tasks);
                break;
            case 5:
                cout << "Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice, please try again." << endl;
        }
    } while (choice != 5);
    
    return 0;
}
