# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
def load_questions():
    questions = []
    with open("questions.txt", "r") as file:
        question = None
        answers = []
        correct_answer = None
        for line in file:
            line = line.strip()
            if line.startswith("Q:"):
                if question:
                    questions.append((question, answers, correct_answer))
                question = line[2:].strip()
                answers = []
            elif line.startswith("Correct answer:"):
                correct_answer = line.split(":")[1].strip()
            elif line:
                answers.append(line.split(":")[1].strip())
        if question:
            questions.append((question, answers, correct_answer))  # Append last question
    return questions

def ask_questions(questions):
    score = 0
    for idx, (question, answers, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question}")
        for i, answer in enumerate(answers, start=1):
            print(f"{chr(64 + i)}: {answer}")

        user_answer = input("Enter your answer (A, B, C, D): ").upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

# Load the questions from the file
questions = load_questions()

# Ask the questions and keep score
ask_questions(questions)
