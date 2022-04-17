"""POKEMON DAMAGE CALCULATOR

Damage = (((2*Level)/5 + 2) (Power * A/D) / 50 + 2 ) * Modifier
    Where:
    Level = level of the attacking Pokemon
    A = effective Attack/Special Attack stat if move is a physical/special move
    D = effective Defense/Special Defense stat if move is a physical/special move
    Power = effective power of the Move used

Modifier = Targets * Weather *Badge * Critical * Random * STAB *Type
    Where:
    Targets = 0.5 if more than one target; 1 otherwise
    Weather = 1.5 if weather is beneficial to type; 0.5 if weather is against to type; 1 otherwise
    Badge = applied in Generation II only; 1.25 if Badge for type is held by player, 1 otherwise
    Critical = 2 for critical hit, 1 otherwise
    random = a random factor between 0.85 and 1.00
    STAB = same-type attack bonus; 1.5 if Move type is similar to any of user’s type, 1 otherwise
    Type = Move type effectiveness; 0 (ineffective), 0.25, 0.5 (not very effective), 1 (normal), 2 or 4 (super
    effective) depending on the Move’s and target’s types
    Burn = 0.5 if attacker is burned; 1 otherwise
    other = 1 in most cases
"""
import random 

print("""A Lv.28 Toucannon (Normal/Flying, Sp. Atk:75) attacks a Lv.28 Sandslash
(Ground, Sp. Def: 55) with Beak Blast, a Flying Type
move with a power of 120 and gain a same-type  attack bonus.
it hits a target and deals a very effective damage. The weather on the field is normal
Given the following condition, determine how much damage Toucannon's attack will deal. \n""")


#damage
Level = 28
Power = 120
A = 75
D = 75

#Modifier
Target = 1
Weather = 1.5
Bagde = 1
Critical = random.randint(1,2)
Ramdon_Number = round(random.uniform(0.05 , 1.00),2)
STAB = 1
Type = 2
other = 1

Modifier = round(Target * Weather * Bagde * Critical * Ramdon_Number * STAB * Type* other)
Damage = round((((((2*Level)/5)+2)*Power*A/D)/50)+2)+Modifier

print("Target: ",Target)
print("Weather: ",Weather)
print("Bagde: ",Bagde)
print("Critical: ",Critical)
print("Ramdon: ",Ramdon_Number)
print("STAB: ",STAB)
print("Type: ",Type)
print("other: ",other)
print("Modifiers: ",Modifier)
print("Pidgeot Deals: ",Damage, "to Sandslash " )

Recoil_Dam = round(Damage*0.333)
Recoil = random.randint(1,500)
if Recoil_Dam:
    print("As well as Sandslash is recoiling.")
else:
    print("However, Sandslash in notrecoiling")
