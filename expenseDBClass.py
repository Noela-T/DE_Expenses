"""Implementing object-oriented programming concepts"""
import uuid
from datetime import datetime, timezone

class Expense:
    """Represents an individual financial expense"""
    def __init__(self,title,amount):
        """initializing attributes of the class"""
        self.id = uuid.uuid4().hex #unique identifier generated as a UUID string
        self.title = title #string representing the title of the expense
        self.amount = amount #float represnting the amount of the expense
        self.created_at = datetime.utcnow() #timestamp indicating when the expense was created (UTC)
        self.updated_at = datetime.utcnow() #timestamp indicating the last time the expense was updated (UTC)

    @property 
    def title(self):
        """gets the instance title attribute"""
        return self._title
    @title.setter #validate that we receive proper values for expense title
    def title(self,given_value):
        if isinstance(given_value, str):
            self._title = given_value
        else:
            raise TypeError("Please enter a valid string for Expense title.")
        

    @property 
    def amount(self):
        """gets the instance amount attribute"""
        return self._amount
    @amount.setter #validate that we receive positive numbers for expense amount
    def amount(self,given_value):
        if isinstance(given_value, int|float) and given_value > 0:
            self._amount = given_value
        else:
            raise TypeError("Please enter a valid positive number as Expense amount.")
        
    
    def update(self,title=None, amount=None):
        """Allows updating the title and/or amount, and updates the updated_at timestamp
            Default values for title and amount are None"""
        if title:
            self.title = title
            print(f"This expense title has been updated to {title} and the update time has been recorded.")
        if amount:
            self.amount = amount
            print(f"This expense amount has been updated to {amount} and the update time has been recorded.")
        if title or amount:
            self.updated_at = datetime.utcnow() #update time

    def to_dict(self):
        """Returns a dictionary reperesentation of the expense, repersents time in a readable format"""
        dict_rep = {'id': self.id, 'title': self.title, 'amount':self.amount,
                    'created_at': self.created_at.strftime('%X %a, %d/%m/%Y'), 'updated_at': self.updated_at.strftime('%X %a, %d/%m/%Y')} 
        return dict_rep
    
    
class ExpenseDB:
    """Manages a acollection of Expense objects"""
    def __init__(self,expenses=[]):
        """initializing attributes of the class"""
        for value in expenses:
            if not isinstance(value, Expense): #validate that we receive only instances of the expense class in this database
                expenses.remove(value)
                raise TypeError (f"{value} is not an object of the Expense Class.")
        self.expenses = expenses #a list storing Expense instances
   
    def add_expense(self,expense):
        """add an expense"""
        if isinstance(expense, Expense): #validate that we receive only instances of the expense class in this database
            self.expenses.append(expense)
            return f"{expense.title} expense successfully added."
        return "Only objects of class Expense are accepted."
    
    def remove_expense(self,expense_id):
        """Removes an expense"""
        for value in self.expenses:
            if value.id == expense_id:
                self.expenses.remove(value)
                return f"Object with '{value.id}' id has been removed from this expenses' database."
        return f"This '{expense_id}' id is not found in this expenses' database."

    def get_expense_by_id(self,expense_id):
        """Retrieves an expense by ID"""
        for value in self.expenses:
            if value.id == expense_id:
                return value
        return f"'{expense_id}' id not found in this expenses' database."
    
    def get_expense_by_title(self,expense_title):
        """Retrieves expenses by title"""
        possible_expenses =[]
        for value in self.expenses:
            if value.title == expense_title:
                possible_expenses.append(value)
        if possible_expenses:
            return possible_expenses
        return f"'{expense_title}' title not found in this expenses' database."
    
    def to_dict(self):
        """Returns a list of dictionaries representing expenses"""
        db_dict = [value.to_dict() for value in self.expenses]
        return db_dict