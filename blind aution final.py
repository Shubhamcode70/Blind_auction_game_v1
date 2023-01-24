from replit import clear
from blindart import logo

print("Welcome to Blindart Auction \n", logo)

aution_record = {}

def highest_bidder(aution_record):
    highest_bid = 0
    winner = ""
    for bidder in aution_record:
        bid_amount = aution_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Highest bid is {highest_bid} and Winner is {winner}")
        
bidding_finished = False
while not bidding_finished:
    user_name = input("Enter Your Name: \n")
    user_bid_price = int(input("Enter Your Bidding Price: \n"))
    #storing the values in the dictionary
    aution_record[user_name] = user_bid_price
    
    want_continue = input("Is there other user for bidding ? Please enter Yes or No : \n")
    if want_continue == "no":
        bidding_finished = True
        highest_bidder(aution_record)
    elif want_continue == "yes":
        clear()
