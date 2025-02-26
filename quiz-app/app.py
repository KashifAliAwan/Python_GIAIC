class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        user_answer = input("Your answer (enter the number): ")
        return int(user_answer)

    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            user_answer = self.display_question(question, options)
            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}: {options[correct_answer-1]}\n")
        print(f"Quiz ended! Your final score is {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
        ("What is 2 + 2?", ["3", "4", "5", "6"], 2),
        ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], 2),
        ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4)
    ]

    quiz = QuizApp(questions)
    quiz.run_quiz()