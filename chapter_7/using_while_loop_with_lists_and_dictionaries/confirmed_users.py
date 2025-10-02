# Moving items from 1 list to another
stocks_untraded = ['NVDA', 'AMZN', 'AMD', 'APPL']
stocks_traded = []

while stocks_untraded:
    current_stock = stocks_untraded.pop()
    print(f'Addng {current_stock} to traded stocks :)')
    stocks_traded.append(current_stock)

print(stocks_traded)