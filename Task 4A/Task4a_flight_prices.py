import pandas as pd
import matplotlib.pyplot as plt

#displays main menu and collects user choice of destination
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("########         Choose a destination          ########")
        print("Alicante (ALC)")
        print("Amsterdam (AMS)")
        print("Athens (ATH)")
        print("Budapest (BUD)")
        print("Cologne (CGN)")
        print("Dublin (DUB)")
        print("Munich (MUC)")
        print("Paris (CDG)")
        print("Rhodes (RHO)")
        print("######################################################")
        print("Or press \'#\' to view trends")

        #collects and validates user input to ensure choice is in the list
        #converts the collected code to full name

        menu_choice = input("Please enter the three letter destination code: ").upper()

        code_list = ["ALC","AMS", "ATH", "BUD", "CGN" ,"DUB", "MUC", "CDG","RHO"]
        airport_list = ["Alicante" ,"Amsterdam", "Athens", "Budapest","Cologne","Dublin","Munich","Paris","Rhodes"]
        
        if menu_choice in code_list:
            airport_postion = code_list.index(menu_choice)
            return airport_list[airport_postion]
        elif menu_choice == "#":
            trends()
            flag = True
        else:
            print("Sorry, you did not enter a valid three letter code")
            flag = True

#collects the month that the user wishes to travel and validates input
def get_date():

    flag = True

    while flag:
        print("######################################################")
        print("When will you be traveling?")
        print("Please enter the number of the month you will be travelling (1-12)")
        print("for example June = 6")
        print("######################################################")

        month_list = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]

        month_choice = input("Please enter the number of your choice (1-12): ")

        try:
            int(month_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(month_choice) < 1 or int(month_choice) > 12:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                travel_date = month_list[int(month_choice)-1]
                return travel_date  

def most_popular_destinations(df):
    popular_destinations = df['Desination'].value_counts().nlargest(5) #in the csv given, "Destination" is spelled incorrectly
    popular_destinations.plot(kind='bar')
    plt.xlabel('Destination')
    plt.ylabel('Number of Flights')
    plt.title('Top 5 Most Popular Destinations')
    plt.show()

def commission_by_month(df):
    df['Commission Earned'] = df['Price'] * df['Commission (%)'] / 100
    commission_by_month = df.groupby('Month')['Commission Earned'].sum()
    commission_by_month.plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Commission Earned')
    plt.title('Commission Earned per Month')
    plt.show()

def flights_by_airline(df):
    airline_count = df['Airline'].value_counts()
    airline_count.plot(kind='bar')
    plt.xlabel('Airline')
    plt.ylabel('Number of Flights')
    plt.title('Number of Flights by Airline')
    plt.show()

def trends():
    flag = True

    while flag:
        # Load data and analyze trends and patterns
        data = pd.read_csv("/home/Jack/test/Task4a_data.csv")
        selec = int(input("Do you want to view: \n 1) Most popular destinations \n 2) Commission by month \n 3) Flights by airline \n"))
        if selec == 1:
            most_popular_destinations(data)
            return
        elif selec == 2:
            commission_by_month(data)
            return
        elif selec == 3:
            flights_by_airline(data)
            return
        else:
            print("You did not give a valid input")
            flag = True

destination = menu()
month = get_date()

#gets the main list of data that matches user search criteia and displays it
def get_data():
    df = pd.read_csv("/home/Jack/test/Task4a_data.csv")
    extract = df.loc[(df['Month'] == month) & (df['Destination'] == destination), df.columns != "Commission (%)"]
    print("We have found these flights that match your criteria:")
    return extract

extracted_data = get_data() 
extract_no_index = extracted_data.to_string(index=False)

#extracts more meaningful data from the results for comparison
def compare_data():
    
    compare_df = extracted_data[['Airline', 'Price']]
   
    column = compare_df['Price']
    max_price = column.max()
    min_price = column.min()
    
    most_expensive = compare_df.loc[(extracted_data['Price']== max_price)]
    least_expensive = compare_df.loc[(extracted_data['Price']== min_price)]
    
    average_price = round(compare_df['Price'].mean(),2)
    
   
    print("###############################################")
    print("The most expensive flights to {} in {} are: ".format(destination, month) )
    print(most_expensive.to_string(index=False))
    print("")
    print("The least expensive flights to {} in {} are: ".format(destination, month) )
    print(least_expensive.to_string(index=False))
    print("")
    print("The average price of a flight to {} in {} is: ".format(destination, month))
    print(average_price)
    print("###############################################")

print(extract_no_index)
compare_data()
