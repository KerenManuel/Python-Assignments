
current_population = 2000
population_increase_rate = 0.15
duration = 1
expected_population = 2000000
year = 0

while current_population <= expected_population:
        current_population = int(current_population + (current_population * population_increase_rate * duration ))
        year += 0.5
print(f'Year: {year} and Population:{current_population} ')


