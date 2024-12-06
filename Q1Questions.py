# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
def create_question():
    # Get question input
    question = input("Enter the multiple choice question: ")
    
    # Get answers input
    print("Enter the four answer choices:")
    answers = []
    for i in range(1, 5):
        answer = input(f"Answer {i}: ")
        answers.append(answer)
    
    # Get the correct answer letter
    correct_answer = input("Enter the correct answer letter (A, B, C, D): ").upper()

    # Store the question and answers in a file
    with open("questions.txt", "a") as file:
        file.write(f"Q: {question}\n")
        for i, answer in enumerate(answers, start=1):
            file.write(f"{chr(64 + i)}: {answer}\n")
        file.write(f"Correct answer: {correct_answer}\n\n")

    print("Question added successfully!")

# Call the function to create a question
create_question()
