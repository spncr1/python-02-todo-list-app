# TODO LIST APPLICATION

A simple command-line Todo List app written in Python.  
This application allows you to add, remove, view, and clear tasks from your todo list interactively.

---

## Features

- **Add tasks** to your todo list.
- **Remove tasks** by selecting their index.
- **Clear the entire todo list.**
- **View all current tasks** with numbering.
- **Graceful exit** from the application.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Application

1. Save the code to a file, e.g. `todo.py`.
2. Run the file in your terminal:
   ```sh
   python todo.py
   ```

---

## Usage

When you run the application, you'll see a menu:

```
--- TODO LIST APPLICATION ---

1. Add a task
2. Remove a task
3. Clear Todo List
4. View Tasks
5. Quit Application
Select an option:
```

**Options:**
- **Add a task:**  
  Enter the description for your new task.

- **Remove a task:**  
  Enter the number associated with the task you wish to remove (as shown in the "View Tasks" option).

- **Clear Todo List:**  
  Clears all tasks from your list.

- **View Tasks:**  
  Shows a numbered list of all tasks currently in your todo list.

- **Quit Application:**  
  Exits the program.

---

## How the Core Logic Works

### 1. Main Loop & Menu

The application uses a `while True:` loop, repeatedly showing the menu until you choose to quit.

### 2. Adding a Task

- Prompts for input.
- Appends task description to `todo_list` (a Python list).

### 3. Removing a Task

- Prompts for the index of the task to remove.
- Uses `pop(index)` to remove the task at the specified position.
- **Note:**  
  The code expects you to enter the index as shown in the "View Tasks" menu.

### 4. Clearing the Todo List

- Uses the `clear()` method to remove all items from the list.

### 5. Viewing Tasks

- Uses `enumerate(todo_list, start=0)` to display tasks with their corresponding indices.
- Each task is shown in the format:  
  `0. Buy groceries`  
  `1. Walk the dog`

---

## Code Explanation

- **`todo_list = []`**  
  Initializes an empty list to hold your tasks.

- **Adding tasks**  
  ```python
  task = input("What task would like to add to your todo list? ")
  todo_list.append(task)
  ```

- **Removing tasks**  
  ```python
  remove_task = int(input("Which task would you like to remove? "))
  if remove_task > 0 & remove_task < len(todo_list):
      todo_list.pop(remove_task)
  else:
      print("That task number doesn't exist on your todo list.")
  ```
  - You should use `0 <= remove_task < len(todo_list)` for proper bounds checking.
  - The `pop(index)` method removes the task at the given index.

- **Viewing tasks**  
  ```python
  for i, task in enumerate(todo_list, start=0):
      print(f"{i}. {task}")
  ```
  - `enumerate()` provides both the index (`i`) and the task (`task`).

---

## Known Issues & Improvements

- The bounds check for removing tasks should use `0 <= remove_task < len(todo_list)` instead of `> 0 &`.
- The removal confirmation prints the index, not the task name.
- Input validation can be improved to handle non-integer input.
- Starting the task numbering from `0` may be less intuitive for users; consider starting from `1` and adjusting indices accordingly.

---

## Example Run

```
--- TODO LIST APPLICATION ---

1. Add a task
2. Remove a task
3. Clear Todo List
4. View Tasks
5. Quit Application
Select an option: 1

--- ADD A TASK ---
What task would like to add to your todo list? Buy milk
Buy milk was successfully added.
------------------

Select an option: 4

--- YOUR TODO LIST ---
0. Buy milk
----------------------

Select an option: 2

--- REMOVE A TASK ---
Which task would you like to remove? 0
0 was successfully removed.
---------------------
```

---

## License

This project is open source and free to use.

---