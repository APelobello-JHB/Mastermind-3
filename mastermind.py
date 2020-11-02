import random

def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""
    code = [0, 0, 0, 0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code

def show_instructions():
    """Shows instructions to the user"""
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def get_answer():
    """
    get user input
    """
    answer = input("Input 4 digit code: ")
    while len(answer) !=4 or not answer.isdigit():
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer

def check_correctness(results, turns):
    """Checks correctness of answer and show output to user"""
    if results[0] != 4:
        show_results(results[0], results[1])
        print('Turns left: ' + str(11 - turns))
        correct = False 
    else:
        show_results(results[0], results[1])
        print('Congratulations! You are a codebreaker!')
        correct = True
    return correct 

def take_turn(answer, code):
    """
    check correctness of answer
    """
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    results = (correct_digits_and_position, correct_digits_only)
    return (results)

def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""
    results = (correct_digits_and_position, correct_digits_only)
    correct_digits_and_position, correct_digits_only = results
    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))

def show_code(code):
    """Show Code that was created to user"""
    print('The code was: '+str(code))

def run_game():
    """Main function for running the game"""
    correct = False
    
    code = create_code()
    show_instructions()
    turns = 0
    while not correct and turns < 12:
        answer = get_answer()
        correct_digits_and_position = take_turn(answer,code)[0]
        correct_digits_only = take_turn(answer,code)[1]
        response = take_turn(answer,code)
        results = take_turn(answer, code)
        check_correctness(results, turns)
        turns += 1
        if results[0] == 4:
            break
    show_code(code)

if __name__ == "__main__":
    run_game()
