# We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

#    🇨🇴 Colombian pesos
#    🇵🇪 Peruvian soles
#    🇧🇷 Brazilian reais

# Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

pesos = int(input('Quantos pesos você ainda tem?'))
soles = int(input('Quantos soles você ainda tem?'))
reais = int(input('Quantos reais você ainda tem?'))

peso_usd = pesos * 0.00023
sol_usd = soles * 0.27
real_usd = reais * 0.17220

usd = peso_usd + sol_usd + real_usd

print(usd)