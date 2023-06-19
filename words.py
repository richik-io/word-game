import pygame
import random
from random_word import RandomWords
import enchant
d= enchant.Dict('en_US')
r= RandomWords()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Word Scramble")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (149, 202, 229)
BUTTON_COLOR = (126, 166, 184)

# Define font
font = pygame.font.Font(None, 36)

# Load a random word using the random-words library
random_word = r.get_random_word()

# Scramble the word
scrambled_word = ''.join(random.sample(random_word, len(random_word)))

# Define buttons for each letter of the word
button_margin = 20
button_size = 60
total_button_width = (button_size + button_margin) * len(scrambled_word) - button_margin
button_start_x = (WIDTH - total_button_width) // 2
button_start_y = (HEIGHT - button_size) // 2
buttons = [
    pygame.Rect(button_start_x + (button_size + button_margin) * i, button_start_y, button_size, button_size)
    for i in range(len(scrambled_word))
]

# Define the selected string
selected_string = ""

# Define the Refresh button
refresh_button = pygame.Rect(WIDTH // 2 - 120, HEIGHT - 80, 100, 60)

# Define the Submit button
submit_button = pygame.Rect(WIDTH // 2 + 20, HEIGHT - 80, 100, 60)

# Define the Correct text box
correct_text_box = pygame.Rect(WIDTH // 2 - 80, HEIGHT - 160, 160, 60)
correct = False

# Define the Score display
score_text = font.render("Score: 0", True, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (20, 20)
score = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check if a letter button was clicked
            for i, button in enumerate(buttons):
                if button.collidepoint(mouse_pos):
                    # Add the letter to the selected string
                    selected_string += scrambled_word[i]
                    # Disable the button
                    buttons[i] = pygame.Rect(-100, -100, 0, 0)
            # Check if the Refresh button was clicked
            if refresh_button.collidepoint(mouse_pos):
                # Load a new random word and scramble it
                random_word = r.get_random_word()
                scrambled_word = ''.join(random.sample(random_word, len(random_word)))
                # Reset the selected string
                selected_string = ""
                # Reset the correct flag
                correct = False
                # Reset the buttons
                buttons = [
                    pygame.Rect(button_start_x + (button_size + button_margin) * i, button_start_y, button_size, button_size)
                    for i in range(len(scrambled_word))
                ]
            # Check if the Submit button was clicked
            if submit_button.collidepoint(mouse_pos):
                if d.check(selected_string.lower()):
                    correct = True
                    score += 1
                    # Load a new random word and scramble it
                    random_word = r.get_random_word()
                    scrambled_word = ''.join(random.sample(random_word, len(random_word)))
                    # Reset the selected string
                    selected_string = ""
                    # Reset the correct flag
                    correct = False
                    # Reset the buttons
                    buttons = [
                        pygame.Rect(button_start_x + (button_size + button_margin) * i, button_start_y, button_size, button_size)
                        for i in range(len(scrambled_word))
                    ]
                else:
                    correct = False
                    # Reset the selected string
                    selected_string = ""

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the buttons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, BUTTON_COLOR, button)
        letter_text = font.render(scrambled_word[i], True, BLACK)
        screen.blit(
            letter_text,
            (button.x + (button_size - letter_text.get_width()) // 2, button.y + (button_size - letter_text.get_height()) // 2)
        )

    # Draw the selected string
    selected_text = font.render(selected_string, True, BLACK)
    screen.blit(selected_text, (WIDTH // 2 - selected_text.get_width() // 2, HEIGHT // 3))

    # Draw the Refresh button
    pygame.draw.rect(screen, BUTTON_COLOR, refresh_button)
    refresh_text = font.render("Refresh", True, BLACK)
    screen.blit(
        refresh_text,
        (refresh_button.x + (refresh_button.width - refresh_text.get_width()) // 2, refresh_button.y + (refresh_button.height - refresh_text.get_height()) // 2)
    )

    # Draw the Submit button
    pygame.draw.rect(screen, BUTTON_COLOR, submit_button)
    submit_text = font.render("Submit", True, BLACK)
    screen.blit(
        submit_text,
        (submit_button.x + (submit_button.width - submit_text.get_width()) // 2, submit_button.y + (submit_button.height - submit_text.get_height()) // 2)
    )

    # Draw the Correct text box
    pygame.draw.rect(screen, BUTTON_COLOR, correct_text_box)
    correct_text = font.render("Correct!", True, BLACK) if correct else font.render("", True, BLACK)
    screen.blit(
        correct_text,
        (correct_text_box.x + (correct_text_box.width - correct_text.get_width()) // 2, correct_text_box.y + (correct_text_box.height - correct_text.get_height()) // 2)
    )

    # Update the Score display
    score_text = font.render(f"Score: {score}", True, BLACK)

    # Draw the Score display
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
