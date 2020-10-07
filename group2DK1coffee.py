#Creating a virtual coffee machine, with prices
#Define a dictionary of ingredients per beverage
import time
CoffeeIngredients = {"Americano":"70% Ground Coffee Beans, 30% Water","Cafe Latte":"40% Ground Coffee Beans, 20% Water, 40% Hot Milk","Cappuccino":"35% Espresso, 35% Hot Milk, 30% Milk Foam","Hot Cocoa":"60% Cocoa Powder, 40% Hot Milk","Hot Water":"100% Hot Water"}
#Define a separate dictionary of prices per beverage
CoffeePrices = {"Americano":"21kr","Cafe Latte":"24kr","Cappuccino":"26kr","Hot Cocoa":"15kr","Hot Water":"5kr"}
#Show the different beverages and corresponding prices to the user
print("Beverage \t - \tPrice")#Beverage and Price printed with two tabs and a dash in between
print("-----------------------------")#Several dashes in a row to simulate a line
for key,value in CoffeePrices.items():
    print(str(key) + "\t - \t" + str(value))
#Ask the user to choose a drink
drink = input("Hello. Which drink would you like?\n")
#Match the input to the dictionary for a price and order
if ((drink == "Americano") or (drink == "Cafe Latte") or (drink == "Cappuccino") or (drink == "Hot Cocoa") or (drink == "Hot Water")):
    print(f"Certainly, one {drink} coming up, please wait.")
    print(f"Your total will be... {CoffeePrices[drink]}. Press RETURN when payment is ready.")
    input() #Asking the user to press RETURN
    print(f"Gathering ingredients for {drink}. {drink} is made of {CoffeeIngredients[drink]}")
    print("Please, hold on while the drink is being made.")
    print("...\t...\t...")
    #Delay the following commands by 5 seconds, to simulate waiting for the drink
    time.sleep(5)   #Delays for 5 seconds.
    print("Your order is finished!")
    time.sleep(2) #Delay one second, for visibility.
    print("Be careful, it is hot.")
    print("Please, enjoy.")
#If input doesn't match dictionary, explain to user
else:
    print("Sorry, I don't have that.")
