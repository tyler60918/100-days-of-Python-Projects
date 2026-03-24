import art

print(art.logo)

def find_highest_bidder(auction_bids):
    maxBid = 0
    maxBidder = ""
    for bidder in auction_bids:
        if auction_bids[bidder] > maxBid:
            maxBid = auction_bids[bidder]
            maxBidder = bidder
    print(f"The winner is {maxBidder} with a bid of ${maxBid}")

auction_bids = {}
more_bidders = 'yes'
while more_bidders == 'yes':
    bidder_name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bids[bidder_name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == 'yes':
        print("\n" * 20)
find_highest_bidder(auction_bids)

