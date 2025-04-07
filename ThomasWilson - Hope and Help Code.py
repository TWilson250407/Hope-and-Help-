#this is the final code for the hope and help system and includes all annotations 


#imports everything that needs to be called for GUI's and the pkl files 
import tkinter as tk
import pickle
import re 
from tkinter import messagebox


#this defines the customer class used for the customer pages 
class Customer:
    def __init__(self, username, password, phone, address):
        
        self.username = username
        self.password = password
        self.phone = phone
        self.address = address
        
#this defines the staff class used for the staff pages 
class Staff:
    def __init__(self, username, password, phone, address):
        
        self.username = username
        self.password = password
        self.phone = phone
        self.address = address

#this defines the stock class used for the stock pages 
class Stock:
    def __init__(self, release_name, pformat, release_year, price, artist, stockid):
        self.release_name = release_name
        self.pformat = pformat
        self.release_year = release_year
        self.price = price
        self.artist = artist
        self.stockid = stockid


#defines the login page, with the dimensions, title and colour declared beneath it     
def login():
    login_page = tk.Tk()
    login_page.geometry('600x400')
    login_page.title('Staff Login')
    login_page.configure(bg="black")  

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    label = tk.Label(login_page, text=' Hope and Help Staff Login', font=('Arial', 15), bg="black", fg="white")
    label.place(x=130, y=10, width=350, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    labelu = tk.Label(login_page, text="Staff Username", bg="black", fg="white")
    labelu.place(x=130, y=50, width=350, height=30)

    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included 
    entryu = tk.Entry(login_page, bg="gray", fg="white", insertbackground="white")
    entryu.place(x=130, y=90, width=350, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    labelp = tk.Label(login_page, text="Password", bg="black", fg="white")
    labelp.place(x=130, y=140, width=350, height=50)

    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included 
    entryp = tk.Entry(login_page, bg="gray", fg="white", insertbackground="white")
    entryp.place(x=130, y=180, width=350, height=50)

    #creates a button used on the page, which is used to execute the login_staff command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    button = tk.Button(login_page, text="Login", command=lambda: login_staff(entryu, entryp, login_page), bg="purple", fg="white", font=('Arial', 10, 'bold'))
    button.place(x=130, y=240, width=350, height=50)

    login_page.mainloop()

#creates the validation loop for when attempting to login  
def login_staff(entryu, entryp, login_page):
    username = entryu.get()
    password = entryp.get()
    valid = False

#this validates a staff account exists in the staff pkl file 
    with open("the_staff.pkl", 'rb') as file:
        staff_users = pickle.load(file)
        for i in range(len(staff_users)):
            if staff_users[i].username == username and staff_users[i].password == password:
                valid = True
                login_page.destroy()
                main_page()
        #this is the negative response if the credentials aren't found          
        if valid == False:
            messagebox.showerror("Error", "Username or password not found")
            return
         

#defines the main_page and its dimensions, title and colour beneath
#this page is the staff hub and is the connector to all the main functionality of the system
def main_page():
    main_page = tk.Tk()
    main_page.geometry('600x450')
    main_page.title('Staff Hub')
    main_page.configure(bg="black")

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    label = tk.Label(main_page, text='Hope and Help Staff Hub', font=('Arial', 15), bg="black", fg="white")
    label.place(x=180, y=20, width=250, height=60)
    button_style = {"bg": "purple", "fg": "white", "font": ('Arial', 10, 'bold')}

    #creates a button used on the page, which is used to execute the add_trans_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonAT = tk.Button(main_page, text="Add Transaction", command=add_trans_page, **button_style)
    buttonAT.place(x=40, y=80, width=170, height=60)

    #creates a button used on the page, which is used to execute the ed_trans_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonEDT = tk.Button(main_page, text="Manage Transactions", command=ed_trans_page, **button_style)
    buttonEDT.place(x=220, y=80, width=170, height=60)

    #creates a button used on the page, which is used to execute the uth_search command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonSUT = tk.Button(main_page, text="Search User Transaction", command=uth_search, **button_style)
    buttonSUT.place(x=400, y=80, width=170, height=60)

    #creates a button used on the page, which is used to execute the a_staff_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonASA = tk.Button(main_page, text="Add Staff", command=a_staff_page, **button_style)
    buttonASA.place(x=40, y=150, width=170, height=60)

    #creates a button used on the page, which is used to execute the ed_staff_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonEDSA = tk.Button(main_page, text="Manage Staff", command=ed_staff_page, **button_style)
    buttonEDSA.place(x=220, y=150, width=170, height=60)

    #creates a button used on the page, which is used to execute the a_customer_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonAC = tk.Button(main_page, text="Add Customer", command=a_customer_page, **button_style)
    buttonAC.place(x=400, y=150, width=170, height=60)

    #creates a button used on the page, which is used to execute the ed_customer_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonEDC = tk.Button(main_page, text="Manage Customers", command=ed_customer_page, **button_style)
    buttonEDC.place(x=40, y=220, width=170, height=60)

    #creates a button used on the page, which is used to execute the a_stock_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonAS = tk.Button(main_page, text="Add Stock", command=a_stock_page, **button_style)
    buttonAS.place(x=220, y=220, width=170, height=60)

    #creates a button used on the page, which is used to execute the ed_stock_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonEDS = tk.Button(main_page, text="Manage Stock", command=ed_stock_page, **button_style)
    buttonEDS.place(x=400, y=220, width=170, height=60)

    #creates a button used on the page, which is used to execute the ss_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonSS = tk.Button(main_page, text="Search Stock", command=ss_page, **button_style)
    buttonSS.place(x=220, y=290, width=170, height=60)

    main_page.mainloop()
  
#this creates the interface that holds two drop down menus, one text box and a button.
# The first part of code is retrieving the customer usernames and the stock release names so that you can select them in the drop down menus

def add_trans_page():
    with open("the_stock.pkl", 'rb') as file:
        stock_users = pickle.load(file)
    stock_names = []
    for i in range(len(stock_users)):
        release_info = f"{stock_users[i].release_name}({stock_users[i].pformat})" #imports the stock release name and pformat into the same drop down, so that if their are 
        stock_names.append(release_info)                                            #multiple of the same release on different physical formats their is no confusion 
    with open("the_customer.pkl", 'rb') as file:
        customer_users = pickle.load(file)      #this loads all customer usernames into the customer_names list so that they are pasted into the drop down for customer accounts
    customer_names = []
    for i in range(len(customer_users)):
        customer_names.append(customer_users[i].username)

    # creates the interface to be interacted with
    # this includes labels, buttons and drop down menus 
    root = tk.Tk()
    root.geometry('600x450')
    root.title('Add Transaction')
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    label = tk.Label(root, text='Add Transaction', font=('Arial', 15), fg='white', bg='black')
    label.place(x=150, y=20, width=350, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    # This also creates a drop down that imports the stock names from the code annotated just above this tk inter
    labelU = tk.Label(root, text="Release Name", fg='white', bg='black')
    labelU.place(x=150, y=60, width=350, height=50)
    stock_list = tk.StringVar(root)
    stock_list.set(stock_names[0])
    stockopt = tk.OptionMenu(root, stock_list, *stock_names)
    stockopt.place(x=140, y=100, width=350, height=50)
    stockopt.config(bg='purple', fg='white')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included 
    # This also creates a drop down that imports the customer accounts from the code annotated just above this tk inter 
    labelU2 = tk.Label(root, text="Customer Username", fg='white', bg='black')
    labelU2.place(x=140, y=150, width=350, height=50)
    customer_list = tk.StringVar(root)
    customer_list.set(customer_names[0])
    customeropt = tk.OptionMenu(root, customer_list, *customer_names)
    customeropt.place(x=140, y=200, width=350, height=50)
    customeropt.config(bg='purple', fg='white')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #also creates an entry box that follows the same principals as all other text entry boxes on the system
    labelD = tk.Label(root, text='Date (dd/mm/yy)', fg='white', bg='black')
    labelD.place(x=140, y=250, width=350, height=50)
    entryD = tk.Entry(root, bg='grey', fg='white')
    entryD.place(x=140, y=300, width=350, height=50)

    #creates a button used on the page, which is used to execute the add_trans command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonA = tk.Button(root, text="Add Transaction", command=lambda: add_trans(stock_list, customer_list, entryD, root), bg='purple', fg='white')
    buttonA.place(x=140, y=380, width=350, height=50)
    
    root.mainloop()

# this is the function that allows transactions to be saved to their pickle file, if it passes the correct validation
def add_trans(stock_list, customer_list, entryD, root):
    selected_stock = stock_list.get()
    selected_customer = customer_list.get()
    entered_date = entryD.get()
    root.destroy()
    validate_pass = True
    #validation to only allow nn/nn/nn otherwise it passes as false 
    if not re.match(r"^\d{2}/\d{2}/\d{2}$", entered_date):
        messagebox.showerror("Validation Error", "Invalid date format. Please use nn/nn/nn.")
        validate_pass = False
    #validates the customer selected for the transaction exists, else it will pass as false 
    try:
        with open('the_customer.pkl', 'rb') as file:
            customer_list = pickle.load(file) 
        username_found = False
        for customer in customer_list:
            try:
                if customer.username == selected_customer:
                    username_found = True
                    break  
            except AttributeError:
                continue
        if not username_found:
            messagebox.showerror("Validation Error", "Username not found in the database.")
            validate_pass = False
    #errors for if the customer pkl file is not found or if an unexpected error occurs 
    except FileNotFoundError:
        messagebox.showerror("Error", "Customer database file not found.")
        validate_pass = False
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        validate_pass = False
    #if customer account is found + date entered is valid, the validation loop is broken and proceeds to the attempt to save the added transaction 
    if validate_pass:
        try:
            transaction = {"release_name": selected_stock, "customer_username": selected_customer, "date": entered_date}

            try:
                with open("the_trans.pkl", 'rb') as file:
                    transactions = pickle.load(file)
            except FileNotFoundError:
                transactions = []

            transactions.append(transaction)
            with open("the_trans.pkl", 'wb') as file:
                pickle.dump(transactions, file)

            messagebox.showinfo("Success", "Transaction added successfully!") #provides a popup if the transaction saves successfully 

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred while saving: {e}")
    else:
        messagebox.showerror("Failure", "Transaction failed to save.")

# This defines the edit and delete transaction page, where it takes the already saved data for the customer username, date and also the release name of the stock.
# This then creates a page with a drop down to select the customer usernames that have been saved into the trans file 
# and then opens another page with a drop down that allows you to select the specific transaction with the date and release name.        
def ed_trans_page():
    

    try:
        with open("the_trans.pkl", 'rb') as file:
            trans_list = pickle.load(file)
        trans_users = list(set(trans["customer_username"] for trans in trans_list)) #calls all customer usernames from the transaction  pkl file 
    except FileNotFoundError:
        trans_list = []
        trans_users = []
    if not trans_users:
        messagebox.showerror("Error", "No transactions found!") #creates and error popup if there are no transactions in the pkl file 
        return

    #creates the edit traansaction GUI, with the geometry, title and colour defined below 
    root = tk.Tk()
    root.geometry('500x350')
    root.title('Manage Transactions')
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text="Manage Transactions", font=('Arial', 15), fg='white', bg='black')
    label.place(x=90, y=20, width=350, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    labelTrans = tk.Label(root, text="Select User", fg='white', bg='black')
    labelTrans.place(x=90, y=60, width=350, height=50)

    #creates the drop down to select the customer usernames that have made a transaction 
    user_var = tk.StringVar(root)
    user_var.set(trans_users[0])
    user_menu = tk.OptionMenu(root, user_var, *trans_users)
    user_menu.place(x=90, y=110, width=350, height=50)
    user_menu.config(bg='purple', fg='white')

    #creates a button used on the page, which is used to execute the show_trans_page command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonSelect = tk.Button(root, text="Select User", command=lambda: show_trans_page(user_var, trans_list, root), bg='purple', fg='white')
    buttonSelect.place(x=90, y=170, width=350, height=50)

    root.mainloop()

#displays a page where you can select the transaction out the ones made by the customer username entered in the previous function
def show_trans_page(user_var, trans_list, root):
    selected_user = user_var.get()
    user_transactions = [trans for trans in trans_list if trans["customer_username"] == selected_user]

    if not user_transactions:
        messagebox.showerror("Error", "No transactions found for this customer.")
        return
    #creates the popup that contains the drop down to select a transaction made by the selected customer account, with the geometry, title and colour defined below
    popup = tk.Toplevel(root)
    popup.title(f"Transactions for {selected_user}")
    popup.geometry('500x350')
    popup.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(popup, text=f"Select a transaction for {selected_user}", font=('Arial',15), fg='white', bg='black')
    label.place(x=90, y=60, width=350, height=50)

    #creates the drop down to select the transaction made by the selected customer account, where it calls the release name and the date the transaction was made
    trans_var = tk.StringVar(popup)
    trans_var.set(f"{user_transactions[0]['release_name']} ({user_transactions[0]['date']})")
    trans_options = [f"{trans['release_name']} ({trans['date']})" for trans in user_transactions]
    trans_menu = tk.OptionMenu(popup, trans_var, *trans_options)
    trans_menu.place(x=90, y=100, width=350, height=50)
    trans_menu.config(bg='purple', fg='white')

    #creates a button used on the page, which is used to execute the edit_trans command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonEdit = tk.Button(popup, text="Edit Transaction", command=lambda: edit_trans(trans_var, user_transactions, trans_list, popup), bg='purple', fg='white')
    buttonEdit.place(x=90, y=160, width=170, height=50)

    #creates a button used on the page, which is used to execute the delete_transaction command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonDelete = tk.Button(popup, text="Delete Transaction", command=lambda: delete_transaction(trans_var, user_transactions, trans_list, popup), bg='purple', fg='white')
    buttonDelete.place(x=270, y=160, width=170, height=50)

    popup.mainloop()

#defines the function to edit a transaction made by a customer 
def edit_trans(trans_var, user_transactions, trans_list, popup):
    popup.destroy()

    selected_display = trans_var.get() #retrieves the selected transaction that was selected in the drop down and splits it back into the stock item and the  date 
    release_name, date = parse_transaction_display(selected_display)
    trans_to_edit = None
    for transaction in user_transactions:
        if transaction["release_name"] == release_name and transaction["date"] == date:
            trans_to_edit = transaction
            break
    if not trans_to_edit:
        messagebox.showerror("Error", "Selected transaction not found.") #provides an error popup if the transaction cannot be retrieved 
        return
    #creates the GUI to allow the date to be edited of the transaction selected, with the geometry, title and colour defined below
    edit_root = tk.Tk()
    edit_root.geometry('400x250')
    edit_root.title('Edit Transaction')
    edit_root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(edit_root, text='Edit Transaction', font=('Arial', 15), fg='white', bg='black')
    label.place(x=80, y=10, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelDate = tk.Label(edit_root, text="Transaction Date (nn/nn/nn)", fg='white', bg='black')
    labelDate.place(x=80, y=60, width=250, height=50)
    entryDate = tk.Entry(edit_root, bg='grey', fg='white')
    entryDate.insert(tk.END, trans_to_edit["date"])
    entryDate.place(x=80, y=100, width=250, height=50)

    #creates a button used on the page, which is used to execute the save_transaction_changes command, also including its colour scheme, font, text size and also its coordinates and dimensions  
    buttonSave = tk.Button(edit_root, text="Save Changes", command=lambda: save_transaction_changes(trans_to_edit, entryDate, trans_list, edit_root), bg='purple', fg='white')
    buttonSave.place(x=80, y=150, width=250, height=50)

    edit_root.mainloop()
#defines teh function to overwrite the old transaction details with the new edited ones 
def save_transaction_changes(transaction, entryDate, trans_list, root):
    new_date = entryDate.get()

    if not re.match(r"^\d{2}/\d{2}/\d{2}$", new_date): #validates the new date entered still follows nn/nn/nn format 
        messagebox.showerror("Validation Error", "Invalid date format. Please use nn/nn/nn.") #provides an error popup if it does not meet validation 
        return
    transaction["date"] = new_date
    try:
        with open("the_trans.pkl", 'wb') as file:
            pickle.dump(trans_list, file)
        messagebox.showinfo("Success", "Transaction date updated successfully!") #opens a success popup if the new date is saved successfully 
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}") # opens an error poup if the date does not save successfully 

#this allows the deletion of the selected transaction made by the user 
def delete_transaction(trans_var, user_transactions, trans_list, popup):
    selected_display = trans_var.get()
    release_name, date = parse_transaction_display(selected_display)

    
    trans_list = [trans for trans in trans_list if not (trans["release_name"] == release_name and trans["date"] == date)]
    try:
        with open("the_trans.pkl", 'wb') as file:
            pickle.dump(trans_list, file)
        messagebox.showinfo("Success", f"Transaction for '{release_name}' on {date} deleted successfully!")
        popup.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# this splits the selected transaction + date from the select transaction page so that it can be extracted as two separate pieces of data 
def parse_transaction_display(display):
    release_name, date = display.rsplit(" (", 1)
    date = date.rstrip(")")
    return release_name, date

#def uth_search or user transaction history search is basically reusing the code from add_trans and ed_trans so that it can allow you to select a customer username and the retrieve all of their transactions onto one popup page    
def uth_search():
    try:
        with open("the_trans.pkl", 'rb') as file:
            trans_list = pickle.load(file)
        trans_users = list(set(trans["customer_username"] for trans in trans_list)) #finds all customer usrnames that have made a transaction so that they can be used in the drop down
    except FileNotFoundError:
        trans_list = []
        trans_users = []

    if not trans_users:
        messagebox.showerror("Error", "No transactions found!") # error if no transactions are found on system
        return
    #creates the page to search user transaction history, with the geometry, title and colour defined below
    root = tk.Tk()
    root.geometry('500x350')
    root.title("Search Transaction History")
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included  
    label = tk.Label(root, text="Search Transaction History", font=('Arial', 15), fg='white', bg='black')
    label.place(x=125, y=10, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    labelUT = tk.Label(root, text="Select User", fg='white', bg='black')
    labelUT.place(x=125, y=50, width=250, height=50)

    #creates the drop down to select the customer account you want to see the transaction history of
    user_var = tk.StringVar(root)
    user_var.set(trans_users[0])  
    user_menu = tk.OptionMenu(root, user_var, *trans_users)
    user_menu.config(bg='purple', fg='white')
    user_menu.place(x=125, y=90, width=250, height=50)

    #creates a button used on the page, which is used to execute the user_trans_p command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonSearch = tk.Button(root, text="Search", command=lambda: user_trans_p(user_var.get(), trans_list, root), bg='purple', fg='white')
    buttonSearch.place(x=125, y=150, width=250, height=50)

    root.mainloop()

#defines the function to collect all transactions made by a customer and then shows them on a popup
def user_trans_p(selected_user, trans_list, root):
    user_transactions = [trans for trans in trans_list if trans["customer_username"] == selected_user]
    if not user_transactions:
        messagebox.showerror("Error", "No transactions found for this user.") #opens a negative popup if there is no transactions made by the selected user 
        return

    #creates the page to show a users transaction history, with the geometry, title and colour defined below
    popup = tk.Toplevel(root)
    popup.title(f"Transactions for {selected_user}")
    popup.geometry('500x400')
    popup.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(popup, text=f"Transactions for {selected_user}", font=('Arial', 15), fg='white', bg='black')
    label.pack()

    for trans in user_transactions:
        transaction_info = f"Stock: {trans['release_name']}, Date: {trans['date']}" #this pastes in all the transactions made by the account 
        label_trans = tk.Label(popup, text=transaction_info, fg='white', bg='black')
        label_trans.pack()

    popup.mainloop()

#creates the interface to add a new staff account into the 'the_staff.pkl', with the geometry, title and colour defined below
def a_staff_page():
    root = tk.Tk()
    root.title('Add Staff Account')
    root.geometry('500x450')
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text='Add Staff Account', font=('Arial', 15), fg='white', bg='black')
    label.pack()

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included  
    labelU = tk.Label(root, text="Username", fg='white', bg='black')
    labelU.place(x=50, y=50, width=150, height=50)
    entryU = tk.Entry(root, bg='gray', fg='white')
    entryU.place(x=160, y=50, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelP1 = tk.Label(root, text="Password", fg='white', bg='black')
    labelP1.place(x=50, y=110, width=150, height=50)
    entryP1 = tk.Entry(root, bg='gray', fg='white')
    entryP1.place(x=160, y=110, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelP2 = tk.Label(root, text="Password Repeat", fg='white', bg='black')
    labelP2.place(x=35, y=170, width=150, height=50)
    entryP2 = tk.Entry(root, bg='gray', fg='white')
    entryP2.place(x=160, y=170, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelp = tk.Label(root, text="Phone Number", fg='white', bg='black')
    labelp.place(x=40, y=230, width=150, height=50)
    entryp = tk.Entry(root, bg='gray', fg='white')
    entryp.place(x=160, y=230, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelAdr = tk.Label(root, text="Address", fg='white', bg='black')
    labelAdr.place(x=50, y=290, width=150, height=50)
    entryAdr = tk.Entry(root, bg='gray', fg='white')
    entryAdr.place(x=160, y=290, width=250, height=50)

    #creates a button used on the page, which is used to execute the save_staff command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonok = tk.Button(root, text="Add Staff Account", command=lambda: save_staff(root, entryp, entryU, entryP1, entryP2, entryAdr), bg='purple', fg='white')
    buttonok.place(x=200, y=350, width=150, height=50)

    root.mainloop()

#defines the function that adds staff into the_staff pkl file 
def save_staff(root, entryp, entryU, entryP1, entryP2, entryAdr):
    username = entryU.get()
    password1 = entryP1.get()
    password2 = entryP2.get()
    phone = entryp.get()
    address = entryAdr.get()

    if not username or not password1 or not password2 or not phone or not address: #verifies all entry boxes are filled and not empty
        messagebox.showerror("Error", "All fields must be filled!") #provides a negative popup if there are missing fields
        return
    if password1 != password2: #makes sure both passwords match 
        messagebox.showerror("Error", "Passwords do not match!") #if both passwords do not match, provides negative popup
        return
    if not (phone.isdigit() and len(phone) == 11): #validates phone numbers are 11 digits and only numbers 
        messagebox.showerror("Error", "Enter a valid phone number!") #negative popup if phone number fails validation 
        return

    new_staff = Staff(username, password1, phone, address) #creates the new staff list, so that it can be added to the_staff pkl file
    try:
        with open("the_staff.pkl", 'rb') as file:
            staff_list = pickle.load(file)
    except FileNotFoundError:
        staff_list = []

    for staff in staff_list:
        if staff.username == username:
            staff.password = password1
            staff.phone = phone
            staff.address = address
            messagebox.showinfo("Duplicate Account", "Staff account already exists!") #popup shows if the account details already exists in the system 
            root.destroy()
            return  

    staff_list.append(new_staff)

    with open("the_staff.pkl", 'wb') as file:
        pickle.dump(staff_list, file)

    messagebox.showinfo("Success", "Staff account added successfully!") #popup shows once the new staff has been added successfully to the_staff.pkl
    root.destroy()

    
# defines the page for the edit / delete staff page.
#contains the functions delete_the_user, edit_the_user and save_edits
# delete_the_user is used to delete a staff account
#edit_the_user is used to edit the details of the user
#save_edits is paired with edit_the_user so that the edited details can overwrite the existing ones in 'the_staff.pkl'
def ed_staff_page():

    with open("the_staff.pkl", 'rb') as file: #loads all staff usernames for the drop down used to edit or delete a staff account 
        staff_users = pickle.load(file)
    staff_names = []
    for i in range(len(staff_users)):
        staff_names.append(staff_users[i].username)

    #creates the page to manage staff, with the geometry, title and colour defined below
    root = tk.Tk()
    root.geometry('400x350')
    root.title('Manage Staff')
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text='Manage Staff Account', font=('Arial', 15), fg='white', bg='black')
    label.pack()

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    labelU = tk.Label(root, text="Username", fg='white', bg='black')
    labelU.place(x=120, y=40, width=150, height=40)

    #creates the drop down to select the staff account you want to manage
    staff_list = tk.StringVar(root)
    staff_list.set(staff_names[0])
    staffopt = tk.OptionMenu(root, staff_list, *staff_names)
    staffopt.config(bg='purple', fg='white', activebackground='purple', activeforeground='white')
    staffopt.place(x=75, y=70, width=250, height=50)

    #creates a button used on the page, which is used to execute the edit_the_user command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonE = tk.Button(root, text="Edit Staff Account", command=lambda: edit_the_user(staff_list, root), bg='purple', fg='white')
    buttonE.place(x=80, y=150, width=120, height=45)

    #creates a button used on the page, which is used to execute the delete_the_user command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonD = tk.Button(root, text="Delete Staff Account", command=lambda: delete_the_user(staff_list, root), bg='purple', fg='white')
    buttonD.place(x=200, y=150, width=120, height=45)

    root.mainloop()

#defines the function used to delete a staff account when the delete button is clicked on the manage staff page
def delete_the_user(staff_list, root):

        staff = staff_list.get()                    #this selects the username selected in manage staff, then finds it in the pkl file and checks it matches,
        with open("the_staff.pkl", 'rb') as file:   #then removes it from the main list and then overwites the pkl file data to exclude it
            staff_users = pickle.load(file)  
        for i in range(len(staff_users)):
            if staff_users[i].username == staff:
                temp = i
        staff_users.pop(temp)
        with open('the_staff.pkl', 'wb') as file:
            pickle.dump(staff_users, file)
        messagebox.showinfo("Success", "Staff account deleted successfully!") #success popup to state the account has been deleted successfully 
        root.destroy()
        
#defines the function that selects the staff details from the pkl file and inputs them into a popup to be edited, with the geometry, title and colour defined below      
def edit_the_user(staff_list, root):
    root.destroy()
    root_staff = tk.Tk()
    root_staff.geometry('500x550')
    root_staff.title('Edit Staff Details')
    root_staff.configure(bg='black')
    
    staff = staff_list.get()
    with open("the_staff.pkl", 'rb') as file:
        staff_users = pickle.load(file) #loads that staff accounts details 

    for i in range(len(staff_users)):
        if staff_users[i].username == staff:

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            label = tk.Label(root_staff, text='Enter the New Details', font=('Arial', 15), fg='white', bg='black')
            label.place(x=130, y=5, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelU1 = tk.Label(root_staff, text="Username", fg='white', bg='black')
            labelU1.place(x=130, y=40, width=250, height=50)
            entryU1 = tk.Entry(root_staff, bg='grey', fg='white')
            entryU1.insert(tk.END, staff_users[i].username)
            entryU1.place(x=130, y=90, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelP1 = tk.Label(root_staff, text="Password", fg='white', bg='black')
            labelP1.place(x=130, y=140, width=250, height=50)
            entryP1 = tk.Entry(root_staff, bg='grey', fg='white')
            entryP1.insert(tk.END, staff_users[i].password)
            entryP1.place(x=130, y=190, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelp = tk.Label(root_staff, text="Phone Number", fg='white', bg='black')
            labelp.place(x=130, y=250, width=250, height=50)
            entryp = tk.Entry(root_staff, bg='grey', fg='white')
            entryp.insert(tk.END, staff_users[i].phone)
            entryp.place(x=130, y=300, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelAdr = tk.Label(root_staff, text="Address", fg='white', bg='black')
            labelAdr.place(x=130, y=350, width=250, height=50)
            entryAdr = tk.Entry(root_staff, bg='grey', fg='white') 
            entryAdr.insert(tk.END, staff_users[i].address)
            entryAdr.place(x=130, y=400, width=250, height=50)

            #creates a button used on the page, which is used to execute the save_edits command, also including its colour scheme, font, text size and also its coordinates and dimensions
            buttonSave = tk.Button(root_staff, text="Save", command=lambda: save_edits(entryU1, entryP1, entryp, entryAdr, root_staff), bg='purple', fg='white')
            buttonSave.place(x=130, y=470, width=250, height=50)

    root_staff.mainloop()
#defines the function that overwites the specific staff accounts details with the new ones entered into the edit staff page
def save_edits(entryU1, entryP1, entryp, entryAdr, root_staff):

    username = entryU1.get()
    pass1 = entryP1.get()
    phone = entryp.get()
    address = entryAdr.get()
    root_staff.destroy()

    if not username or not pass1 or not phone or not address: #verifies that all text entry boxes are filled and not empty
        messagebox.showerror("Error", "All fields must be filled!") #negative popup if validation fails 
        return
    if not (phone.isdigit() and len(phone) == 11): #validates that the phone number is 11 digits and only numbers 
        messagebox.showerror("Error", "Enter a valid phone number!") #negative popup if validation fails
        return
    with open('the_staff.pkl', 'rb') as file:
                    staff_list = pickle.load(file) #loads the old information and overwites it with the newly entered and validated one
    for i in range(len(staff_list)):
        if staff_list[i].username == username:
            staff_list[i].password = pass1
            staff_list[i].phone = phone
            staff_list[i].address = address
    with open('the_staff.pkl', 'wb') as file:
            pickle.dump(staff_list, file)
            messagebox.showinfo("Success", "New staff details saved successfully!") #positive popup if details are saved successfully 

#creates the interface to add a new customer account into the 'the_customer.pkl', with the geometry, title and colour defined below
def a_customer_page():
    root = tk.Tk()
    root.title('Add Customer Account')
    root.geometry('500x450')
    root.configure(bg='black') 

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text='Add Customer Account', font=('Arial', 15), fg='white', bg='black')
    label.pack()

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelU = tk.Label(root, text="Username", fg='white', bg='black')
    labelU.place(x=50, y=50, width=150, height=50)
    entryU = tk.Entry(root, bg='grey', fg='white')
    entryU.place(x=160, y=50, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelP1 = tk.Label(root, text="Password", fg='white', bg='black')
    labelP1.place(x=50, y=110, width=150, height=50)
    entryP1 = tk.Entry(root, bg='grey', fg='white') 
    entryP1.place(x=160, y=110, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelP2 = tk.Label(root, text="Password Repeat", fg='white', bg='black')
    labelP2.place(x=35, y=170, width=150, height=50)
    entryP2 = tk.Entry(root, bg='grey', fg='white') 
    entryP2.place(x=160, y=170, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelp = tk.Label(root, text="Phone Number", fg='white', bg='black')
    labelp.place(x=40, y=230, width=150, height=50)
    entryp = tk.Entry(root, bg='grey', fg='white') 
    entryp.place(x=160, y=230, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelAdr = tk.Label(root, text="Address", fg='white', bg='black')
    labelAdr.place(x=50, y=290, width=150, height=50)
    entryAdr = tk.Entry(root, bg='grey', fg='white')  
    entryAdr.place(x=160, y=290, width=250, height=50)

    #creates a button used on the page, which is used to execute the save_customer command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonok = tk.Button(root, text="Save", command=lambda: save_customer(root, entryp, entryU, entryP1, entryP2, entryAdr), bg='purple', fg='white')
    buttonok.place(x=200, y=350, width=150, height=50)
    root.mainloop()


#defines the function that adds customers into the_customer pkl file 
def save_customer(root, entryp, entryU, entryP1, entryP2, entryAdr):
    username = entryU.get()
    password1 = entryP1.get()
    password2 = entryP2.get()
    phone = entryp.get()
    address = entryAdr.get()

    if not username or not password1 or not password2 or not phone or not address: #validates all entry boxes are filled and not empty 
        messagebox.showerror("Error", "All fields must be filled!") #negative popup if validation fails 
        return

    if password1 != password2: #validates both entered passwords match 
        messagebox.showerror("Error", "Passwords do not match!") #negative popup if validation fails
        return

    if not (phone.isdigit() and len(phone) == 11): #validates phone number is 11 digits and only numbers 
        messagebox.showerror("Error", "Enter a valid phone number!") #negative popup if validation fails
        return

    new_customer = Customer(username, password1, phone, address) #creates the new customer list, so that it can be added to the_customer pkl file
    try:
        with open("the_customer.pkl", 'rb') as file:
            customer_list = pickle.load(file)
    except FileNotFoundError:
        customer_list = []

    for customer in customer_list:
        if customer.username == username:
            customer.password = password1
            customer.phone = phone
            customer.address = address
            messagebox.showinfo("Duplicate Account", "Customer account already exists!") #popup shows if the account details already exists in the system
            root.destroy
            return
    
    customer_list.append(new_customer)

    with open("the_customer.pkl", 'wb') as file:
        pickle.dump(customer_list, file)

    messagebox.showinfo("Success", "Customer account added successfully!") #popup shows once the new customer has been added successfully to the_customer.pkl
    root.destroy()

# defines the page for the edit / delete customer page.
#contains the functions delete_the_user2, edit_the_user2 and save_edits2
# delete_the_user2 is used to delete a customer account
#edit_the_user2 is used to edit the details of the user
#save_edits2 is paired with edit_the_user2 so that the edited details can overwrite the existing ones in 'the_customer.pkl'
def ed_customer_page():
    
    with open("the_customer.pkl", 'rb') as file: #loads all customer usernames for the drop down used to edit or delete a customer account
        customer_users = pickle.load(file)
    customer_names = [customer.username for customer in customer_users]

    #creates the page to manage customer, with the geometry, title and colour defined below
    root = tk.Tk()
    root.geometry('400x300')
    root.title('Manage Customers')
    root.configure(bg='black') 

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text='Manage Customer Account', font=('Arial',15), fg='white', bg='black')
    label.pack()

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    labelU = tk.Label(root, text="Username", fg='white', bg='black')
    labelU.place(x=120, y=40, width=150, height=40)

    #creates the drop down to select the customer account you want to manage
    customer_list = tk.StringVar(root)
    customer_list.set(customer_names[0])
    customeropt = tk.OptionMenu(root, customer_list, *customer_names)
    customeropt.place(x=65, y=70, width=280, height=50)
    customeropt.configure(bg='purple', fg='white')

    #creates a button used on the page, which is used to execute the edit_the_user2 command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonE = tk.Button(root, text="Edit Customer Account", command=lambda: edit_the_user2(customer_list, root), bg='purple', fg='white')
    buttonE.place(x=65, y=150, width=140, height=45)

    #creates a button used on the page, which is used to execute the delete_the_user2 command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonD = tk.Button(root, text="Delete Customer Account", command=lambda: delete_the_user2(customer_list, root), bg='purple', fg='white')
    buttonD.place(x=205, y=150, width=140, height=45)

    root.mainloop()

#defines the function used to delete a customer account when the delete button is clicked on the manage customer page
def delete_the_user2(customer_list, root):
    customer = customer_list.get()                  #this selects the username selected in manage customer, then finds it in the pkl file and checks it matches,
    with open("the_customer.pkl", 'rb') as file:    #then removes it from the main list and then overwites the pkl file data to exclude it
        customer_users = pickle.load(file)
    customer_users = [cust for cust in customer_users if cust.username != customer]
    with open("the_customer.pkl", 'wb') as file:
        pickle.dump(customer_users, file)
    messagebox.showinfo("Success", "Customer account deleted successfully!") #success popup to state the account has been deleted successfully
    root.destroy()

#defines the function that selects the customer details from the pkl file and inputs them into a popup to be edited, with the geometry, title and colour defined below      
def edit_the_user2(customer_list, root):
    root.destroy()
    root_customer = tk.Tk()
    root_customer.geometry('500x550')
    root_customer.title('Edit Customer Details')
    root_customer.configure(bg='black')

    customer = customer_list.get()
    with open("the_customer.pkl", 'rb') as file:
        customer_users = pickle.load(file) #loads that staff accounts details 

    for i in range(len(customer_users)):
        if customer_users[i].username == customer:
            customer_to_edit = customer_users[i]

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            label = tk.Label(root_customer, text='Enter the New Details', font=('Arial', 15), fg='white', bg='black')
            label.place(x=130, y=5, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelU1 = tk.Label(root_customer, text="Username", fg='white', bg='black')
            labelU1.place(x=130, y=40, width=250, height=50)
            entryU1 = tk.Entry(root_customer, bg='grey', fg='white')
            entryU1.insert(tk.END, customer_to_edit.username)
            entryU1.place(x=130, y=90, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelP1 = tk.Label(root_customer, text="Password", fg='white', bg='black')
            labelP1.place(x=130, y=140, width=250, height=50)
            entryP1 = tk.Entry(root_customer, bg='grey', fg='white') 
            entryP1.insert(tk.END, customer_to_edit.password)
            entryP1.place(x=130, y=190, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelp = tk.Label(root_customer, text="Phone Number", fg='white', bg='black')
            labelp.place(x=130, y=250, width=250, height=50)
            entryp = tk.Entry(root_customer, bg='grey', fg='white') 
            entryp.insert(tk.END, customer_to_edit.phone)
            entryp.place(x=130, y=300, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelAdr = tk.Label(root_customer, text="Address", fg='white', bg='black')
            labelAdr.place(x=130, y=350, width=250, height=50)
            entryAdr = tk.Entry(root_customer, bg='grey', fg='white') 
            entryAdr.insert(tk.END, customer_to_edit.address)
            entryAdr.place(x=130, y=400, width=250, height=50)

            #creates a button used on the page, which is used to execute the save_edits2 command, also including its colour scheme, font, text size and also its coordinates and dimensions
            buttonSave = tk.Button(root_customer, text="Save", command=lambda: save_edits2(entryU1, entryP1, entryp, entryAdr, root_customer), bg='purple', fg='white')
            buttonSave.place(x=130, y=470, width=250, height=50)

    root_customer.mainloop()

#defines the function that overwites the specific customer accounts details with the new ones entered into the edit customer page
def save_edits2(entryU1, entryP1, entryp, entryAdr, root_customer):
    username = entryU1.get()
    pass1 = entryP1.get()
    phone = entryp.get()
    address = entryAdr.get()
    root_customer.destroy()

    if not username or not pass1 or not phone or not address: #validates that all entry text boxes are filled and not empty
        messagebox.showerror("Error", "All fields must be filled!") #negative popup if validation fails 
        return
    if not (phone.isdigit() and len(phone) == 11): #validates phone number is 11 digits and only numbers
        messagebox.showerror("Error", "Enter a valid phone number!") #negative popup if validation fails
        return
    with open('the_customer.pkl', 'rb') as file:
        customer_list = pickle.load(file) #loads the old information and overwites it with the newly entered and validated one
    for customer in customer_list:
        if customer.username == username:
            customer.password = pass1
            customer.phone = phone
            customer.address = address
            break
    with open('the_customer.pkl', 'wb') as file:
        pickle.dump(customer_list, file)
        messagebox.showinfo("Success", "New customer details saved successfully!") #positive popup if details are saved successfully

#creates the interface to add a new stock item into the 'the_stock.pkl', with the geometry, title and colour defined below
def a_stock_page():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Add Stock')
    root.configure(bg='black')

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    label = tk.Label(root, text='Add Stock', font=('Arial', 15), fg='white', bg='black')
    label.pack()

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelRN = tk.Label(root, text="Release Name", fg='white', bg='black')
    labelRN.place(x=40, y=50, width=150, height=50)
    entryRN = tk.Entry(root, bg='grey', fg='white')
    entryRN.place(x=160, y=50, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelPF = tk.Label(root, text="Physical Format", fg='white', bg='black')
    labelPF.place(x=40, y=110, width=150, height=50)
    entryPF = tk.Entry(root, bg='grey', fg='white')
    entryPF.place(x=160, y=110, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelRY = tk.Label(root, text="Release Year", fg='white', bg='black')
    labelRY.place(x=40, y=170, width=150, height=50)
    entryRY = tk.Entry(root, bg='grey', fg='white')
    entryRY.place(x=160, y=170, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelp = tk.Label(root, text="Price", fg='white', bg='black')
    labelp.place(x=40, y=230, width=150, height=50)
    entryp = tk.Entry(root, bg='grey', fg='white')
    entryp.place(x=160, y=230, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelA = tk.Label(root, text="Artist", fg='white', bg='black')
    labelA.place(x=40, y=290, width=150, height=50)
    entryA = tk.Entry(root, bg='grey', fg='white')
    entryA.place(x=160, y=290, width=250, height=50)

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    labelS = tk.Label(root, text="Stock Amount", fg='white', bg='black')
    labelS.place(x=40, y=350, width=150, height=50)
    entryS = tk.Entry(root, bg='grey', fg='white')
    entryS.place(x=160, y=350, width=250, height=50)

    #creates a button used on the page, which is used to execute the save_stock command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonok = tk.Button(root, text="Add Stock", command=lambda: save_stock(root, entryRN, entryPF, entryRY, entryp, entryA, entryS), bg='purple', fg='white')
    buttonok.place(x=200, y=410, width=150, height=50)

    root.mainloop()

#defines the function that adds stock items into the_stock pkl file 
def save_stock (root, entryRN, entryPF, entryRY, entryp, entryA, entryS):
    release_name = entryRN.get()
    pformat = entryPF.get()
    release_year = entryRY.get()
    price = entryp.get()
    artist = entryA.get()
    stock_number = entryS.get() 
    root.destroy()
    
    if not release_name or not release_year or not price or not artist or not pformat: #validates all entry boxes are filled and not empty 
        messagebox.showerror("Input Error", "Please fill all fields") #negative popup if validation fails 
        return

    if not (release_year.isdigit() and len(release_year) == 4): #validates the release year is 4 characters long and only numbers 
        messagebox.showerror("Error", "Enter a valid release year!") #negative popup if validation fails 
        return

    try:
        try:
            with open('the_stock.pkl', 'rb') as file:
                stock_list = pickle.load(file) #creates the new stock list, so that it can be added to the_stock pkl file
        except (FileNotFoundError, EOFError):
            stock_list = []  
        for stock in stock_list:
            if stock.release_name == release_name and stock.release_year == release_year and stock.pformat == pformat and stock.artist == artist:
                messagebox.showinfo("Duplicate Entry", "Stock already exists") #negative popup if the stock already exists in the system
                return
        new_stock = Stock(release_name, pformat, release_year, price, artist, stock_number)
        stock_list.append(new_stock)
        with open('the_stock.pkl', 'wb') as file:
            pickle.dump(stock_list, file)
            messagebox.showinfo("Success", "Stock added successfully!") #popup shows once the new stock has been added successfully to the_stock.pkl

    except Exception as e:
        messagebox.showerror('Error', 'This Item Already Exists')
   
# defines the page for the edit / delete stock page.
#contains the functions delete_the_user3, edit_the_user3 and save_edits3
# delete_the_user3 is used to delete a stock item
#edit_the_user3 is used to edit the details of the stock
#save_edits3 is paired with edit_the_user3 so that the edited details can overwrite the existing ones in 'the_stock.pkl'

def ed_stock_page():
    with open("the_stock.pkl", 'rb') as file:
        stock_users = pickle.load(file)
    stock_names = [f"{stock.release_name} ({stock.pformat})" for stock in stock_users] #makes the drop down stock names include the pformat 

    root = tk.Tk()
    root.geometry('400x300')
    root.title('Manage Stock')
    root.configure(bg='black')

    #creates the page to manage customer, with the geometry, title and colour defined below
    label = tk.Label(root, text='Manage Stock', font=('Arial', 15), fg='white', bg='black')
    label.pack()

    #creates the page to manage customer, with the geometry, title and colour defined below
    labelU = tk.Label(root, text="Release Name", fg='white', bg='black')
    labelU.place(x=120, y=40, width=150, height=40)

    #creates the drop down to select the stock you want to manage
    stock_list = tk.StringVar(root)
    stock_list.set(stock_names[0])
    stockopt = tk.OptionMenu(root, stock_list, *stock_names)
    stockopt.config(bg='purple', fg='white') 
    stockopt.place(x=65, y=70, width=280, height=50)

    #creates a button used on the page, which is used to execute the edit_the_user3 command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonE = tk.Button(root, text="Edit Stock", command=lambda: edit_the_user3(stock_list, root), bg='purple', fg='white')
    buttonE.place(x=65, y=150, width=140, height=45)

    #creates a button used on the page, which is used to execute the delete_the_user3 command, also including its colour scheme, font, text size and also its coordinates and dimensions
    buttonD = tk.Button(root, text="Delete Stock", command=lambda: delete_the_user3(stock_list, root), bg='purple', fg='white')
    buttonD.place(x=205, y=150, width=140, height=45)
    
    root.mainloop()

#defines the function used to delete a stock item when the delete button is clicked on the manage stock page
def delete_the_user3(stock_list, root):
    stock = stock_list.get()
    with open("the_stock.pkl", 'rb') as file:
        stock_users = pickle.load(file)
    
    
    release_name = stock.split(" (")[0] #used to split the release name and pformat so that it can be used to find and delete the stock item selected 
    
    temp = None
    for i in range(len(stock_users)):
        if stock_users[i].release_name == release_name:  #follows the same form of deletion as delete_the_user and delete_the_user2
            temp = i                                     # inputs the pkl file list and cuts out the selected stock, then
            break  
    
    if temp is not None:
        stock_users.pop(temp)
        with open('the_stock.pkl', 'wb') as file:
            pickle.dump(stock_users, file)
        messagebox.showinfo("Success", "Stock deleted successfully!") #success popup to state the account has been deleted successfully
    root.destroy()

#defines the function that selects the stock details from the pkl file and inputs them into a popup to be edited, with the geometry, title and colour defined below
def edit_the_user3(stock_list, root):
    root.destroy()
    root_stock = tk.Tk()
    root_stock.geometry('500x750')
    root_stock.title('Edit the Stock')
    root_stock.configure(bg='black') 

    stock = stock_list.get()
    with open("the_stock.pkl", 'rb') as file:
        stock_users = pickle.load(file) #loads that stock items details


    stocknamewithoutpformat = stock.split(" (")[0] #used to split the release name and pformat so that it can be used to find and edit the stock item selected

    for i in range(len(stock_users)):
        if stock_users[i].release_name == stocknamewithoutpformat:
            stock_to_edit = stock_users[i]

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            label = tk.Label(root_stock, text='Enter the New Details', font=('Arial', 15), fg='white', bg='black')
            label.place(x=130, y=5, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelRN1 = tk.Label(root_stock, text="Release Name", fg='white', bg='black')
            labelRN1.place(x=130, y=40, width=250, height=50)
            entryRN1 = tk.Entry(root_stock, bg='grey', fg='white')  
            entryRN1.insert(tk.END, stock_to_edit.release_name)
            entryRN1.place(x=130, y=90, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelPF1 = tk.Label(root_stock, text="Physical Format", fg='white', bg='black')
            labelPF1.place(x=130, y=140, width=250, height=50)
            entryPF1 = tk.Entry(root_stock, bg='grey', fg='white') 
            entryPF1.insert(tk.END, stock_to_edit.pformat)
            entryPF1.place(x=130, y=190, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelRY1 = tk.Label(root_stock, text="Release Year", fg='white', bg='black')
            labelRY1.place(x=130, y=250, width=250, height=50)
            entryRY1 = tk.Entry(root_stock, bg='grey', fg='white')  
            entryRY1.insert(tk.END, stock_to_edit.release_year)
            entryRY1.place(x=130, y=300, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelP = tk.Label(root_stock, text="Price", fg='white', bg='black')
            labelP.place(x=130, y=350, width=250, height=50)
            entryP = tk.Entry(root_stock, bg='grey', fg='white') 
            entryP.insert(tk.END, stock_to_edit.price)
            entryP.place(x=130, y=400, width=250, height=50)

            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelA1 = tk.Label(root_stock, text="Artist", fg='white', bg='black')
            labelA1.place(x=130, y=450, width=250, height=50)
            entryA1 = tk.Entry(root_stock, bg='grey', fg='white') 
            entryA1.insert(tk.END, stock_to_edit.artist)
            entryA1.place(x=130, y=500, width=250, height=50)
            #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
            #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
            labelSN = tk.Label(root_stock, text="Stock Number", fg='white', bg='black')
            labelSN.place(x=130, y=550, width=250, height=50)
            entrySN = tk.Entry(root_stock, bg='grey', fg='white') 
            entrySN.insert(tk.END, stock_to_edit.stockid)
            entrySN.place(x=130, y=600, width=250, height=50)

            #creates a button used on the page, which is used to execute the save_edits3 command, also including its colour scheme, font, text size and also its coordinates and dimensions
            buttonSave = tk.Button(root_stock, text="Save", command=lambda: save_edits3(entryRN1, entryPF1, entryRY1, entryP, entryA1, entrySN, stock_users, root_stock), bg='purple', fg='white')
            buttonSave.place(x=130, y=670, width=250, height=50)

            root_stock.mainloop()

#defines the function that overwites the specific stock items details with the new ones entered into the edit stock page
def save_edits3(entryRN1, entryPF1, entryRY1, entryP, entryA1, entrySN, stock_users, root_stock):
    release_name = entryRN1.get()
    pformat = entryPF1.get()
    release_year = entryRY1.get()
    price = entryP.get()
    artist = entryA1.get()
    stock_number = entrySN.get()

   
    if not release_name or not pformat or not release_year or not price or not artist or not stock_number: #validates all text entry boxes are filled and not empty
        messagebox.showerror("Error", "All fields must be filled.") #negative popup if validation fails 
        return
    if not (release_year.isdigit() and len(release_year) == 4): #validates release year is 4 characters long and only numbers 
        messagebox.showerror("Error", "Enter a valid release year!") #negative popup if validation fails
        return
    for stock in stock_users:
        if stock.release_name == release_name:
            stock.pformat = pformat
            stock.release_year = release_year
            stock.price = price
            stock.artist = artist
            stock.stockid = stock_number
    with open('the_stock.pkl', 'wb') as file:

        pickle.dump(stock_users, file)
        messagebox.showinfo("Success", "New stock details saved successfully!") #positive popup if details are saved successfully

    root_stock.destroy()

#defines the function that holds the page to search for stock, with the geometry, title and colour defined below
def ss_page():
    
    with open("the_stock.pkl", 'rb') as file:
        stock_users = pickle.load(file)
    #creates the GUI that allows you to search for the stock by release name 
    root = tk.Tk()
    root.title("Stock Search")
    root.geometry('400x300')
    root.configure(bg='black')  

    #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
    labelSS = tk.Label(root, text="Enter Release Name to Search:", font=('Arial', 15), fg='white', bg='black')
    labelSS.pack()

    #creates an entry box used on the page, with the co-ordinates, font, text size and dimensions included
    entry_release_name = tk.Entry(root, bg='grey', fg='white') 
    entry_release_name.place(x=80, y=50, width=250, height=50)

    #defines the function that retrieves every stock item that matches the entered text on the ss_page
    def search_stock():
        release_name = entry_release_name.get().lower()
        results = []
        for stock in stock_users:
            if release_name in stock.release_name.lower():
                results.append(f"{stock.release_name} by {stock.artist} ({stock.pformat})") #formats the results found to be release name by artist (pformat)
        if not results:
            results.append("No stocks found matching the entered release name.") #negative popup if no results are found 

        #creates the results page, with the geometry, title and colour defined below
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.geometry("400x450")
        result_window.configure(bg='black')

        #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
        label = tk.Label(result_window, text="Matching Results:", font=('Arial', 15), fg='white', bg='black')
        label.place(x=20, y=10)

        #creates a label used on the page, with the co-ordinates, font, text size and dimensions included
        result_label = tk.Label(result_window, text="\n".join(results), wraplength=350, justify="left", fg='white', bg='black')
        result_label.place(x=20, y=50, width=360, height=380)

    #creates a button used on the page, which is used to execute the search_stock command, also including its colour scheme, font, text size and also its coordinates and dimensions
    button_search = tk.Button(root, text="Search", command=search_stock, bg='purple', fg='white')
    button_search.place(x=80, y=120, width=250, height=50)

    root.mainloop()

login()



