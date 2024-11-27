import tkinter as tk
from tkinter import messagebox
import random
import sqlite3
import pygame

# Initialize Pygame
pygame.mixer.init()

# Database setup function
def create_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Create the table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS quiz_questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 question_text TEXT,
                 option1 TEXT,
                 option2 TEXT,
                 option3 TEXT,
                 option4 TEXT,
                 correct_answer INTEGER,
                 explanation TEXT)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Add some sample questions to the database
def insert_sample_questions():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Sample data
    sample_questions = [
        ("What is a phishing attack?", "A type of malware", "A way to steal personal information", "A computer virus",
         "A network security protocol", 1, "Phishing attacks involve tricking individuals into providing sensitive information."),
        ("What is a strong password?", "123456", "password", "aBcD@1234", "qwerty", 2, "A strong password includes a mix of characters."),
        ("What does 'HTTPS' stand for?", "HyperText Transfer Protocol", "HyperText Transfer Protocol Secure", "HyperText Transmission Protocol",
         "HyperText Protocol Secure", 1, "HTTPS is a secure extension of HTTP."),
        ("Which is a common form of social engineering?", "SQL Injection", "Phishing", "DDoS Attack", "Malware", 1,
         "Phishing is a method to deceive individuals."),
        ("What is two-factor authentication?", "A type of virus", "A method to verify identity using two methods", "A security protocol",
         "A phishing technique", 1, "Two-factor authentication adds extra security.")
    ]

    c.executemany('''INSERT INTO quiz_questions (question_text, option1, option2, option3, option4, correct_answer, explanation)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', sample_questions)

    conn.commit()
    conn.close()

# Fetch questions from the database
def fetch_questions_from_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    c.execute('SELECT * FROM quiz_questions')
    rows = c.fetchall()

    # Convert to list of Question objects
    questions = []
    for row in rows:
        question_text = row[1]
        options = [row[2], row[3], row[4], row[5]]
        correct_answer = row[6]
        explanation = row[7]
        questions.append(Question(question_text, options, correct_answer, explanation))

    conn.close()
    return questions

# Question class to hold the structure of each question
class Question:
    def __init__(self, question_text, answer_options, correct_answer_index, explanation):
        self.question_text = question_text
        self.answer_options = answer_options
        self.correct_answer_index = correct_answer_index
        self.explanation = explanation

# Quiz class to manage the flow of the quiz
class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))  # Shuffle questions
        self.score = 0
        self.current_question_index = 0

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def check_answer(self, selected_index):
        current_question = self.get_current_question()
        if selected_index == current_question.correct_answer_index:
            self.score += 1
            return True
        return False

    def next_question(self):
        self.current_question_index += 1
        return self.current_question_index < len(self.questions)

# QuizApp class for handling the GUI
class QuizApp:
    def __init__(self, root, quiz):
        self.root = root
        self.quiz = quiz
        self.root.title("Cybersecurity Awareness Quiz")

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_var = tk.IntVar()
        self.answer_buttons = []

        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.answer_var, value=i)
            btn.pack(anchor='w', padx=20)
            self.answer_buttons.append(btn)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.timer_label = tk.Label(root, text="Time left: 30")
        self.timer_label.pack(pady=10)

        self.remaining_time = 30
        self.correct_sound = pygame.mixer.Sound("Right.mp3")
        self.incorrect_sound = pygame.mixer.Sound("Wrong.mp3")
        pygame.mixer.music.load("Starting.mp3")
        pygame.mixer.music.play()

        # Check when the starting sound finishes, then show the first question
        self.wait_for_starting_music()

    def wait_for_starting_music(self):
        if pygame.mixer.music.get_busy():
            self.root.after(100, self.wait_for_starting_music)  # Check every 100ms if the music is still playing
        else:
            self.next_question()  # Show the first question once the music finishes

    def next_question(self):
        if self.quiz.next_question():
            current_question = self.quiz.get_current_question()
            self.question_label.config(text=current_question.question_text)
            for i, option in enumerate(current_question.answer_options):
                self.answer_buttons[i].config(text=option, value=i)
            self.answer_var.set(-1)
            self.remaining_time = 30
            self.update_timer()
        else:
            self.show_score()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time}")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "Time's up! Moving to the next question.")
            self.next_question()

    def submit_answer(self):
        if self.answer_var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct = self.quiz.check_answer(self.answer_var.get())
        current_question = self.quiz.get_current_question()

        if correct:
            self.correct_sound.play()  # Play correct sound
            messagebox.showinfo("Result", "Correct Answer!")
        else:
            self.incorrect_sound.play()  # Play incorrect sound
            messagebox.showinfo("Result",
                                f"Wrong Answer! The correct answer is: {current_question.answer_options[current_question.correct_answer_index]}\n\nExplanation: {current_question.explanation}")

        self.next_question()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is {self.quiz.score}/{len(self.quiz.questions)}.")
        pygame.mixer.music.stop()
        self.root.quit()

def main():
    # Create the database and insert sample questions if necessary
    create_db()
    insert_sample_questions()

    # Fetch questions from the database
    questions = fetch_questions_from_db()

    # Create the quiz instance
    quiz = Quiz(questions)

    # Set up the GUI
    root = tk.Tk()
    app = QuizApp(root, quiz)
    root.mainloop()

if __name__ == "__main__":
    main()
