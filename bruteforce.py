
import csv
import json

from itertools import combinations


with open('forcebrute.csv') as data:
    data = [d for d in csv.DictReader(data, delimiter=';')]
    

combinaisons = []
for i in range(1, 20):
  comb = combinations(data, i)
  combinaisons.extend(list(comb))


print(len(combinaisons))



def sumcomb(comb):
  total_price = 0
  for element in comb:
    total_price += int(element["price"])
  return total_price

new_combinaisons = []

for comb in combinaisons:
  comb_price = sumcomb(comb)
  if comb_price <= 500:
    new_combinaisons.append(comb)


def calculer_profit(comb):
  total_profit =0
  for element in comb:
    total_profit += (int(element['profit']) * int(element['price'])) / 100
  return total_profit

best_combination = new_combinaisons[0]
best_total_profit = calculer_profit(best_combination)

for comb in new_combinaisons:
  total_profit= calculer_profit(comb)
  if total_profit > best_total_profit:
    best_total_profit = total_profit
    best_combination = comb

    
print(best_total_profit)
print(best_combination)
total_price = sumcomb(best_combination)
print(total_price)

  

# comparer le temps d'exécution et remettre au propre les prints avec des phrses plus juste nom des actions 



