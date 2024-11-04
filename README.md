[![Python application](https://github.com/andrelcunha/myToDo_python_GTK4/actions/workflows/python-app.yml/badge.svg)](https://github.com/andrelcunha/myToDo_python_GTK4/actions/workflows/python-app.yml)
# My TO-DO App

A simple TO-DO application built with Python, GTK4, and Libadwaita, with both CLI and GUI interfaces for managing tasks.

## Features

- Add tasks with a single click.
- Mark tasks as completed.
- Delete tasks effortlessly.
- Clean, modern UI with custom CSS styling.
- Persist tasks using SQLite for reliable storage.

## Installation

### Prerequisites

- Python 3.8+ (Tested on Python 3.14.2)
- Pipenv

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app
    ```
2. Install dependencies:
   ```sh
    pipenv install
    pipenv shell
    ```
## Usage

### CLI

Run the command-line interface:
   ```sh
   python run_console.py
   ```
### GUI
Run the graphical interface:
   ```sh
   python run_gui.py
   ```
### Folder Structure
   ```
.
├── src/                # Source code
│   ├── tests/          # Unit tests for DbService
│   │   └── test_dbservice.py
│   ├── app/
│   │   ├── model/
│   │   │   └── task/
│   │   │       └── task.py
│   │   ├── gui/
│   │   │   ├── style.css
│   │   │   └── main.py
│   │   ├── dbservice/
│   │   │   └── dbservice.py
│   │   └── cli/
│   │       └── main.py
├── run_graphic.py      # Script to run the GUI
├── run_console.py      # Script to run the CLI
├── README.md           # This file
├── Pipfile             # Pipenv setup file
└── .gitignore          # Git ignore file
   ```
## Contributing
Feel free to fork this project and submit pull requests. Any contributions, suggestions, or improvements are welcome!
## License
This project is licensed under the MIT License.
