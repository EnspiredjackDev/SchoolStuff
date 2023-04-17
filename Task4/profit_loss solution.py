import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np


def profit_loss_menu():

    flag = True
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Profit and Loss over a period of time ")
        print("2. Quantity sold by suppliers ")
        print("3. Profit by suppliers ")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 3:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 




def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("5.  Onions")
        print("6.  Apples")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name


def get_supplier_choice():

    flag = True

    while flag:
        
        print("######################################################")
        print("Please choose a supplier form the list:")
        print("Please enter the number of the product (1-5)")
        print("1.  Farm Direct")
        print("2.  Natural Best")
        print("3.  Nature Food")
        print("4.  Grocers Int.")
        print("5.  Clean Living")
        print("######################################################")

        supplier_list = ["Farm Direct", "Natural Best", "Nature Food", "Grocers Int.", "Clean Living"]

        supplier_choice = input("Please enter the number of your choice (1-5): ")

        try:
            int(supplier_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(supplier_choice) < 1 or int(supplier_choice) > 5:
                print("Sorry, you did not eneter a valid choice")
                flag = True
            else:
                supplier_name = supplier_list[int(supplier_choice)-1]
                return supplier_name


def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Plese enter start date for your time range (DD/MM/YYYY):')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(start_date, dayfirst=True)



def get_end_date():
    
    flag = True
    while flag:
        end_date = input('Plese enter end date for your time range (DD/MM/YYYY):')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(end_date, dayfirst=True)



def get_date_range_all():
    df1 = pd.read_csv("Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]

    list_profits=results["Profit subtotal"].tolist();
    list_dates=results["Date"].tolist();
    plt.plot(list_profits, label = "sigmoid value", linestyle="-.")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Profit subtotal")
    plt.show()
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    
    print(results_print)
    print("The overall profit/loss for the selected time frame was £{}".format(total))
    print("")



def get_supplier_profit():
    df1 = pd.read_csv("Task4a_data.csv") 
      
    
    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date)].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    
    df2 = results.groupby('Supplier',as_index =False)['Profit subtotal'].sum()
    list_profits=df2["Profit subtotal"].values.tolist();
    list_suppliers=df2["Supplier"].values.tolist();
    plt.bar(list_suppliers,list_profits)
    plt.legend()
    plt.xlabel("Suppliers")
    plt.ylabel("Profit subtotal")
    plt.show()
    print(df2)
    print("")


def get_supplier_quantity():
    df1 = pd.read_csv("Task4a_data.csv") 
       
    
    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date)].copy()
    
    
    df2 = results.groupby('Supplier',as_index =False)['KGs Sold'].sum()
    list_profits=df2["KGs Sold"].values.tolist();
    list_suppliers=df2["Supplier"].values.tolist();
    plt.bar(list_suppliers,list_profits)
    plt.legend()
    plt.xlabel("Suppliers")
    plt.ylabel("KGs Sold")
    plt.show()
    print(df2)
    print("")
    

def get_date_range_product():
    product_name = get_product_choice()
    df2 = pd.read_csv("Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(product_results["Profit subtotal"])
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))


def process_menu_choice():

    if profit_choice == 1:
        get_date_range_product()
    elif profit_choice == 2:
        get_supplier_quantity()
    elif profit_choice == 3:
        get_supplier_profit()
    else:
        get_date_range_all()


start_date = get_start_date()
end_date = get_end_date()
profit_choice = profit_loss_menu()
process_menu_choice()



