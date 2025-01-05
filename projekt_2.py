
# HLAVIČKA souboru
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Luděk Šubrt
email: LSubrt@seznam.cz
discord: 001Marek#7313
"""
# import modulů do Python programu
import random
import time

# generuje 4místné číslo bez opakujících číslic a které nezačíná 0
def generate_number():
    first_digit = random.choice(list("123456789")) 
    remaining_digits = list("0123456789")  
    remaining_digits.remove(first_digit) 
    other_digits = random.sample(remaining_digits, 3)
    number = first_digit + ''.join(other_digits)
    return number

# získává a ověřuje vstup od uživatele
def validate_guess(guess):
    if len(guess) !=4 or not guess.isdigit():
        return "Please enter a 4-digit number"
    if guess[0] == "0":
        return "The number cannot start with 0"
    if len(set(guess)) !=4:
        return "The digits must be unique"
    return None

# počítání počtu "Bulls" a "Cows"
def bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

# definuje hlavní funkci main, kde je řízeno samotné hraní hry
def main():
    print("Hi there!")
    print("-" * 47)
    secret_number = generate_number()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a Bulls and Cows game.")
    print("-" * 47)
    
    guesses = 0
    start_time = time.time()
    
# začíná nekonečný cyklus, který umožňuje hadání čísla, dokud se neuhodne    
    while True:
        guess = input("Enter a number: ")
        error_message = validate_guess(guess)
        
        if error_message:
            print(error_message)
            continue
        
        guesses += 1
        bulls, cows = bulls_and_cows(secret_number, guess)
        
        bulls_word = "bull" if bulls == 1 else "bulls"
        cows_word = "cow" if cows == 1 else "cows"
        
        print(f"{bulls} {bulls_word}, {cows} {cows_word}")
        print("-" * 47)
        
        if bulls == 4:
            elapsed_time = time.time() - start_time
            print(f"Correct, you have guessed the right number in {guesses} guesses!")
            feedback = "That is amazing!" if guesses<= 5 else "That is average!" if guesses <= 10 else "Not so good."
            print(f"{feedback}")
            print(f"Time taken: {elapsed_time:.2f} seconds")
            break
        
if __name__ == "__main__":
    main()
    
            
        
        
        
    



