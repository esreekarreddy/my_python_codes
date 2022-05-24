import art
import os

print(art.logo)
entry = False
entries = {}

def highest_bid(entries):
    highest = 0
    for bidder in entries:
        bidder_amount = entries[bidder]
        if bidder_amount > highest:
            highest = bidder_amount
            bidder_name = bidder
    os.system('clear')
    print(f"The winner is {bidder_name} with a bid of ${highest}.")

while not entry:
    name = input("Enter the name: ")
    bid = int(input("Enter the bid value: "))
    entries[name] = bid
    print("Entry has been taken in.")
    entry_vaule = input("Is there another bidder (yes/no)? ")
    if entry_vaule == "yes":
        os.system('clear')
    else:
        entry = True
        highest_bid(entries)


