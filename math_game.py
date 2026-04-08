while True:
    print("\n----- Μαθηματικό Παιχνίδι -----")
    print("1. Πρόσθεση (+)")
    print("2. Αφαίρεση (-)")
    print("3. Πολλαπλασιασμός (X)")
    print("4. Έξοδος")
    
    epilogi = input("\nΕπίλεξε πράξη (1-4): ")

    if epilogi == "1":
        print("\n--- Ας προσθέσουμε! ---")
        num1 = int(input("Δώσε τον πρώτο αριθμό: "))
        num2 = int(input("Δώσε τον δεύτερο αριθμό: "))
        sum = num1 + num2
        print(f"Το αποτέλεσμα είναι: {num1} + {num2} = {sum}")

    elif epilogi == "2":
        print ("\n --- Ας αφαιρέσουμε! ---")
        num1 = int(input("Δώσε τον πρώτο αριθμό: "))
        num2 = int(input("Δώσε τον δεύτερο αριθμό: "))
    
        if num1 >= num2:
            diaf = num1 - num2  
            print(f"Η διαφορά τους είναι: {num1} - {num2} = {diaf}")
        else:
            diaf = num2 - num1  
            print(f"Η διαφορά τους είναι: {num2} - {num1} = {diaf}")
        

    elif epilogi == "3":
        print("\n--- Ας πολλαπλασιάσουμε! ---")
        num1 = int(input("Δώσε τον πρώτο αριθμό: "))
        num2 = int(input("Δώσε τον δεύτερο αριθμό: "))
        ginomeno = num1 * num2
        print(f"Το γινόμενο είναι: {num1} * {num2} = {ginomeno}")

    elif epilogi == "4":
        print("Ευχαριστώ που παίξαμε! Τα λέμε!")
        break  # Σταματάει το loop και κλείνει το πρόγραμμα
    
    else:
        print("Χμμ, δεν κατάλαβα... Διάλεξε 1, 2, 3 ή 4")
    epipedo=(input ("\nΕπίλεξε επίπεδο δυσκολίας: "))
    print ("\n1. Εύκολο")
    print ("\n2. Δύσκολο")
#time to commit