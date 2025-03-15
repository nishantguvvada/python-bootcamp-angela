logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
                   
'''

print(logo)

go_again = 1
bidding = {}

while go_again > 0:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidding[name] = bid
    go_again -= 1
    should_continue = input("Add more bidders? Type 'yes' or 'no': ")
    if should_continue.lower() == 'yes':
        go_again += 1

def maximum_bid(bidding):
    max_bid = {k: v for k, v in bidding.items() if v == max(bidding.values())}
    # max_bid = max(bidding, key=bidding.get)
    return max_bid

print(f"The winner is {list(maximum_bid(bidding=bidding).keys())[0]} with a bid of ${list(maximum_bid(bidding=bidding).values())[0]}")