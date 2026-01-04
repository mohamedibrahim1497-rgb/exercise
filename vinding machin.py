#
print("Welcome to my vending machine")
print("code      item       price      stock")
print(" [112]     pepsi        $2         4     ")
print(" [221]      coke        $2         3    " )
print(" [332]     chips        $1         0     ")
print(" [443]     choco        $4         2     ")
print(" [554]     juice        $2         5     ")
print(" [665]     water        $1          8   " )
#create variable for items price and stock
pepsi_price = 2
coke_price = 2
chips_price = 1
choco_price = 4
juice_price = 2
water_price = 1

pepsi_stock = 4
coke_stock = 3
chips_stock = 0
choco_stock = 2
juice_stock = 5
water_stock = 8

#insert money command and stock availibiltyb command:

def purchase_item(item,price, stock) :
    if stock > 0:
        print(f"You chose {item} . please insert ${price}.")
        money_inserted = float(input())
        if money_inserted >= price:
            stock -= 1
            print(f"Here is your {item}. Enjoy!")
            if money_inserted > price:
                print(f"Here is your change: ${money_inserted - price}")
            else:
                print("Insufficient money . please try again.")
        else:
          print(f"Sorry, {item} is out of stock")
          return stock
while True:

    #ask the user to selct a code
    print("please enter a code for an item:")
    user_Code = int(input())

    #evey code category
    if user_Code == 112:
        pepsi_stock = purchase_item("Pepsi" , pepsi_price, pepsi_stock)
    elif user_Code == 221:
        coke_stock = purchase_item("Coke" , coke_price, coke_stock)
    elif user_Code == 332:
        chips_stock = purchase_item("Chips", chips_price, chips_stock)
    elif user_Code == 443:
        choco_stock = purchase_item("Choco", choco_price, choco_stock)
    elif user_Code == 554:
        juice_stock = purchase_item("Juice" , juice_price, juice_stock)
    elif user_Code == 665:
        water_stock = purchase_item("Water" , water_price, water_stock)
    else:
        print("Invalid code. please try agin.")
        continue
    again = input("Would you like to but another item?  (Yes/No:)").strip().lower()
    if again != "yse":
        print("Thank you for using my vnding machine! Goodbye!")
        break
