my_dictionary = {"First name": "Hamuel", "Age": "27", "Country": 'USA', "Favorite Food": "Pork Tamales"}

def print_dictionary_values(dic):
    for keys,data in dic.items():
        print("My" + " " + keys + " " + "is" + " " + str(data))

print_dictionary_values(my_dictionary)
