hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price

average_price = total_price/len(prices)

print(f'The average price of haircut is ${average_price}')

lower_prices = []

for discount in prices:
    lower_prices.append(discount-5)

print(lower_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue = prices[i]+last_week[i]

print(f'Total Revenue: {total_revenue}')