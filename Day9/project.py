from art import art

print(art)

bids_and_bidders={}
continue_bidding=True
while continue_bidding==True:
    name= input("What's your name?\n").lower()
    bid= int(input("What's your bid\n$"))
    bids_and_bidders[name]=bid

    keep_going=input("Are there any more bidders? yes or no: ").lower()

    print("\n"*100)

    if keep_going=='no':
        continue_bidding=False

all_bids=[]
for key in bids_and_bidders:
    all_bids.append(bids_and_bidders[key])

highest_bid=max(all_bids)
highest_bidder=""
for key, value in bids_and_bidders.items():
    if value==highest_bid:
        highest_bidder=key

print(f"{highest_bidder} won this auction with a bid of ${highest_bid}")
    
   
