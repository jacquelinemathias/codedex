# Every year at the Oscars, the Academy Award for Best Picture is awarded to a single film. It's usually the last award presented and is considered to be the most prestigious.

# Let's use a Python list to document the recent winners!

# Google the Best Picture winners from 2020, 2021, 2022, 2023, and 2024. Then, add them to the front of the best_pictures list.

# Lastly, print the best_pictures list. Make sure that the updated list starts with the winner for 2024, then 2023, then 2022, then 2021, then 2020, and so on.

# Note: Make sure to match the format of the existing list. And remember, it's the year of the movie, not the year of the ceremony.

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist'
]

best_pictures.reverse()
best_pictures.append('2020 - Nomadland')
best_pictures.append('2021 - CODA')
best_pictures.append('2022 - Everything Everywhere All At Once')
best_pictures.append('2023 - Oppenheimer')
best_pictures.append('2024 - Anora')

for i in best_pictures:
    print(i)