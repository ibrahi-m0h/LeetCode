# Find maxiumum price:

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 98.34
poster_price = 24.33

prices = [tshirt_price, shorts_price, mug_price, poster_price]

max = prices[0]

for price in prices:
    if price > max:
        max = price

print(max)