currentValue = 533

currency = {"quarters":25, "dimes":10, "nickels": 5, "pennies": 1}
coinAmount = {}
for coinType,currencyValue in currency.items():
    coinCount = currentValue // currencyValue
    currentValue = currentValue - (currencyValue * coinCount)
    coinAmount[coinType] = coinCount


print(f'There are {coinAmount["quarters"]} quarters, {coinAmount["dimes"]} dimes, and {coinAmount["nickels"]} nickels, and {coinAmount["pennies"]} pennies')