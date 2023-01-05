#Declare constants
price_per_night = 45.00
breakfast_price = 8.75
discount1 = 0.05
discount2 = 0.075

def get_name():
    flag = True

    while flag:
        name = input("Please enter your name: ")

        if len(name) < 2 or len(name) > 50:
            print("Sorry, you did not enter a valid name")
            flag = True 
        else:
            for char in name:
                if char.isdigit():
                    print("Sorry, you did not enter a valid name")
                    flag = True
                else:
                    return name
            
def phone_num():
    flag = True

    while flag:
        number = input("Please enter your phone number: ")

        try:
            int(number)
        except:
            print("Sorry, you did not enter a valid number")
            flag = True
        else:
            if len(number) != 11:
                print("Sorry, you did not enter a valid number")
                flag = True
            else:
                for digit in number:
                    if digit.isdigit() == False:
                        print("Sorry, you did not enter a valid name")
                        flag = True
                    else:
                        return number


def get_email():

    flag = True

    while flag:
        email = input("Please enter your email address: ")

        if "@" not in email:
            print("Sorry, you did not enter a email address")
            print("Your email must contain the @ symbol")
            flag = True
        else:
            return email

def hotel_choice():
    print("###############################################")
    print("Please choose the hotel location")
    print("1. London")
    print("2. Manchester")
    print("3. Edinburgh")
    print("###############################################")

    choice = input("Please enter the number of your choice (1-3): ")
    locations = ["London", "Manchester", "Edinburgh"]

    hotel = locations[int(choice)-1]
    return hotel 


def get_arrival_date():
    flag = True
    
    while flag:

        date = input("Please enter the date of arrival (DD/MM/YYYY): ")
  
        if len(date) != 10:
            print("The date has to be in the format DD/MM/YYYY")
            flag = True
        elif not date[:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit():
            print("Incorrect date format entered.")
            flag = True
        elif not date[2] == "/" or not date[5] == "/":
            print("Incorrect date format entered. You must use '/' as the date separator.")
            flag = True
        else:
            return date

def get_stay_length():
    flag = True
    
    while flag:
        nights = input("Please enter the number nights you wish to stay: ")
        
        try:
            int(nights)
        except:
            print("Sorry, you did not enter a valid input")
            flag = True
        else:
            if int(nights) < 1:
                print("Sorry, you did not enter a valid input")
                flag = True
            else:
                return nights 

def get_number_people():
    flag = True
    
    while flag:
        people = input("Please enter the number of people: ")
        
        try:
            int(people)
        except:
            print("Sorry, you did not enter a valid input")
            flag = True
        else:
            if int(people) < 1:
                print("Sorry, you did not enter a valid input")
                flag = True
            else:
                return people

def get_breakfast():
    flag = True
    
    while flag:
        choice = input("Would you like to include breakfast? (Y/N) ").upper()
        
        if choice == "YES" or choice == "Y" or choice == "NO" or choice == "N":
            return choice
        else:
            print("Sorry, you did not enter a valid input")
            flag = True 


#get the personal details
name = get_name()
address = input("PLease enter your address: ")
phone_number = phone_num()
email_add = get_email()


#Get the stay details
location = hotel_choice()
date = get_arrival_date()
number_of_nights =  get_stay_length()
number_people = get_number_people()
breakfast = get_breakfast()


room_cost = (price_per_night * int(number_people)) * int(number_of_nights)

def calculate_breakfast():
    if breakfast == "Yes" or breakfast == "N":
        breakfast_cost = (float(breakfast_price) * int(number_people)) * int(number_of_nights)
    else:
        breakfast_cost = 0.00
    
    return breakfast_cost

breakfast_cost = calculate_breakfast()

subtotal = float(room_cost) + float(breakfast_cost)

def returning_cust():
    flag = True
    
    while flag:
        returning = input("Have you stayed with us before? (Y/N) ").upper()
        
        if returning == "YES" or returning == "Y" or returning == "NO" or returning == "N":
            return returning
        else:
            print("Sorry, you did not enter a valid input")
            flag = True 

returning_customer = returning_cust()

def length_discount():
    if int(number_of_nights) > 10:
        len_discount = "Yes"
        
    else:
        len_discount = "No"
    
    return len_discount

len_discount = length_discount()

def calculate_discount():
    discounts = subtotal

    if returning_customer == "YES" or returning_customer == "Y" and len_discount == "Yes":
        print("Weclome back. A loyalty discount has been applied to your bill")
        print("Also get a discount for staying for 10 nights or more")
        discounts = (discounts * discounts) + (discounts * discounts)
        return discounts
    elif returning_customer == "YES" or returning_customer == "Y" and len_discount == "No":
        print("Weclome back. A loyalty discount has been applied to your bill")
        discounts = (discounts * discount1)
        return discounts
    elif returning_customer == "NO" or returning_customer == "N" and len_discount == "Yes":
        print("You have been given a discount for staying for 10 nights or more")
        discounts = (discounts * discount2)
        return discounts

discount_value = calculate_discount()

totalCost = float(subtotal) - float(discount_value)

#generate screen output
print("Here is a reciept for you records")
print("#########Booking Details##############")
print("Name: ", name)
print("Address: ",  address)
print("Phone Number: ", phone_number)
print ("Email: ",  email_add)
print("Booked Hotel: ", location)
print ("Date of Arrival: ",  date)
print("Number of Nights", number_of_nights )
print("Number of People: ", number_people)
print("Breakfast: ", breakfast)
print("")
print("##############Costs################")
print("Room: £", room_cost)
print("Breakfast: £", breakfast_cost)
print("Return Discount: ", returning_customer)
print("10 Nights or More: ", len_discount)
print("Cost before discounts: £", subtotal)
print('Discounts: -£', discount_value)
print("Total cost of stay: £", totalCost)


#output to text file
with open("reciept.txt", "w") as txt:
    txt.write("Here is a reciept for you records")
    txt.write("#########Booking Details##############")
    txt.write("Name: {}".format(name))
    txt.write("Address: {}".format(address))
    txt.write("Phone Number:{}".format(phone_number))
    txt.write ("Email: {}".format(email_add))
    txt.write("Booked Hotel: {}".format(location))
    txt.write ("Date of Arrival:{}".format(date))
    txt.write("Number of Nights: {}".format(number_of_nights))
    txt.write("Number of People: {}".format(number_people))
    txt.write("Breakfast:{}".format(breakfast))
    txt.write("\n")
    txt.write("##############Costs################")
    txt.write("Room: £ {}".format(room_cost))
    txt.write("Breakfast: £{}".format(breakfast_cost))
    txt.write("Return Discount: {}".format(returning_customer))
    txt.write("10 Nights or More: {}".format(len_discount))
    txt.write("Cost before discounts: £ {}".format(subtotal))
    txt.write("Discounts: -£{}".format(discount_value))
    txt.write("Total cost of stay: £ {}".format(totalCost))   