def make_change(cents):
    dollar_amount = 0
    halfdollar_amount = 0
    quarter_amount = 0
    dime_amount = 0
    nickel_amount = 0
    penny_amount = 0
    change_back = {"dollars_back": 0,"halfdollars_back": 0, "quarters_back": 0, "dimes_back": 0, "nickels_back": 0, "pennies_back": 0,}
    # To put our coin amounts into a new dictionary (Dictionaries Lesson in Python Fundamentals "Creating Dictonaries")
    money_type = {"dollar": 1.00, "halfdollar": .50, "quarter": 0.25, "dime": 0.10, "nickel": 0.05, "penny": 0.01}
    for data in money_type:
        if cents >= 1.00:
            dollar_amount= dollar_amount + 1
            cents = cents - money_type["dollar"]
            change_back["dollars_back"] = change_back["dollars_back"] + 1

        elif cents >= .50:
            halfdollar_amount= halfdollar_amount + 1
            cents = cents - money_type["halfdollar"]
            change_back["halfdollars_back"] = change_back["halfdollars_back"] + 1
        elif cents >= .25:
            quarter_amount = quarter_amount + 1
            cents = cents - money_type["quarter"]
            change_back["quarters_back"] = change_back["quarters_back"] + 1
        elif cents >= .10:
            dime_amount= dime_amount + 1
            cents = cents - money_type["dime"]
            change_back["dimes_back"] = change_back["dimes_back"] + 1
        elif cents >= .05:
            nickel_amount= nickel_amount + 1
            cents = cents - money_type["nickel"]
            change_back["nickels_back"] = change_back["nickels_back"] + 1
        elif cents >= .01:
            penny_amount= penny_amount + 1
            cents = cents - money_type["penny"]
            change_back["pennies_back"] = change_back["pennies_back"] + 1

    print("You get back...")
    print(dollar_amount, "dollar(s)")
    print(halfdollar_amount, "halfdollar(s)")
    print(quarter_amount, "quarter(s)")
    print(nickel_amount, " nickel(s)")
    print(dime_amount, " dime(s)")
    print(penny_amount, " pennies")
    print("Thank you for shopping at Kwik I Mart!!!")
    print(change_back)
    return change_back

make_change(.76)
