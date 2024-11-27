import tkinter as tk
import random
import time
import pygame

# Game constants
RUPEES_PER_DIAMOND = 10
QUICK_FIND_TIME_LIMIT = 5  # seconds for quick find multiplier
SCORE_MULTIPLIER = 2  # 2x multiplier for quick finds

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound effects
diamond_sound = pygame.mixer.Sound("Diamond.mp3")  # Replace with actual file path
bomb_sound = pygame.mixer.Sound("Bomb.wav")  # Replace with actual file path

class DiamondMineGame:
    def __init__(self, root, rows, cols, bomb_count):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.bomb_count = bomb_count
        self.buttons = {}
        self.grid = []
        self.diamonds_found = 0
        self.total_diamonds = self.rows * self.cols - self.bomb_count
        self.score = 0
        self.last_diamond_time = None  # Track last diamond find time
        self.game_over_label = None  # Placeholder for game over label

        self.root.title("Custom Diamond Mine Game")
        self.root.configure(bg="#2c2f33")

        # Fullscreen
        self.root.attributes('-fullscreen', True)

        # Score display
        self.score_label = tk.Label(self.root, text=f"Rupees: {self.score}", font=("Arial", 16, "bold"), fg="#ffffff", bg="#2c2f33")
        self.score_label.grid(row=self.rows, column=0, columnspan=self.cols, pady=10)

        self.create_grid()
        self.place_bombs()
        self.update_display()

    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(
                    self.root, text=" ", width=6, height=3,
                    bg="#4e5d6c", font=("Arial", 12, "bold"),
                    command=lambda r=row, c=col: self.reveal_cell(r, c),
                    relief="solid", bd=1, highlightthickness=0
                )
                button.bind("<Button-3>", lambda e, r=row, c=col: self.flag_cell(r, c))
                button.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[(row, col)] = button
                self.grid.append({"type": "D", "is_revealed": False, "is_flagged": False})

    def place_bombs(self):
        placed = 0
        while placed < self.bomb_count:
            row, col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.grid[self.cols * row + col]["type"] != "B":
                self.grid[self.cols * row + col]["type"] = "B"
                placed += 1

    def reveal_cell(self, row, col):
        cell = self.grid[self.cols * row + col]
        button = self.buttons[(row, col)]

        if cell["is_revealed"] or cell["is_flagged"]:
            return

        cell["is_revealed"] = True
        if cell["type"] == "D":
            button.config(text="💎", bg="whitesmoke", state="disabled", disabledforeground="blue")
            diamond_sound.play()
            self.diamonds_found += 1

            # Score calculation with quick find bonus
            current_time = time.time()
            if self.last_diamond_time and (current_time - self.last_diamond_time <= QUICK_FIND_TIME_LIMIT):
                self.score += RUPEES_PER_DIAMOND * SCORE_MULTIPLIER
            else:
                self.score += RUPEES_PER_DIAMOND

            self.last_diamond_time = current_time  # Update the last find time
            self.update_score_display()

            if self.diamonds_found == self.total_diamonds:
                self.game_over(won=True)
        elif cell["type"] == "B":
            button.config(text="💣", bg="#ff6347", state="disabled", disabledforeground="red")
            bomb_sound.play()
            self.game_over(won=False)

    def flag_cell(self, row, col):
        cell = self.grid[self.cols * row + col]
        button = self.buttons[(row, col)]

        if cell["is_revealed"]:
            return

        if cell["is_flagged"]:
            cell["is_flagged"] = False
            button.config(text=" ", bg="#4e5d6c")
        else:
            cell["is_flagged"] = True
            button.config(text="🚩", fg="#ffa500")

    def game_over(self, won):
        if self.game_over_label:
            self.game_over_label.destroy()

        result_text = "🎉 Congratulations! You found all diamonds! 🎉" if won else "💥 Game Over! You hit a bomb. 💥"
        self.game_over_label = tk.Label(self.root, text=result_text, font=("Arial", 16, "bold"), fg="#ffffff", bg="#2c2f33")
        self.game_over_label.grid(row=self.rows, column=0, columnspan=self.cols, pady=20)

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[self.cols * row + col]
                button = self.buttons[(row, col)]
                if cell["type"] == "B" and not cell["is_revealed"]:
                    button.config(text="💣", bg="#ff6347", disabledforeground="red")
                button.config(state="disabled", relief="flat", bg="#a0a4a8")

        play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 14), command=self.play_again, bg="#FFEB3B", fg="#1E1E1E")
        play_again_button.grid(row=self.rows + 1, column=0, columnspan=self.cols, pady=10)

    def play_again(self):
        self.diamonds_found = 0
        self.score = 0
        self.last_diamond_time = None  # Reset last diamond find time
        self.update_score_display()

        if self.game_over_label:
            self.game_over_label.destroy()
            self.game_over_label = None

        for button in self.buttons.values():
            button.config(text=" ", bg="#4e5d6c", state="normal")

        self.grid = []
        self.create_grid()
        self.place_bombs()
        self.update_display()

    def update_score_display(self):
        self.score_label.config(text=f"Rupees: {self.score}")

    def update_display(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        grid_width = self.cols * 80
        grid_height = self.rows * 50

        x_offset = (screen_width - grid_width) // 2
        y_offset = (screen_height - grid_height) // 2
        self.root.geometry(f"{screen_width}x{screen_height}+{x_offset}+{y_offset}")

def start_game(rows, cols, bombs):
    root = tk.Tk()
    DiamondMineGame(root, rows, cols, bombs)
    root.mainloop()

def configure_game():
    config_window = tk.Tk()
    config_window.title("Customize Your Game")
    config_window.configure(bg="#2c2f33")

    tk.Label(config_window, text="Enter Grid Size and Bomb Count", font=("Arial", 16, "bold"), bg="#2c2f33", fg="#ffffff").pack(pady=10)

    tk.Label(config_window, text="Rows:", font=("Arial", 12), bg="#2c2f33", fg="#ffffff").pack()
    row_entry = tk.Entry(config_window)
    row_entry.pack()

    tk.Label(config_window, text="Columns:", font=("Arial", 12), bg="#2c2f33", fg="#ffffff").pack()
    col_entry = tk.Entry(config_window)
    col_entry.pack()

    tk.Label(config_window, text="Number of Bombs:", font=("Arial", 12), bg="#2c2f33", fg="#ffffff").pack()
    bomb_entry = tk.Entry(config_window)
    bomb_entry.pack()

    def start_custom_game():
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        bombs = int(bomb_entry.get())

        # Ensure the number of bombs is less than total cells
        if bombs >= rows * cols:
            tk.Label(config_window, text="Bombs must be less than total cells!", font=("Arial", 10), fg="red", bg="#2c2f33").pack()
            return

        config_window.destroy()
        start_game(rows, cols, bombs)

    start_button = tk.Button(config_window, text="Start Game", font=("Arial", 14), command=start_custom_game, bg="#FFEB3B", fg="#1E1E1E")
    start_button.pack(pady=10)

    config_window.mainloop()


configure_game()
