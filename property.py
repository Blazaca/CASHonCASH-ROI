import os

# CLEAR SCREEN - os.system('cls')
# Flag is used for all checks of correct input locally in calculation
print("Hello and welcome to the 'Four Sqaure Method!'")
input("\nPress enter to continue...")
os.system('cls')
def calculation():
    calculating = True
    flag = True
    invest_total = 0
    expense_total = 0
    rental_income = 0
    monthly_cash_flow = 0
    while calculating:
        while flag:
            # Rental income
            while flag:
                rental_income = input('What is your current total monthly rental income?\n'
                                    'Hint: This is the cost of the rental property per month total...\n')
                if int(rental_income.isnumeric()):
                    flag = False
                    rental_income = int(rental_income)
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            flag = True
            # Start adding together all expenses starting with taxes
            os.system('cls')
            while flag:
                print("Here we are going to calculate all of your current expenses\n"
                    "We will start off with a few examples.\n")
                expense_add = input('What is the total in taxes per month?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Adding in insurance
            flag = True
            while flag:
                expense_add = input('What is the total of insurance?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Adding in Utilities
            flag = True
            while flag:
                expense_add = input('What is the total of utilities?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Adding in HOA
            flag = True
            while flag:
                expense_add = input('What is the total of HOA fees?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Adding landscaping
            flag = True
            while flag:
                expense_add = input('What is for landscaping? (if any...)\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Monthly vacancy upkeep
            flag = True
            while flag:
                expense_add = input('Per month how are you saving for months of property vacancy?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Average of monthly repairs
            flag = True
            while flag:
                expense_add = input('What is the average cost of monthly repairs on the unit?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Adding Cap Ex
            flag = True
            while flag:
                expense_add = input('How much are you saving per month for' 
                                'large projects and property upgrades?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Property management cost
            flag = True
            while flag:
                expense_add = input('Per month how much do you spend on external management of the property?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Morgage
            flag = True
            while flag:
                expense_add = input('How much is the morgage per month if any?\n')
                if int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            print('These are our base expenses for most area in the US.'
                '\n If you have any more expenses please enter them now...')
            # Extra expenses
            flag = True
            while flag:
                expense_add = input('(At any time type "n" to continue.)\nExtra expenses: ')
                if expense_add.lower() == 'n':
                    flag = False
                elif int(expense_add.isnumeric()):
                    expense_total += int(expense_add)
                    print('Expense added...')
                else:
                    print('Invalid entry. Please use numbers only.')
            os.system('cls')
            print('This is the total of all expense:\n')
            print('$',expense_total)
            print('\nYour income minus your expenses:\n')
            print('$', rental_income - expense_total)
            monthly_cash_flow = rental_income - expense_total
            input("Press enter to continue...") 
            os.system('cls')
            print('We will now calculate your Cash on Cash ROI...')
            # ROI Calculate\
            # Down payment
            flag = True
            while flag:
                invest_add = input('What was your down payment cost?\n')
                if int(invest_add.isnumeric()):
                    invest_total += int(invest_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Closing costs
            flag = True
            while flag:
                invest_add = input('What was your closing costs?\n')
                if int(invest_add.isnumeric()):
                    invest_total += int(invest_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')   
            # House Renovations total
            flag = True
            while flag:
                invest_add = input('What was the total for initial house renovations?\n')
                if int(invest_add.isnumeric()):
                    invest_total += int(invest_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            # Total of other costs
            flag = True
            while flag:
                invest_add = input('Total of other costs... (type 0 if none)\n')
                if int(invest_add.isnumeric()):
                    invest_total += int(invest_add)
                    flag = False
                    os.system('cls')
                else: 
                    input('Invalid entry. Please use numbers only.\n Press enter...')
                    os.system('cls')
            yearly_cash_flow = monthly_cash_flow * 12
            if invest_total == 0:
                coc_roi = 0
            else:
                coc_roi = yearly_cash_flow/invest_total
            print('Your cash on cash return of investment is:\n',
                coc_roi, '%\n')
            input('Press enter to continue...')
            os.system('cls')
            print('Over all here are all the calculations made for today.\n'
                'Rental Income: $', rental_income, '\n', 'Total Expenses: $', expense_total, '\n'
            , 'Monthly Profit: $', monthly_cash_flow, '\n', 'Cash on Cash ROI: $', coc_roi, '\n\n')
            input('Press enter to continue...')
            os.system('cls')
            flag = True
            continue_calc = input('Would you like to make another calculation? y/n\n')
            if continue_calc.lower() == 'y':
                continue
            elif continue_calc.lower() == 'n':
                print('Thank you for using our CASH ON CASH ROI INVESTOR!')
                quit()

            else:
                input('Invalid entry. Please use "y" or "n" \n Press enter...')


calculation()
