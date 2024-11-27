import pygame
import time
import threading

# Initialize Pygame
pygame.init()

# Load the explosion sound, countdown tick sound, and image
explosion_sound = pygame.mixer.Sound("jeenajeena.mp3")  # Change to your explosion sound file
countdown_tick_sound = pygame.mixer.Sound("countdown-boom-76577.mp3")  # Change to your countdown sound file
bomb_image = pygame.image.load("TeddyLove.jpg")  # Load your image file


# Function to handle the explosion
def detonate():
    explosion_sound.play()  # Play the explosion sound
    display_message("I LOVE U")  # Display a message


def display_message(message):
    # Create a window to display the message
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Time Bomb Detonated!")

    # Set up the font and render the message
    font = pygame.font.Font(None, 74)  # Set font size
    text = font.render(message, True, (255, 0, 0))  # Render the message
    text_rect = text.get_rect(center=(400, 50))  # Center the text vertically

    # Draw everything on the screen
    screen.fill((255, 255, 255))  # Fill the background with white
    screen.blit(text, text_rect)  # Draw the message on the screen
    screen.blit(bomb_image, (200, 100))  # Draw the bomb image below the message
    pygame.display.flip()  # Update the display


    time.sleep(30)
    pygame.quit()


def countdown(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        if not pygame.mixer.get_busy():
            countdown_tick_sound.play()
        time.sleep(1)
        seconds -= 1
    detonate()


def main():
    countdown_time = 20  # Set countdown time in seconds
    countdown_thread = threading.Thread(target=countdown, args=(countdown_time,))
    countdown_thread.start()


if __name__ == "__main__":
    main()
