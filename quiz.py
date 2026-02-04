import json
import random

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def run_quiz():
    questions = load_questions()
    score = 0

    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        choice = int(input("Enter your answer number: "))
        selected = q["options"][choice - 1]

        if selected == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is: {q['answer']}")

    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()

