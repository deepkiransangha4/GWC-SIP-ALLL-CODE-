from turtle import * 
import random

#My GUI for this is at this site:http://www.codeskulptor.org/#user41_Sy2s5YcRw3_0.py

#Menu
adjectives = ["Zesty","Delicious","Chocolatey","Buttery","Crispy","Juicy","Hearty","Citrusy","Glazed","Tart"]
food_items = ["Pasta","Tacos","Mashed Potatoes","Eggplant Parmesean","Cereal","Oatmeal","Kebab","Falafel","Fried Rice","Noodles"]
cooking_styles = ["Barbecued","Sauteed","Carmelized","Fried","Juiced","Curdled","Flipped","Pureed","Roasted","Teriyaki"]

adjectives_len = len(adjectives)
food_items_len = len(food_items)
cooking_styles_len = len(cooking_styles)


random_adjectives = random.randint(0,9)
random_food_items = random.randint(0,9)
random_cooking_styles = random.randint(0,9)

print(adjectives[random_adjectives] + " " + cooking_styles[random_cooking_styles] + " " + food_items[random_food_items])




