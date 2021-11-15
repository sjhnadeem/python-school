# Lists for the 3 types of data
components = ['Processor', 'RAM', 'Storage', 'Screen Size', 'Tower Type', 'Number of ports']
component_names = ['p3','p5','p7','16GB','32GB','1TB','2TB','19"','23"','Mini Tower', 'Midi Tower', '2 ports', '4 ports']

item_prices = [100,120,200,75,150,50,100,65,120,40,70,10,20]
# Made up list of stock levels for each product
original_stock_level = [12,23,0,12,43,21,3,1,4,7,9,3,2]
stock_level = [12,23,0,12,43,21,3,1,4,7,9,3,2]

# Task 3:
num_order = 0
todays_total = 0

# Find today's date:
import datetime
now = datetime.datetime.now()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
print("Today is", months[now.month -1], now.day)

customer_orderNum = 1000
keepGoing = True
while keepGoing:

    # New Customer:
    customer_total_cost = 0
    customer_choices = []
    customer_prices = []
    customer_orderNum = customer_orderNum + 1
    name = input("Please enter your name: ")
    todays_date = now.day
    print(name + ", today is ", months[now.month], todays_date, 'and your Order Number is:', customer_orderNum)
    #____________________________________
    print("Processor option: " + str(component_names[0:3]))
    user_choice = input()

    # Validation: Have they entered a suitable option?
    while user_choice not in component_names[0:3] or stock_level[component_names.index(user_choice)] < 1:
        print("Your choice is out of stock or an invalid option. Please try again \n")
        user_choice = input()

    # find out the index of the choice
    choice_position = component_names.index(user_choice)
    #its valid, now update stock number:
    stock_level[choice_position] = stock_level[choice_position] - 1
    # append item to the list of choice ,append cost to the price list
    customer_choices.append(user_choice)
    customer_prices.append(item_prices[choice_position])
    # keep running total:
    customer_total_cost = customer_total_cost + item_prices[choice_position]
    #_____________________________________________________________________
    # loop through reming components as all have 2 option:
    for pos in range(1, len(components)):
        this_component = components[pos]
        # move along the list to reference the correct positions:
        low = pos*2+1
        high = pos*2+3
        print(this_component, 'option are: ', component_names[low:high])
        user_choice = input()
        #print(stock_level[component_names.index(user_choice)])
        #Validation: have they entered a suitbale option?
        while user_choice not in component_names[low:high] or stock_level[component_names.index(user_choice)] < 0:
            print("Your choice is out of stock or an invalid input, Please try again.")
            user_choice = input()
        #find out the index of the choice
        choice_position = component_names.index(user_choice)
        # its valid, now update stock number:
        stock_level[choice_position] -= 1
        # append item to the list of choice ,append cost to the price list
        customer_choices.append(user_choice)
        customer_prices.append(item_prices[choice_position])
        # keep running total:
        customer_total_cost = customer_total_cost + item_prices[choice_position]
        #_____________________________________________________________________

    # Finalised order details (Task 2)
    print("****** ORDER SUMMARY *******")
    print("Customer name:", name)
    print(str(months[now.month])+ str(todays_date))
    print("\nTotal Cost of this PC for: $" + str(customer_total_cost*1.2))
    print("Chosen component prices are:", customer_prices)
    #print ("Stock levels are now", stock_level)

    # Task 3 - Update variable:
    num_order += 1
    todays_total = todays_total + customer_total_cost *1.2

    print("\nMake another order?")
    go = input().lower()
    if go in ['no', 'n', 'nope']:
        keepGoing = False

# Task 3: End of the day summary 

# number of orders made
print("Number of orders today:", num_order)
#total of each component sold
for index in range(1, len(original_stock_level),1):
    print(component_names[index], original_stock_level[index] - stock_level[index], end=', ')
# value of the orders
print("\n Today's total value of orders: $" + str(todays_total))



