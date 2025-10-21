import random

print("Voulez vous jouer ? Répondez par Y ou N.")
want_play = str(input(">>> "))


colors = ("Pique","Trèfle","Carreau","Coeur")


Values = ("1" , "2" , "3" , "4"  , "5"  , "6", "7" , "8" , "9" , "10" , "Valet", "Dame" , "Roi" )

jeu = []

if want_play == "Y" : 

    for color in colors : 
        for value in Values : 
            jeu.append({color : value})


    random.shuffle(jeu)      


    player1 = []

    player2 = []

    player3 = []

    player4 = []

    players = [player1, player2, player3, player4]

    for i in range(8) : 
        for player in players : 
            player.append(jeu.pop())


    print("Player1:", player1)
    print("__________")

    print("Player2:", player2)
    print("__________")

    print("Player3:", player3)
    print("__________")

    print("Player4:", player4)
    print("__________")
                      
else : 
    print("Bonne journée au revoir")
