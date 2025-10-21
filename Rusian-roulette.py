import random



while True : 

    print("Voulez vous tirer ? Répondez par Oui ou Non.")

    want_shoot = str(input(">>> "))
    load_chamber = random.randint(1,6)
    choose_chamber = random.randint(1,6)

    if want_shoot == ("Oui") or ("oui"):

        if load_chamber != choose_chamber : 

            print("Vous avez survécu")
            print(f"La chambre chargée était la : {load_chamber}")
            print("Voulez vous rejouer ? Oui ou Non")
            Replay = str(input(">>> "))

            if Replay == ("Oui") or ("oui") : 

                continue

            else : 

                break

        elif load_chamber == choose_chamber :

            print ("Dommage, vous êtes mort")
            print(f"La chambre chargée était la : {load_chamber}")
    else :
        print ("Tapette")
        break
