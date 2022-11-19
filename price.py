def format_price(price):
    #price = int(price)
    #return f'Цена: {price} руб.'
    return 'Цена: {0} руб.'.format(int(price))

new_price = format_price(56.24)
print(new_price)