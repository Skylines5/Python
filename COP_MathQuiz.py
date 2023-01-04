# enter name

# create 10 equations
    #randomize numbers and operator

#allow user to answer equation
    #display if answer was right or wrong
    #show correct answer if wrong
    #accumulate score and total correct answers

#display name, total right, and score


import random


PERFECT_SCORE = 100
QUESTIONS = 10
total_correct = 0
total_questions = 0


print('')
intro = print("Addition math quiz. Enter name and answer 10 questions. Type in '00' to exit" +'\n')
user_name = input("Enter your name: ")
print('')


for i in range(QUESTIONS):

    number1 = random.randrange(1, 500)
    number2 = random.randrange(1, 500)
    operators = ['+'] #['+', '-', '*', '/']
    chosen_operator = random.choice(operators)

    question = str(number1) + '  ' + chosen_operator + ' ' + str(number2)
    print('What is the answer to the following equation:' +'\n'+ question)
    
    try:
        user_answer = int(input('What is the sum?: '))
        actual_answer = eval(question)

        if  user_answer == actual_answer:
            print('Correct' + '\n')
            total_correct += 1
            
        elif user_answer == 00:
            quit()
        else:
            print('-Incorrect' +'\n'+ " Correct answer =", actual_answer)
            print('')
    except:
        print('Invalid input' + '\n')



points_per_question = PERFECT_SCORE / QUESTIONS
score = total_correct * points_per_question

print(user_name.capitalize(), "got", str(total_correct), "questions right.", str(score)+"%")
