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

        #collects and validates user input to ensure choice is in the list
        #converts the collected code to full name

        menu_choice = input("Please enter the three letter destination code: ").upper()

        code_list = ["ALC","AMS", "ATH", "BUD", "CGN" ,"DUB", "MUC", "CDG","RHO"]
        airport_list = ["Alicante" ,"Amsterdam", "Athens", "Budapest","Cologne","Dublin","Munich","Paris","Rhodes"]
        
        if menu_choice in code_list:
            airport_postion = code_list.index(menu_choice)
            return airport_list[airport_postion]
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

destination = menu()
month = get_date()

#gets the main list of data that matches user search criteia and displays it
def get_data():
    df = pd.read_csv("/home/Jack/Documents/SchoolStuff/Task 4A/Task4a_data.csv")
    extract = df.loc[(df['Month'] == month) & (df['Desination'] == destination), df.columns != "Commission (%)"]
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

def analyze_data(df):
    # Most popular destinations
    popular_destinations = df["Desination"].value_counts().head(5)
    print("Most popular destinations:")
    print(popular_destinations)
    popular_destinations.plot(kind='bar')
    plt.xlabel('Destination')
    plt.ylabel('Number of Flights')
    plt.title('Most Popular Destinations')
    plt.show()

    # Commission earned from sales for different airlines
    df['Commission Earned'] = df['Price'] * (df['Commission (%)'] / 100)
    commission_by_airline = df.groupby('Airline')['Commission Earned'].sum().sort_values(ascending=False)
    print("Commission earned from sales for different airlines:")
    print(commission_by_airline)
    commission_by_airline.plot(kind='bar')
    plt.xlabel('Airline')
    plt.ylabel('Commission Earned')
    plt.title('Commission Earned by Airlines')
    plt.show()


print(extract_no_index)
compare_data()

df = pd.read_csv("Task4a_data.csv")
analyze_data(df)



