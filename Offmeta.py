import requests
import Champions
import Items
import Summs
import random


type = ['Tank', 'Mage', 'Fighter', 'Assassin', 'Marksman', 'Support']
lane = ['Bottom', 'Top', 'Jungle', 'Mid']


random_type = random.choice(type)
random_lane = random.choice(lane)

random_champ = random.choice(Champions.x)

#Takes 5 items from a list in Items.py 
for i in range(5):
	random_items = random.choice(Items.x)
	print(random_items)

print()
#Suggestions for boots
for i in range(2):
	random_boots = random.choice(Items.Boots)
	Items.Boots.remove(random_boots)
	print(random_boots)

print()

#Suggestions for wards
for i in range(1):
	random_ward = random.choice(Items.Wards)
	print(random_ward)

print()

#Gives two summoner spells
for i in range(2):
	random_summs = random.choice(Summs.x)
	Summs.x.remove(random_summs)
	print(random_summs)

print()

print(random_champ + "\n" + random_type + "\n" + random_lane)
