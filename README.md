# Coding Journal

The Coding Journal is a Python-based application that allows users to create, manage, and edit personal coding journals stored in a MySQL database. This application is designed to help you keep track of your daily coding activities, including errors, collaborators, tasks, and additional comments.

## Features

- **Journal Creation**: Easily create new journals by specifying a unique name.
- **Entry Management**: Add entries to your journal with details like descriptions, errors encountered, collaborators, to-do tasks, and additional comments.
- **Entry Modification**: Modify existing entries by editing descriptions, errors, collaborators, tasks, and dates.
- **Data Retrieval**: Search and retrieve journal entries based on specific dates.
- **Spell Check**: Integrated grammar and spelling correction using the `Grammer` module.
- **Interactive CLI**: User-friendly command-line interface to navigate and manage your journals.

## Data Structures and Algorithms

### 1. **MySQL Database**
   - **Data Structure**: Relational Database
   - **Usage**: The journal entries are stored in a MySQL database, where each entry is represented as a row in a table. The database schema includes columns for description, errors, collaborators, to-do tasks, additional comments, and the date. This relational model allows for efficient querying, modification, and retrieval of entries based on various criteria.

![image](https://github.com/user-attachments/assets/eab5ad96-204d-4a61-9c4f-824df4b93327)


### 2. **Dictionary**
   - **Data Structure**: Python Dictionary
   - **Usage**: The `extract` function retrieves journal entries from the database and stores them in a Python dictionary. This structure allows for easy access to each field of a journal entry by using keys (e.g., 'description', 'errors', 'buddy'). The dictionary's O(1) average-time complexity for lookups makes it an ideal choice for handling entry data.

![image](https://github.com/user-attachments/assets/721d15f8-e53b-431b-b933-b9950eff2e93)


### 3. **Conditional Statements**
   - **Algorithm**: Conditional Logic
   - **Usage**: The program uses conditional statements extensively to handle different user inputs and actions. For instance, when modifying a journal entry, conditional logic determines which field (description, errors, etc.) needs to be updated. This ensures that the correct SQL update command is generated and executed.

![image](https://github.com/user-attachments/assets/f9ae2ba4-6203-4577-92c2-2fb103403553)

### 4. **Input Validation**
   - **Algorithm**: Input Validation
   - **Usage**: The application checks user inputs to ensure they are valid before processing. For example, when selecting a journal or date, the program validates the input to prevent SQL errors and to ensure the journal or date exists in the database. This reduces the chances of runtime errors and enhances the user experience.

![image](https://github.com/user-attachments/assets/478d0bcb-ffc4-4712-9349-63a64ff8015d)


### 5. **Parameterization in SQL Queries**
   - **Algorithm**: SQL Query Parameterization
   - **Usage**: To prevent SQL injection attacks, the application uses parameterized SQL queries. By passing user input as parameters rather than interpolating them directly into the SQL string, the application ensures that the database interactions are secure.

![image](https://github.com/user-attachments/assets/144a4488-6ce8-4ad6-8bf1-6608553251a6)

### 6. **Spell Checking and Grammar Correction**
   - **Algorithm**: Spell Check and Grammar Correction
   - **Usage**: The `Grammer` module is used to automatically correct spelling and grammar errors in the journal entries. This is an important feature for maintaining the quality and readability of journal entries, ensuring that they are consistent and error-free.

![image](https://github.com/user-attachments/assets/88c3fbef-44e3-4982-9484-24e0dffa1394)


## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/coding-journal.git
    cd coding-journal
    ```

2. **Install the required Python packages:**

    ```bash
    pip install mysql-connector-python
    ```

3. **Set up the MySQL database:**

    - Ensure MySQL is running on your machine.
    - Create a MySQL user with the appropriate privileges.
    - Update the `host`, `user`, and `password` parameters in `codingjournal.py` to match your MySQL setup.

## Usage

1. **Run the Coding Journal application:**

    ```bash
    python codingjournal.py
    ```

2. **Choose an option:**

    - Press `1` to access a previous journal.
    - Press `2` to create a new journal.

3. **Manage entries:**

    - Press `1` to make new entries.
    - Press `2` to make changes to existing entries.
    - Press `3` to find an entry by date.
    - Press `4` to quit the application.

## Modules

- **codingjournal.py**: The main application file that handles user interaction and journal management.
- **Grammer.py**: A module responsible for grammar and spelling corrections.
- **Newjournal.py**: Handles the creation and insertion of new journal entries.
- **questions.py**: Contains prompts and questions for journal entries.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. 
