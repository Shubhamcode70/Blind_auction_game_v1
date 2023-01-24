from blindart import logo
from replit import clear
print(f"Blind Aution Has Started","\n",logo)

def find_highest_bid(dict):

    highest_bid = 0
    winner = ""
    
    for bidder in dict:
        bid_amount = dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with highest {highest_bid} bid")
    
dict = {}
want_continue = True
while want_continue:
    user_name = input("Enter user name : \n")
    bid = int(input("Enter your bid RS. \n"))
    dict[user_name] = bid
    
    #print(dict)
    
    user_choice = input("Is there any other Bidder ?  Enter Yes or No. \n").lower()

    
    if user_choice == "yes" :
        clear()
        want_continue = True
    elif user_choice == "no":
        find_highest_bid(dict)
        want_continue = False
