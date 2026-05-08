# Python Project: Math Game
import random
import time
print("\n===== Μαθηματικό Παιχνίδι =====\n\n")
#Menu
# until correct input loop create
while True:
def main_menu():
    choice = input("Τι θέλετε να κάνετε; Παρακαλώ επιλέξτε: \n\n"
                     "1. Έναρξη παιχνιδιού\n"
                     "2. Οδηγίες\n"
                     "3. Έξοδος\n\n"
                     "📌 Επιλέξτε 1-3: ")
    
    # Choices for menu
    if choice == '1':
        play_game()
    elif choice == '2':
        show_instructions()
    elif choice == '3':
        print("Ευχαριστούμε που παίξατε!")
    else:
        print("Άκυρη επιλογή. Παρακαλώ δοκιμάστε ξανά.")

def play_game():
    score = 0     



    print("\n===== Μαθηματικό Παιχνίδι =====")
    print("1. Πρόσθεση (+)")
    print("2. Αφαίρεση (-)")
    print("3. Πολλαπλασιασμός (X)")
    print("4. Έξοδος")
    
    epilogi = input("\nΕπίλεξε πράξη (1-4): ")

    if epilogi == "1":
        print("\n--- Ας προσθέσουμε! ---")
        print("Διάλεξε επίπεδο δυσκολίας: ")
        print ("Επίπεδο 1: Εύκολο \n" 
               "Επίπεδο 2: Μέτριο \n"
               "Επίπεδο 3: Δύσκολο \n")
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