"""
An education app that elementary school teachers can use to help teach their students learn addition and subtraction. 
The app allows students to virtually roll two dice. The values of the dice will be displayed to the students, and the app will then ask students to input either the sum of the two dice or the difference between the two dice. 
Students are told whether their answer was correct or not.
"""
from app_functions import roll_die
from app_functions import get_question_type
from app_functions import print_question
from app_functions import input_answer
from app_functions import print_error_message
from app_functions import is_correct_answer
from app_functions import print_congratulations
from app_functions import print_correct_answer






def main():
    """
    Use the functions defined in app_functions.py to make this game work.

    The flow of the game goes as follows:
    - Rolls two virtual dice to generate two pseudo-random numbers between 1 and 6, inclusive.
    - Pseudo-randomly decide whether the question will be an addition or a subtraction question.
    - Present the question to the user and ask them to enter their response.
    - If the user entered an invalid response, print an error message and do nothing further (i.e. do not do the next two steps below).
    - If their answer was correct, congratulate them.
    - If their answer was incorrect, show them the correct answer.
    """
    print("")  # line break
    print("Welcome to the Math App!!!")
    print("")  # line break
    ### write code to complete this function BELOW here ###
    print_question(roll_die, roll_die, get_question_type)
    input_answer()
    if input_answer() == "-1":
        print_error_message()
    else:
        if is_correct_answer() == True:
            print_congratulations()
        if is_correct_answer() == False:
            print_correct_answer()


    ### write code to complete this function ABOVE here ###
    print("")  # line break
    print("Game over!!!")
    print("Thank you for playing!!!\n")


# call the main function
main()
