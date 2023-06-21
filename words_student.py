# Word Scramble Game
# This program is a word scramble game where players unscramble words by selecting letters
# and submitting their guesses. The game provides a random scrambled word, and the player
# needs to rearrange the letters to form a valid English word. The player earns points for
# each correct guess and can refresh to get a new word. The game is built using the Pygame
# library.
import pygame
import random
from random_word import RandomWords
import enchant

# Initialize enchant dictionary for English words
d = enchant.Dict('en_US')

# Initialize random word generator
r = RandomWords()

# Initialize Pygame
pygame.init()

# Set up the display, set it to fullscreen and add a title


# Define colors

# Define font

# Load a random word using the random-words library ref to the documentation of 

# Scramble the word

# Define buttons for each letter of the word


# Define the selected string

# Define the Refresh button

# Define the Submit button

# Define the Correct text box

# Define the Score display

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check if a letter button was clicked
                    
                    # Add the letter to the selected string
                    
                    # Disable the button
                    
            # Check if the Refresh button was clicked
            if refresh_button.collidepoint(mouse_pos):
                # Load a new random word and scramble it
                
                # Reset the selected string
                
                # Reset the correct flag
                
                # Reset the buttons
            


            # Check if the Submit button was clicked
            
                    # Load a new random word and scramble it
                    
                    # Reset the selected string
                    
                    # Reset the correct flag
                    
                    # Reset the buttons
                    
                else:
                    
                    # Reset the selected string
                    
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
    
    # Draw the Refresh button
    

    # Draw the Submit button
    

    # Draw the Correct text box
   

    # Update the Score display
    
    # Draw the Score display
    
    # Update the display
    
# Quit the game
pygame.quit()
