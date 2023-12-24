from expenseDBClass import Expense, ExpenseDB

if __name__ == "__main__":

    store1 = ExpenseDB([Expense('t-shirt',2000.0),Expense('pants',10000.9)])

    mon=Expense('pants',5000)
    tue=Expense('blouse',4000)
    wed=Expense('t-shirt',3000)
    thu=Expense('bags',15000.98)
    fri=Expense('jewelry',670.5)
    sat=Expense('shoes',30500)
    sun=Expense('jewelry',6000)
    t=wed.id

    for value in [mon,tue,wed,thu,fri,sat,sun]:
        print(store1.add_expense(value))

    print(store1.get_expense_by_title('jewelry'))
    print(store1.get_expense_by_id(t))
    print(store1.get_expense_by_id('tesr'))
    print(store1.remove_expense(t))
    print(store1.get_expense_by_title('pants'))