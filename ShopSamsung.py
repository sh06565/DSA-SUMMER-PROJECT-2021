# importig funcitons that will be required to run our code

from abc import abstractproperty
import os
from os import system, name
from time import sleep
from tkinter import *
from tkinter.font import ROMAN, names
global cart
global totals
global data

# The main layout of terminal resembles a lot to the online mobile application.
# In which the main functions are that the user can add items to the cart, removes item from his cart, view his cart and then finally
# place his order.

# Thanks

# using a list to store our inventory, each dictionary inside of the list representing the data for an item.


def main_starting():
    global cart
    cart = {}
    global window
    window = Tk()
    window.state("zoomed")
    window.title("SHOP SAMSUNG")
    Label(window, text="===================").pack()
    Label(text="    SHOP SAMSUNG   ",  fg="black",
          width="60", height="2", font=("Calibri", 16)).pack()
    Label(window, text="===================").pack()
    Label(window, text="").pack()
    Button(text="Login", width="50", height="2",
           bg="grey", fg="white", command=login).pack()
    Label(window, text="").pack()
    Button(text="Register", width="50", height="2",
           bg="grey", fg="white", command=register).pack()
    window.mainloop()
    pass


def login():
    global screen2
    screen2 = Toplevel(window)
    screen2.title("Login")
    screen2.state("zoomed")
    Label(screen2, text="===============================").pack()
    Label(screen2, text="Please enter your details below").pack()
    Label(screen2, text="===============================").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", bg="grey", fg="white", width=10,
           height=1, command=login_verify).pack()
    pass


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            pass_not_recognised()
    else:
        user_not_found()
    pass


def login_success():
    screen3 = Toplevel(window)
    screen3.title("Success")
    screen3.state("zoomed")
    x = Label(screen3, text="Login Success").pack()
    Button(screen3, text="OK", bg="grey", fg="white",
           command=lambda: delete(screen3)).pack()
    delete(screen2)
    window.destroy()
    main()

    pass


def pass_not_recognised():
    screen4 = Toplevel(window)
    screen4.title("Failed")
    screen4.state("zoomed")
    Label(screen4, text="Password not recognised").pack()
    Button(screen4, text="OK", command=lambda: delete(screen4)).pack()
    pass


def user_not_found():
    screen5 = Toplevel(window)
    screen5.title("Not Found")
    screen5.state("zoomed")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=lambda: delete(screen5)).pack()
    pass


def delete(screen):
    screen.destroy()
    pass


def register():
    global screen1
    screen1 = Toplevel(window)
    screen1.title("Register")
    screen1.state("zoomed")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="==========================").pack()
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="==========================").pack()
    Label(screen1, text="Usename *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Register", bg="grey", fg="white", width=10,
           height=1, command=register_user).pack()
    pass


def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text=" Registration Successful!",
          fg="green", font=("calibri", 11)).pack()
    pass


def clear():
    for widgets in root.winfo_children():
        widgets.destroy()


data = [
    {"id": 1301, "Info": "1301    Samsung Galaxy A20      Price   " +
        str(15999), "Name": "Samsung Galaxy A20", "Price": 15999, "Stock": 10},
    {"id": 1408, "Info": "1408    Samsung Galaxy A81      Price   " +
        str(61999), "Name": "Samsung Galaxy A81", "Price": 61999, "Stock": 10},
    {"id": 1503, "Info": "1503    Samsung Galaxy A30      Price   " +
        str(23999), "Name": "Samsung Galaxy A30", "Price": 23999, "Stock": 10},
    {"id": 1065, "Info": "1065    Samsung Galaxy A51      Price   " +
        str(41999), "Name": "Samsung Galaxy A51", "Price": 41999, "Stock": 10},
    {"id": 1070, "Info": "1070    Samsung Galaxy A82      Price   " +
        str(67999), "Name": "Samsung Galaxy A82", "Price": 67999, "Stock": 10},
    {"id": 1025, "Info": "1025    Samsung Galaxy A52      Price   " +
        str(44999), "Name": "Samsung Galaxy A52", "Price": 44999, "Stock": 10},
    {"id": 1802, "Info": "1802    Samsung Galaxy A21      Price   " +
        str(18999), "Name": "Samsung Galaxy A21", "Price": 18999, "Stock": 10},
    {"id": 1026, "Info": "1026    Samsung Galaxy A61      Price   " +
        str(53499), "Name": "Samsung Galaxy A61", "Price": 53499, "Stock": 10},
    {"id": 1301, "Info": "1301    Samsung Galaxy A72      Price   " +
        str(59999), "Name": "Samsung Galaxy A72", "Price": 59999, "Stock": 10}
]


# function that displays the inventory to the user


def userMenu(x):
    c = 0
    for each in x:
        p = Label(root, text=each["Info"]).pack()
        c += 1
        if c != len(x):
            Label(root, text="").pack()

# function that clears the screen

# quick sort, sorts the prices


def quicksort(lst, check2):
    if len(lst) <= 1:
        return lst
    # if check is l then it sorts from low to high
    if check2 == "l":
        p = lst.pop()
        gi, li = [], []
        # get each item's dict from our inventory's list
        for c in lst:
            # comparing the Price values of items
            if c["Price"] > p["Price"]:
                gi.append(c)
            else:
                li.append(c)
        # recursion returning the sorted list
        return quicksort(li, check2)+[p]+quicksort(gi, check2)
    # if check is h then it sorts from high to low
    elif check2 == "h":
        p = lst.pop()
        gi, li = [], []
        # get each item's dict from our inventory's list
        for c in lst:
            # comparing the Price values of items
            if c["Price"] < p["Price"]:
                gi.append(c)
            else:
                li.append(c)
        # recursion returning the sorted list
        return quicksort(li, check2)+[p]+quicksort(gi, check2)


def linear_search(lst, item):
    front = 0
    rear = len(lst)-1
    while front < rear:
        if int(item) == int((lst[front])["id"]):
            return front
            # return True
        elif int(item) == int((lst[rear])["id"]):
            return rear
            # return True
        else:
            front += 1
            rear -= 1

    return -1


# function that filters the inventory data, by either high or low using bubble sort


def filter():
    # print() statement for spacing

    # asks user if they would like to filter the prices
    check = Entry(root)

    v = Label(root, text="Would you like to filter the prices? Y or N?").pack()
    # Label(root,text="").pack()
    check.pack()
    Label(root, text="").pack()
    confirm = Button(root, text="Confirm", bg="grey", fg="white",
                     command=lambda: answer(check.get())).pack()


def answer(x):
    if x.lower() == "y":
        clear()
        Label(root, text="").pack()
        f = Label(root, text="To filter from low to high Enter L, Else H. ").pack()
        Label(root, text="").pack()
        check2 = Entry(root)
        check2.pack()
        Label(root, text="")
        confirm1 = Button(root, text="Confirm", bg="grey", fg="white",
                          command=lambda: filter1(check2.get())).pack()
        Label(root, text="")
    elif(x.lower() == "n"):

        # INV=data
        shoppingCart(x, cart, filtered=[])
        # userMenu(data)


def filter1(check2):
    check2 = check2.lower()
    # if yes, then we ask if they would like to filter from low to high or high to low
    clear()
    filtered = (quicksort(data, check2))
    userMenu(filtered)
    # INV=filtered
    clear()
    shoppingCart(check2, cart, filtered)


# funcion that updates the stock in the inventory when changes are made to cart


def stock(qnty, position):
    qnty = int(qnty)
    x = int((data[position])["Stock"])
    if x == qnty or x > qnty:
        return x
    # else if stock is less than our quantity then negative stock is returned
    elif x < qnty:
        return -x


def update_Astock(item, qnty):
    pos = linear_search(data, item)
    data[pos]["Stock"] = int((data[pos])["Stock"])-int(qnty)
    pass
# function that adds selected items to cart


def addprompt(cart):
    gh = Label(root, text="Enter the id of the item u would like to add: ").pack()
    item = Entry(root)
    item.pack()
    fg = Label(root, text="Kindly enter the quantity of the item: ").pack()
    qnty = Entry(root)
    qnty.pack()
    Button(root, text="Confirm", bg="grey", fg="white", command=lambda: add(
        cart, item.get(), qnty.get())).pack()


def add(cart, item, qnty):

    # asks user for the item that they would like to add to cart

    # we get the index of our dictionary from the list

    position = linear_search(data, item)
    # check for if index in list
    if position != -1:
        # ask for the required quantity of the item

        # check, using our stock fucniton, that if the entered quantity is available
        ok = stock(qnty, position)
        if ok <= 0:
            # if there isnt enough stock it displays an error msg and calls the add(cart) fucntion back
            fd = Label(root, text="There isn't that much stock, only " +
                       str(-1*ok)+" pieces are available.").pack()
            de = Label(
                root, text="Kindly selecct the quantity accordingly!").pack()
            add(cart, item=int, qnty=int)
        else:
            if int(item) in cart.keys():
                x = cart[int(item)]
                name = x[0]
                new_qnty = int(x[1])+int(qnty)
                new_price = int(x[2]) + \
                    (int((data[position])["Price"])*int(qnty))
                del(cart[int(item)])
                cart[item] = [name, new_qnty, new_price]
            # if stock is present then it adds the to the cart with the set quantity and their total price
            else:
                price = int((data[position])["Price"])*int(qnty)
                name = (data[position])["Name"]
                cart[(data[position])["id"]] = [name, qnty, price]
            update_Astock(item, qnty)
            # print(cart)
            # Button(root, text="OK",
            #        command=lambda: shoppingCart(p, t,cart)).pack()
            Label(root, text="Item added to cart!").pack()
            shoppingCart(p, cart, t)
    else:
        # if id not in inventory then it outputs an error msg
        dsa = Label(root, text="Enter a valid id to add!").pack()


def update_Rstock(item, qnty):
    pos = linear_search(data, item)
    data[pos]["Stock"] = int((data[pos])["Stock"])+qnty
# function deletes the selected item from the cart


def remove_prompt1(cart):
    clear()
    # displays cart to user
    Label(root, text="").pack()
    viewcart(cart)
    Label(root, text="").pack()
    Label(root, text="").pack()
    # inputs for the item id to be removed
    x = Label(root, text="Enter the item id that you would like to remove: ").pack()
    Label(root, text="").pack()
    item = Entry(root)
    item.pack()
    Label(root, text="").pack()
    Button(root, text="Confirm", bg="grey", fg="white", command=lambda: remove_prompt2(
        item.get(), cart)).pack()
    Label(root, text="").pack()
    pass


def remove_prompt2(item, cart):
    if int(item) in cart.keys():
        # inputs the quantity of that item to be removed
        Label(root, text="Enter the quantity that you would like to remove: ").pack()
        qnty = Entry(root)
        qnty.pack()
        Button(root, text="Confirm", bg="grey", fg="white", command=lambda: remove(
            int(item), int(qnty.get()), cart)).pack()
    else:
        # if id not present in cart prompts the user to enter a valid id
        Label(root, text="Enter a valid id to remove!").pack()
        clear()
        remove_prompt1(cart)
    pass


def remove(item, qnty, cart):
    # if the cart quantity matches the entered quantity
    if int(cart[item][1]) == qnty or int(cart[item][1]) == 1:
        # deletes that item from cart
        del(cart[item])
        Label(root, text="Item removed from cart!").pack()
        update_Rstock(item, qnty)
        clear()
        shoppingCart(p, cart, t)
    # else if quantitiy does not match the items quantity in cart then it tells the user to enter a valid quantity
    elif int(cart[item][1]) < qnty:
        Label(root, text="Entered quantity doesn't exist, enter a valid quantity to remove!").pack()
        remove_prompt2(item, cart)
    # else, then it removes the set quantity from the cart
    else:
        # removing item from cart
        intial = int(cart[item][1])
        cart[item][1] = int(cart[item][1])-qnty
        cart[item][2] = int(cart[item][2])-(int(cart[item][2]/intial)*qnty)
        Label(root, text="Item removed from cart!").pack()
        update_Rstock(item, qnty)
        clear()
        shoppingCart(p, cart, t)

# fucnion that displays the cart to the user


def viewcart(cart):
    #Label(root, text="ID      Name                       Quantity    Price").pack()
    # Label(root, text="ID---    NAME--------------      PRICE   " +"-----").
    Label(root, text="ID"+"   "+"NAME--------------" +
          "         " + "QNTY"+"           "+"PRICE").pack()
    Label(root, text="").pack()
    for key, value in cart.items():
        Label(root, text=str(key)+"  "+value[0]+"         " +
              str(value[1])+"           "+str(value[2])).pack()

# fucntion that displays the total bill


def checkout(cart):
    clear()
    total = 0
    # sums up all the prices of items present in our cart
    for key, value in cart.items():
        total += value[2]
    if cart != {}:
        Label(root, text="").pack()
        Label(root, text="Shown below is your cart").pack()
        Label(root, text="").pack()
        viewcart(cart)
        Label(root, text="").pack()
        # displays the receipt
        Label(root, text="========================").pack()
        Label(root, text="Total:                  " +
              str(total)).pack()
        Label(root, text="========================").pack()
        Label(root, text="").pack()
        Button(root, text="Next", bg="grey",
               fg="white", command=location).pack()

    # if the total is < or =  0 it means that there is no item in cart, so it prompts the user that they can not proceed to checkout
    if total <= 0:

        Label(root, text="Your cart is empty, you can not proceed to checkout!").pack()
        Button(root, text="Back", bg="grey", fg="white",
               command=lambda: shoppingCart(p, cart, t)).pack()

# funciton that displays the delivery time and the fastest route that the rider will take


def final_check(cart):
    clear()
    total = 0
    # sums up all the prices of items present in our cart
    for key, value in cart.items():
        total += value[2]
    if cart != {}:
        viewcart(cart)

        # displays the receipt
        Label(root, text="========================").pack()
        Label(root, text="Total:                  " +
              str(total)).pack()
        Label(root, text="========================").pack()
        Label(root, text="").pack()

# dijkstra gives us the delivery path and time taken from our store to the user's area


def dijsktra(graph, start, end):
    lst_nodes = list(graph.keys())
    short_dist, visited, infinity = {}, [], 9999
    for each_node in lst_nodes:
        if each_node == start:
            short_dist[each_node] = ("", 0)
        else:
            short_dist[each_node] = ("", infinity)
    while len(visited) != len(lst_nodes):
        lst = []
        for value in short_dist.items():
            if value[0] not in visited:
                lst.append(value[1][1])
        min_d = min(lst)
        for key, value in short_dist.items():
            if min_d == value[1] and key not in visited:
                visited.append(key)
                for val in graph[key]:
                    temp = short_dist[key][1] + (val[1])
                    if temp < short_dist[val[0]][1]:
                        short_dist[val[0]] = (key, temp)
    path = []
    x = ""
    y = end
    while x != start:
        x = short_dist[y][0]
        path.insert(0, (x, y))
        y = x
    time = 0
    # calculates the total time taken that the rider will take to get the products to the user
    for each in path:
        time += (short_dist[each[1]])[1]
    final = ""
    # makes the path that the rider will take to get from DHA to the selected delivery area
    for tuple in path:
        for each in tuple:
            if each not in final:
                final += each+" --> "
    Label(root, text="").pack()
    final_check(cart)
    Label(root, text="").pack()
    Label(root, text="==> The path from our store to your area is " +
          final[:-4].upper()).pack()
    Label(root, text="").pack()
    Label(root, text="==> The time taken to reach your area will be  " +
          str(time)+" mins.").pack()
    Label(root, text="").pack()
    Label(root, text="TYPE Enter for a new user or Exit to end program: ").pack()
    Label(root, text="").pack()
    OK = Entry(root)
    OK.pack()
    Label(root, text="").pack()
    Button(root, text="Confirm", bg="grey",
           fg="white", command=lambda: last(OK)).pack()


def last(OK):
    if OK.get().lower() == "enter":
        root.destroy()
        main_starting()
    elif OK.get().lower() == "exit":
        exit()


def location():
    clear()
    # dicionary of areas that we deliver to
    areas = {
        1: "DHA",
        2: "Bahadrabad",
        3: "Clifton",
        4: "Cantt",
        5: "Saddar",
        6: "Nazimabad",
        7: "Saki Hassan",
        8: "Garden",
        9: "North Nazimabad",
        10: "North Karachi"
    }
    # connnections of our delivery areas
    links = {
        "DHA": [("Bahadrabad", 22), ("Clifton", 12), ("Cantt", 12)],
        "Bahadrabad": [("Saki Hassan", 19), ("Saddar", 9), ("DHA", 20)],
        "Clifton": [("Saddar", 12), ("Cantt", 10), ("Garden", 20), ("DHA", 11)],
        "Cantt": [("DHA", 14), ("Clifton", 11), ("Saddar", 8)],
        "Saddar": [("Clifton", 14), ("Cantt", 7), ("Bahadrabad", 14), ("North Nazimabad", 25), ("Nazimabad", 18), ("Garden", 9)],
        "Nazimabad": [("North Nazimabad", 10), ("North Karachi", 17), ("Saddar", 20)],
        "Saki Hassan": [("Bahadrabad", 21)],
        "Garden": [("Clifton", 18), ("Saddar", 9)],
        "North Nazimabad": [("Nazimabad", 11)],
        "North Karachi": [("Nazimabad", 18)]
    }
    # asks the user to select their delivery area
    Label(root, text="""
    Our Store is located in DHA and below are the available delivery options:
    ================================
    Delivery options
    ================================

    1:"DHA"

    2:"Bahadrabad"

    3:"Clifton"

    4:"Cantt"

    5:"Saddar"

    6:"Nazimabad"

    7:"Saki Hassan"

    8:"Garden"
     
    9:"North Nazimabad"

    10:"North Karachi"
    """).pack()
    Label(root, text="Kindly choose your residential area : ").pack()
    Label(root, text="").pack()
    choice = Entry(root)
    choice.pack()
    Label(root, text="").pack()
    Button(root, text="Confirm", bg="grey", fg="white", command=lambda: loci(
        choice.get(), areas, links)).pack()

    # checks if the selected choice is present in our areas


def loci(choice, areas, links):
    choice = int(choice)
    if choice in areas.keys():
        # if areas is no.1 then it is the same area as our store
        if choice == 1:
            clear()
            Label(root, text="==> Our Store is located in your area.").pack()
            Label(root, text="==> The time taken to reach your area will be  " +
                  str(5)+" mins.").pack()
            Label(root, text="TYPE Enter for a new user or Exit to end program: ").pack()

            OK = Entry(root)
            OK.pack()
            Button(root, text="Confirm", bg="grey",
                   fg="white", command=lambda: last(OK)).pack()

        else:
            # calls the dijkstra function to display rider path and time taken
            clear()
            dijsktra(links, "DHA", areas[choice])

        # print("-----------------------------------")
    else:
        # if area not present in dict then it prompts the user and calls the location function again
        Label(root, text="").pack()
        Label(root, text="You have entered an invalid choice, kindly enter again!").pack()
        location()

# function that has all the commands that we can make to our shopping cart


def shoppingCart(check, cart, filtered=[]):
    global p
    global t
    p = check
    t = filtered
    # displays the available options to the user
    clear()
    # userMenu(INV)
    yt = Label(root, text="These are the avialble products").pack()
    Label(root,      text="===============================").pack()
    # Label(root,text="").pack()
    gt = Label(
        root, text="ID---    NAME--------------      PRICE   " + "-----").pack()
    Label(root, text="").pack()
    if check.lower() == "n":
        userMenu(data)
        Label(root,      text="===============================").pack()
    elif check.lower() == "l" or check.lower() == "h":
        userMenu(filtered)
        Label(root,      text="===============================").pack()
    display = Label(root, text="Shopping basket options").pack()
    # choice1 = Label(root, text="Kindly choose your choice: ").pack()
    # inputs the choice from the user
    choice1 = Button(root, text="1: Add item", bg="light grey", fg="green",
                     command=lambda: addprompt(cart)).pack()
    choice2 = Button(root, text="2: Remove item", bg="light grey", fg="green",
                     command=lambda: remove_prompt1(cart)).pack()
    choice3 = Button(root, text="3: View cart", bg="light grey", fg="green",
                     command=lambda: viewcart(cart)).pack()
    choice0 = Button(root, text="0: Proceed to checkout", bg="light grey", fg="green",
                     command=lambda: checkout(cart)).pack()


def main():

    global root
    # main funciton that runs the whole code
    root = Tk()
    root.title("AL CHUK")
    root.state("zoomed")

    # displays welcome msg

    # displays the available products

    # j = Button(root, text="Welcome", command=userMenu(data)).pack()
    yt = Label(root, text="These are the avialble products").pack()
    Label(root,      text="===============================").pack()
    # Label(root,text="").pack()
    #h = Label(root, text="ID      Name                    Price   ").pack()
    h = Label(
        root, text="ID---    NAME--------------      PRICE   " + "-----").pack()
    Label(root, text="").pack()
    userMenu(data)
    Label(root,      text="===============================").pack()
    filter()

    root.mainloop()


   # call the main function
main_starting()
