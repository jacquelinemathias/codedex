# Create a stock_analysis.py program that implements three functions:

#     price_at(x) that finds the price on a given day x.
#     max_price(a, b) that finds the maximum price from day a to day b.
#     min_price(a, b) that finds the minimum price from day a to day b.

# The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

i = int(input('Qual dia você deseja saber o valor da bolsa? (1-20)'))
a = int(input('Deseja encontrar os valores mínimos e máximos começando de qual dia? '))
b = int(input('E terminando em qual? '))

if i >= 1 and i <= 20:
    def encontrar_preco(i):
        return stock_prices[i-1]
else:
    print('Valor inválido')

print(min(stock_prices[a - 1 : b]))
print(max(stock_prices[a - 1 : b]))