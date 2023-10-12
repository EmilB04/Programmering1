with open ("forelesningskoding/fil_lesing_skriving/textFil.txt", "a") as fil: #append
    while True:
        brukerInput = input(": ")

        if brukerInput == "q":
            break
        
        fil.write(brukerInput + "\n")