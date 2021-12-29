# Importing python random and math libraries from CodeHS
import random
import math

# Variable declarations
running = True
score = 100
DELTA_SCORE = 5
clues_left = 3
guesses = 0
vals_lst = []
score_lst = []
secret_number_lst = []
difficulty_lst = []
guesses_lst = []


# Function to generate the first clue
# Returns the number by which the secret number is divisible
def generate_clue_1(secret_number, max_allowed):
    divisible = 0
    if secret_number == 1:
        divisible = secret_number
    else:
        for i in range(2, max_allowed + 1):
            if secret_number % i == 0:
                divisible = i
                break
    return divisible


# Function to generate the second clue
# Returns 'True' if secret number is greater than the halfway number based on the maximum value allowed
# Returns 'False' if secret number is less than the halfway number based on the maximum value allowed
def generate_clue_2(secret_number, max_allowed):
    middle = max_allowed // 2
    if secret_number > middle:
        return "Secret number is greater than the halfway(" + str(middle) + ") number"
    else:
        return "Secret number is less than the halfway(" + str(middle) + ") number"


# Function to generate the last clue
# Returns the last digit of the secret number
def generate_clue_3(secret_number):
    secret_number = str(secret_number)
    return secret_number[-1]


# Function to keep track of the data which will be displayed at the end of game execution
def score_tracker(score, secret_number, difficulty, guesses):
    POSSIBLE = ["EASY", "MEDIUM", "HARD"]

    # Checking if score has reached '0' or not
    if score == 0:
        print("Oops your score reached zero. Better luck next time")
        print("")
    else:
        print("Congragulations, you guessed the secret number")

    # Appending score, secret number, guess and difficulty to their respective lists
    score_lst.append(score)
    secret_number_lst.append(secret_number)
    if difficulty.upper() not in POSSIBLE:
        difficulty_lst.append("EASY")
    else:
        difficulty_lst.append(difficulty.upper())
    guesses_lst.append(guesses)


# Function to retun the maximum value allowed as the guess based on the difficulty entered by user
def get_max(difficulty):
    if difficulty.lower() == "easy":
        max_allowed = 100
    elif difficulty.lower() == "medium":
        max_allowed = 200
    elif difficulty.lower() == "hard":
        max_allowed = 300
    else:
        max_allowed = 100
    return max_allowed


# This function is called to generate a valid user guess based on different conditions
# The guess is only returned to the main function once all of the criterias have been meet
def get_guess(max_allowed, vals_lst):
    # Boolean declarations
    valid = False
    is_int = False
    is_string = False

    # While loop which will execute until the guess becomes valid i.e valid = True
    while not valid:
        guess = input("Enter your guess or type '[C]lue' to get a clue: ")

        # Determining whether the guess is a string or an integer
        try:
            if int(guess):
                is_int = True
        except ValueError:
            is_string = True

        # Checking for various conditions to see if the guess is valid
        if is_string:
            if guess.lower() == "clue" or guess.lower() == 'c':
                valid = True
            else:
                print("Guessed value must be an integer not a string")
        elif is_int:
            if int(guess) in vals_lst:
                print("Number guessed has already been tried. Pleasy try a new number")
            elif int(guess) > max_allowed:
                print("invalid guess. Guess must be within the range of 1 to " + str(max_allowed))
            elif int(guess) == 0:
                print("Guess can not be 0")
            else:
                vals_lst.append(int(guess))
                valid = True
        else:
            print("Kindly enter valid number")

        # Resets variable of is_int and is_string so that the data type of the next guess can be evaluated
        is_int = False
        is_string = False

    # Returing guess after it has been declared valid
    return guess


# Function to generate the final data for all of the trials played by user
# It is called only when the user prompts NOT to play further anymore
def generate_statistics(score_lst, secret_numbers_lst, difficulty_lst, guesses_lst):
    print("Thanks for Playing! Come Back Soon!")
    print("---------------------------------------------------------------------------------")
    print("Here is your game data:")
    print("Trial" + "\t" + "Score" + "\t" + "Secret Number" + "\t"
          + "Difficulty" + "\t" + "No. Of Guesses")

    # Displaying data in a fixed format
    for i in range(len(score_lst)):
        print(str(i + 1) + "\t" + str(score_lst[i]) + "\t" + str(secret_numbers_lst[i])
              + "\t" + "\t" + difficulty_lst[i] + "\t" + "\t" + str(guesses_lst[i]))
    print("")

    # Displaying the high-score, the trial at which the high score was achieved
    # along with the average score and the average number of guesses take before
    # guessing the secret number from analyzing the scores_lst and guesses_lst
    high_score = score_lst[0]
    sum_score = 0
    sum_guess = 0
    for i, score in enumerate(score_lst):
        sum_score += score_lst[i]
        sum_guess += guesses_lst[i]
        if score > high_score:
            high_score = score
    index = score_lst.index(high_score) + 1
    average_score = round((sum_score / len(score_lst)), 2)
    average_guess = round((sum_guess / len(guesses_lst)), 2)

    print("HIGH SCORE: " + str(high_score))
    print("ACHIEVED ON TRIAL: " + str(index))
    print("AVERAGE SCORE: " + str(average_score))
    print("AVERAGE GUESSES TAKEN: " + str(average_guess))


# Function to reset all of the essential variables required to run the game again
# Execeuted only when prompted by user choice
# This function will call the main guess_game function to execute the game code again
def play_again():
    global score, guesses, clues_left, vals_lst, running
    running = True
    score = 100
    clues_left = 3
    guesses = 0
    list.clear(vals_lst)
    print("---------------------------------------------------------------------------------")
    guess_game(running)


# Main function that runs the game endless number of times unless prompted by user
def guess_game(running):
    global guesses, score, min_allowed, clues_left, vals_lst
    difficulty = input("Select difficult [Easy, Medium, Hard]: ")
    max_allowed = get_max(difficulty)
    secret_number = random.randint(1, max_allowed)
    clue1 = generate_clue_1(secret_number, max_allowed)
    clue2 = generate_clue_2(secret_number, max_allowed)
    clue3 = generate_clue_3(secret_number)
    print(secret_number)

    while running:
        guessed_number = get_guess(max_allowed, vals_lst)
        if guessed_number.lower() == "clue" or guessed_number.lower() == "c":
            if clues_left == 3:
                print("The secret number is divisible by " + str(clue1))
                print("You have '2' clues left")
                clues_left -= 1
                score -= DELTA_SCORE * 2
                guesses += 1
            elif clues_left == 2:
                print(clue2)
                print("You have '1' clues left")
                clues_left -= 1
                score -= DELTA_SCORE * 2
                guesses += 1
            elif clues_left == 1:
                print("The last digit of the secret number is " + str(clue3))
                print("You have '0' clues left")
                clues_left -= 1
                score -= DELTA_SCORE * 2
                guesses += 1
            else:
                print("No clues left")
        else:
            if score != 0:
                guesses += 1
                if secret_number == int(guessed_number):
                    break
                elif secret_number > int(guessed_number):
                    print("The secret number is greater than the number guessed!")
                    score -= DELTA_SCORE
                else:
                    print("The secret number is less than the number guessed!")
                    score -= DELTA_SCORE
            else:
                break
    score_tracker(score, secret_number, difficulty, guesses)
    repeat = input("Type 'Yes' to play again or type 'No' to see statistics: ")
    if repeat == "Yes" or repeat == "yes":
        play_again()
    else:
        generate_statistics(score_lst, secret_number_lst, difficulty_lst, guesses_lst)


# Instructions
print("Welcome to GUESS THE NUMBER!!")
print("1) The objective of the game is simple. It can be guessed from the title itself.")
print("2) The player has to guess the secret number generated based on their choosen")
print("difficulty before their score reaches zero.")
print("3) EASY = secret number in the range of 1-100")
print("4) MEDIUM = secret number in the range of 1-200")
print("5) HARD = secret number in the range of 1-300")
print("6) For aid we have provided 3 clues to make the game much easier. However, the")
print("cons have its pros! Instead of loosing 5 points per guess the player would be")
print("loosing 10 points per clue taken. So use your bain wisely and efficiently to get")
print("the highest score possible.")
print("7) To add a cherry on top, the game can be played for an ENDLESS amount of time")
print("8) The player would be able to see all their stats for those particular games")
print("at the end, when the game is prompty finished according to the user.")
print("9) Feel free to compete with friends and familty to crown the ULTIMATE CHAMPION")
print("Let's not further ado and get into GUESS THE NUMBER!!")
print("---------------------------------------------------------------------------------")

# Game execution function being called
guess_game(running)
