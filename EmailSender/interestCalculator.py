def main():
    print("This is A monthly Payment Loan Calculator")
    print("")

    principle = float(input("Enter the loan Amount::"))
    apr = float(input("Enter the anual Interest rates:: "))
    years = int (input("Enter amount of years::"))

    monthly_interest_rate = apr/1200
    amount_of_months = years *12
    monthly_payment = principle+monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months))


    print("The MOnthly Payment for this lone is :%.2f"%monthly_payment)
                      
main()