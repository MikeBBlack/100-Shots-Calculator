def shots_game(num_shots):
    # Initialise list of "False" (e.g. "empty" glass) of specified length, and counter for total shots bought
    shots = [False] * num_shots
    total_bought = 0

    #Loop through each person
    for person_number in range(1, num_shots+1):
        # Initialise counter for each person to allow for 
        bought_by_person = 0
        # Loop through each shot glass
        # If the glass is divisible by the person's number, fill/empty the glass as needed
        # If the glass is filled (False to True), increment the person's counter
        for index in range(num_shots):
            if (index+1) % person_number == 0:
                if shots[index] == False:
                    bought_by_person += 1
                shots[index] = not shots[index]
        # Add the number of shots each person bought to the overall total
        total_bought += bought_by_person
        
        # Optional additional statement to show how many shots each person buys (uncomment if needed)
        # print(f"Person {person_number} bought {bought_by_person} shots. {total_bought} shots bought so far.")
    
    # Print final result
    print(f"For a row of {num_shots} empty glasses, {total_bought} shots were bought.")

# Prints results for 1-100 glasses by default - adjust as needed
for num in range(1, 101):
    shots_game(num)
