def new_game():
    print("Welcome to my quiz")
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:  # car index initial est 0
            print(i)
        guess = input("Enter A, B, C or D: ").capitalize()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("Results: ")
    print("Correct answers: ")
    for i in questions:
        print(questions.get(i))

    # print("Your guesses: ")
    # for i in guesses:
    #     print(guesses.get(i))

    score = int((correct_guesses/len(questions))*100)
    print("You got " + str(score) + " points")
    print("Your score is: "+str(score)+"%")


questions = {
    "What is the capital of Macedonia?": "C",
    "What is the half of 6/2?": "C",
    "What is the most spoken language in the world in 2022?": "A",
    "How old is queen Elisabeth II?": "A",
    "Who painted the famous portrait ‘MonaLisa’?": "C"
}


options = [["A. Dublin", "B: Sarajevo", "C: Skopje", "D: Reykjavik"],
           ["A. '3'", "B. '4'", "C. '1.5'", "D. '3.5'"],
           ["A. English", "B. Mandarin Chinese", "C. Spanish", "D. Arabic"],
           ["A. 95", "B. 105", "C. 92", "D. 72"],
           ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"]]

new_game()
