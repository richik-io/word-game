import pygame
import random
from random_word import RandomWords
import enchant
d = enchant.Dict("en_US")
r= RandomWords()
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Scramble")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Load a random word using the random-words library
random_word = r.get_random_word()

# Scramble the word
scrambled_word = ''.join(random.sample(random_word, len(random_word)))


# Define the selected string
selected_string = ""

# Define the Refresh button
refresh_button = pygame.Rect(WIDTH // 2 - 120, HEIGHT - 80, 100, 60)

# Define the Submit button
submit_button = pygame.Rect(WIDTH // 2 + 20, HEIGHT - 80, 100, 60)

# Define the Correct text box
correct_text_box = pygame.Rect(WIDTH // 2 - 80, HEIGHT - 160, 160, 60)
correct = False

# Main game loop
running = True
while running:
    # Define buttons for each letter of the word
    button_margin = 20
    button_size = 60
    buttons = [
        pygame.Rect(button_margin + (button_size + button_margin) * i, HEIGHT // 2, button_size, button_size)
        for i in range(len(scrambled_word))
    ]
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
            # Check if the Refresh button was clicked
            if refresh_button.collidepoint(mouse_pos):
                try:
                    # Load a new random word and scramble it
                    random_word = r.get_random_word()
                    scrambled_word = ''.join(random.sample(random_word, len(random_word)))
                    # Reset the selected string
                    selected_string = ""
                    # Reset the correct flag
                    correct = False
                except:
                    print('error')
            # Check if the Submit button was clicked
            if submit_button.collidepoint(mouse_pos):
                try:
                    if d.check(selected_string.lower()):
                        correct = True
                        random_word = r.get_random_word()
                        scrambled_word = ''.join(random.sample(random_word, len(random_word)))
                        # Reset the selected string
                        selected_string = ""
                    else:
                        correct = False
                except:
                    print(selected_string)
                    print('sumbit error')
    # Clear the screen
    screen.fill(WHITE)

    # Draw the buttons
    for i, button in enumerate(buttons):
        try:
            pygame.draw.rect(screen, BLACK, button)
            letter_text = font.render(scrambled_word[i], True, WHITE)
            screen.blit(
                letter_text,
                (button.x + (button_size - letter_text.get_width()) // 2, button.y + (button_size - letter_text.get_height()) // 2)
            )
        except:
            pass

    # Draw the selected string
    selected_text = font.render(selected_string, True, BLACK)
    screen.blit(selected_text, (WIDTH // 2 - selected_text.get_width() // 2, HEIGHT // 3))

    # Draw the Refresh button
    pygame.draw.rect(screen, BLACK, refresh_button)
    refresh_text = font.render("Refresh", True, WHITE)
    screen.blit(
        refresh_text,
        (refresh_button.x + (refresh_button.width - refresh_text.get_width()) // 2, refresh_button.y + (refresh_button.height - refresh_text.get_height()) // 2)
    )

    # Draw the Submit button
    pygame.draw.rect(screen, BLACK, submit_button)
    submit_text = font.render("Submit", True, WHITE)
    screen.blit(
        submit_text,
        (submit_button.x + (submit_button.width - submit_text.get_width()) // 2, submit_button.y + (submit_button.height - submit_text.get_height()) // 2)
    )
    # Draw the Correct text box
    pygame.draw.rect(screen, BLACK, correct_text_box)
    correct_text = font.render("Correct!", True, WHITE) if correct else font.render("Incorrect", True, BLACK)
    screen.blit(
        correct_text,
        (correct_text_box.x + (correct_text_box.width - correct_text.get_width()) // 2, correct_text_box.y + (correct_text_box.height - correct_text.get_height()) // 2)
    )

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
