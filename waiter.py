#reset order
global userOrder
userOrder = "null"
global orderList
orderList = []

#dictionary for menu
global menu
menu = {
    
    "food": {
        "Chicken Nuggets": "$4",
        "Fries": "$2",
        "Hamburger": "$7"
        ""
    },
    
    "drinks": {
        "Pepsi": "$2",
        "Coca-Cola": "$2",
        "Dr. Pepper": "$2",
        "Water": "$0"
    }
    
    
}

def prompt():
    print('Type "order" to order more, type "review" to review order')
    print('Type "done" if you are done ordering')
    selection = input("").strip().lower()
    if selection == "order": 
      orderGet(); 
    elif selection == "review":
      print ("")
      print (orderList)
      prompt();
    elif selection == "done":
        print("")
        print("")
        print("")
        print("Your order is:")
        for x in orderList:
            print(x)
    else:
      print ("That is not a valid command.")
      prompt();

def orderSuccess():
    print("")
    print("Added to order")
    prompt();
    

#def orderFinished():
    

#ordering function
def orderGet():
    print("We have:")
    for i in menu["food"] :
        print("Item: " + i, " Price: " + menu["food"][i])
    print("")
    for i in menu["drinks"] :
        print("Item: " + i, " Price: " + menu["drinks"][i])
    print("What would you like to order?")
    userOrder = input("").strip().lower().title()

    if userOrder in menu["food"] or menu["drinks"]:
        orderList.append(userOrder)
        orderSuccess();
    #when user orders something not on the menu, throw error
    else:
        print("That's not on the menu. Try something else");
        orderGet();


orderGet();

