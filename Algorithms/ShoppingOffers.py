'''
In LeetCode Store, there are some kinds of items to sell. Each item has a price.
However, there are some special offers, and a special offer consists of one or
more different kinds of items with a sale price. You are given the each item's price,
a set of special offers, and the number we need to buy for each item.
The job is to output the lowest price you have to pay for exactly certain items as given,
where you could make optimal use of the special offers. Each special offer is represented
in the form of an array, the last number represents the price you need to pay for this special offer,
other numbers represents how many specific items you could get if you buy this offer.
You could use any of special offers as many times as you want.
'''

def shoppingOffers(price, specials, needs):
    N = len(needs)
    clean_specials = []
    for special in specials:
        is_good = True
        for i in range(N):
            if special[i] > needs[i]:
                is_good = False
                break
        if is_good:
            clean_specials.append(special)
    
    min_price = sum([needs[i]*price[i] for i in range(N)])
    
    if len(clean_specials) == 0:
        return min_price
    
    for special in clean_specials:
        needs2 = [needs[i] - special[i] for i in range(N)]
        min_price = min([shoppingOffers(price, clean_specials, needs2) + special[-1], min_price])
    return min_price

'''
Runtime: 40ms - 100%
Memory: 14.2MB - 83.22%
'''