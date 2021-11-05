import random

ronde = 0 
poging = 0
randomNumber = 0
score = 0
while ronde < 20:
    ronde += 1
    randomNumber = random.randint(1, 1000)
    print("Dit is ronde:",ronde)
    poging = 0
    while poging < 10:
        gok = int(input("Welke getal wil je invullen:\n"))
        poging += 1
        verschil = gok - randomNumber
        if verschil < 0:
            verschil = abs(verschil)
        if gok == randomNumber:
            print("Je hebt goed geraden")
            score += 1
            if ronde == 20:
                break
            print("Je score is:",score)
        elif poging == 10:
            print("Je hebt niet de goede getal geraden, het getal was:", randomNumber)
            print("Je score is:",score)
        if poging == 10 or gok == randomNumber:
            if ronde == 20:
                break 
            nogmaals = input("Nog een getal raden? ja/nee \n")
            if nogmaals == "ja":
                poging = 11
            else:
                poging = 11
                ronde = 20        
        
        if verschil < 50 and verschil > 20:
            print('Je bent warm')
            if gok > randomNumber:
                print('Probeer wat lager')
            else:
                print('Probeer wat hoger.')  
        elif verschil < 20 and verschil > 0:
            print('Je bent heel warm')
            if gok > randomNumber:
                print('Probeer wat lager')
            else:
                print('Probeer wat hoger.') 
print("Je eindscore is:", score)             