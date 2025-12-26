print("🎮 Welcome to the Quiz Game 🎮")
print("Type a, b, c or d\n")

score = 0

questions = [
    {
        "q": "What is the capital of India?",
        "options": ["a) Delhi", "b) Mumbai", "c) Kolkata", "d) Chennai"],
        "answer": "a"
    },
    {
        "q": "Which language is used for Data Science?",
        "options": ["a) HTML", "b) Python", "c) CSS", "d) XML"],
        "answer": "b"
    },
    {
        "q": "Who is known as the Father of Computer?",
        "options": ["a) Alan Turing", "b) Charles Babbage", "c) Bill Gates", "d) Elon Musk"],
        "answer": "b"
    }
]

for q in questions:
    print(q["q"])
    for opt in q["options"]:
        print(opt)

    user_ans = input("Your answer: ").lower()

    if user_ans == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print("🎯 Quiz Finished")
print(f"Your score: {score}/{len(questions)}")
