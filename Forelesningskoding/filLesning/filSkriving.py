with open ("forelesningskoding/filLesning/textFil.txt", "a") as fil: #append
    while True:
        brukerInput = input(": ")

        if brukerInput == "q":
            break
        
        fil.write(brukerInput + "\n")