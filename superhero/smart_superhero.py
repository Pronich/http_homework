from pprint import pprint
from superhero_class import superhero

def find_most_intelligence(hero_list):
    intel_list = []
    for hero in hero_list:
        intel_list.append(hero.intelligence)
    intel_list.sort()

    for hero in hero_list:
        if hero.intelligence == intel_list[0]:
            return hero.name

hero_list = []

hulk = superhero('Hulk')
hulk.intelligence = int(hulk.Intelligence())
hero_list.append(hulk)

cap = superhero('Captain America')
cap.intelligence = int(cap.Intelligence())
hero_list.append(cap)

thanos = superhero('Thanos')
thanos.intelligence = int(thanos.Intelligence())
hero_list.append(thanos)

pprint(find_most_intelligence(hero_list))
