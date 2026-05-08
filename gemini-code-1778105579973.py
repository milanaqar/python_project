import time

def countdown(seconds):
    while seconds > 0:
        print(f"Απομένουν: {seconds} δευτερόλεπτα", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Τέλος χρόνου! Μπαμ! 💥")

# countdown(10)