# DE_Expenses
This repository contains my solution to the DE first semester assesment.
This project aims to create a personal expense tracking application to assist individuals in managing and understanding their financial expenditures. 
This project contains two main files: the expenseDBClass.py and the main_file.py files. It utilizes two core classes: Expense and ExpenseDB, which are defined in the expenseDBClass.
Expense Class:
    Purpose: Models a single expense with relevant attributes.
    Attributes:
        id (UUID): Unique identifier
        title (string): Expense title
        amount (float): Expense amount
        created_at (timestamp): Creation time
        updated_at (timestamp): Last update time
    Methods:
        init: Initializes expense attributes.
        update: Modifies title and/or amount, updates updated_at.
        to_dict: Returns a dictionary representation of the expense.
        
ExpenseDB Class:
    Purpose: Manages a collection of Expense objects.
    Attributes:
        expenses (list): Stores Expense instances.
    Methods:
        init: Initializes the list.
        add_expense: Adds an expense to the database.
        remove_expense: Removes an expense by ID.
        get_expense_by_id: Retrieves an expense by its unique ID.
        get_expense_by_title: Retrieves expenses matching a given title.
        to_dict: Returns a list of dictionaries representing all expenses.

To create a copy of this project (Clone the project) and run the code on your computer, please follow the steps below:
1. Prerequisites: Ensure that you have git and python3 installed on your computer
2. Create a Github account if you do not have one yet
3. Click on the green "Code" button on the top-right of this page and copy the HTTPS link
4. On your computer, open your terminal and navigate to the directory where you want to clone this project
5. Initiate the clone by typing the following command: git clone , press ENTER to execute the command
6. Once finished, you'll have a new directory with the project's name
7. Navigate to this directory with the cd command
8. In this directory, run the command: python3 main_file.py
9. You will see some use cases of the Expense and expenseDB classes.
10. To test and create instances of the Expense and ExpenseDB classes, please write you code in the main_file.py file. This will ensure that you are abstracted from the implementation of the classes and prevents you from making any unwanted or accidental changes to the class definitions.

