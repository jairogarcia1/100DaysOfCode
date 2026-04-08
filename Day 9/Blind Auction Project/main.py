import art
print(art.logo)
# TODO-1: Ask the user for input
name = input("What is your name? ")
bid = input("What is your bid? $")
# TODO-2: Save data into dictionary {name: price}
bid_dict = {name: bid}
# TODO-3: Whether if new bids need to be added
new_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
while new_bid == "yes":
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bid_dict[name] = bid
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
for key in bid_dict:
    if int(bid_dict[key]) > highest_bid:
        highest_bid = int(bid_dict[key])
        winner = key
print(f"The winner is {winner} with a bid of ${highest_bid}.")


