# amount of students that took the test
# enter test score for each student

# get average of test scores
# display average score

get_average_score = True

while get_average_score:

    test_taken_amt = int(input('How many students took the test: '))
    total_student_score = 0

    for students in range(test_taken_amt):
        student_score = int(input('Enter their score: '))
        total_student_score += student_score


    end_or_continue = input("Do you want to end program? (Enter no to process a new set of scores):  ")
    if end_or_continue.lower() == 'yes':
        get_average_score = False
    else:
        continue

    
average_test_score = total_student_score / test_taken_amt
print('Average test score is', str(average_test_score))
