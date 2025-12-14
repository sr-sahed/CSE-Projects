import pygame
import sys
import random
import os
import sys


# py installed
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)




# Initialize Pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Save From Box Game")

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_BORDER_COLOR = (255, 0, 0) 
BUTTON_COLOR = (0, 0, 255)  
HOVER_TEXT_COLOR = (255, 0, 0)  
TEXT_COLOR = (255, 255, 255)  
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SLOW_COLOR = (255, 165, 0)  
BOOST_COLOR = (0, 255, 255) 

# Background image
background = pygame.image.load(resource_path('assets/background.png'))
background = pygame.transform.scale(background, (800, 600))

# Load background music and sound effects
background_music = pygame.mixer.music.load(resource_path('assets/background_music.wav'))
button_click_sound = pygame.mixer.Sound(resource_path('assets/button_click.mp3'))
game_over_sound = pygame.mixer.Sound(resource_path('assets/game_over.mp3'))

# Player 
player_size = 50
player_x = 375
player_y = 275
original_player_speed = 5
player_speed = original_player_speed

# Obstacle 
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []
spawn_probability = 0.02 

# Power-ups
power_up_width = 30
power_up_height = 30
power_ups = []
power_up_speed = 3
speed_boost_duration = 10 
slowdown_duration = 10  

# Power-up types
SPEED_BOOST = 1
SLOWDOWN = 2

# Difficulty Levels
EASY = 1
NORMAL = 2
HARD = 3

# Default settings
difficulty = NORMAL
score = 0
level = 0
# Button dimensions (for calculation purposes, to detect clicks)
button_width = 200
button_height = 50

# Button texts
start_text = font.render("Start", True, WHITE)
score_text = font.render("Score", True, WHITE)
settings_text = font.render("Settings", True, WHITE)
rules_text = font.render("Rules", True, WHITE)
quit_text = font.render("Quit", True, WHITE)

# Positions of the buttons
start_pos = (300, 150)
score_pos = (300, 220)
settings_pos = (300, 290)
rules_pos = (300, 360)
quit_pos = (300, 430)

# Difficulty setting
difficulty = "Normal"
high_scores = {"Easy": 0, "Normal": 0, "Hard": 0}

# Function to check if the mouse click is on a specific button's text
def is_text_button_clicked(text_surface, pos, mouse_pos):
    text_rect = text_surface.get_rect(topleft=pos)
    return text_rect.collidepoint(mouse_pos)

# Function to handle menu click actions
def handle_menu_click(mouse_pos):
    if is_text_button_clicked(start_text, start_pos, mouse_pos):
        button_click_sound.play()
        game_loop() 
    elif is_text_button_clicked(score_text, score_pos, mouse_pos):
        button_click_sound.play()
        show_score() 
    elif is_text_button_clicked(settings_text, settings_pos, mouse_pos):
        button_click_sound.play()
        settings_screen() 
    elif is_text_button_clicked(rules_text, rules_pos, mouse_pos):
        button_click_sound.play()
        rules_screen()  
    elif is_text_button_clicked(quit_text, quit_pos, mouse_pos):
        pygame.quit()
        sys.exit()

# Function to check if the mouse is hovering over a button
def is_text_button_hovered(text_surface, pos, mouse_pos):
    text_rect = text_surface.get_rect(topleft=pos)
    return text_rect.collidepoint(mouse_pos)

# Function to render text with a specific color
def render_text(text, color, font_type=font):
    return font_type.render(text, True, color)

# Main menu function
def main_menu():
    while True:
        screen.fill(BLACK)

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw the text (acting as buttons)
        # Start Button
        if is_text_button_hovered(start_text, start_pos, mouse_pos):
            screen.blit(render_text("Start", HOVER_TEXT_COLOR), start_pos)  
            pygame.draw.rect(screen, HOVER_BORDER_COLOR, start_text.get_rect(topleft=start_pos), 2) 
        else:
            screen.blit(start_text, start_pos)  

        # Score Button
        if is_text_button_hovered(score_text, score_pos, mouse_pos):
            screen.blit(render_text("Score", HOVER_TEXT_COLOR), score_pos) 
            pygame.draw.rect(screen, HOVER_BORDER_COLOR, score_text.get_rect(topleft=score_pos), 2)  
        else:
            screen.blit(score_text, score_pos) 

        # Settings Button
        if is_text_button_hovered(settings_text, settings_pos, mouse_pos):
            screen.blit(render_text("Settings", HOVER_TEXT_COLOR), settings_pos)  
            pygame.draw.rect(screen, HOVER_BORDER_COLOR, settings_text.get_rect(topleft=settings_pos), 2) 
        else:
            screen.blit(settings_text, settings_pos) 
        # Rules Button
        if is_text_button_hovered(rules_text, rules_pos, mouse_pos):
            screen.blit(render_text("Rules", HOVER_TEXT_COLOR), rules_pos)  
            pygame.draw.rect(screen, HOVER_BORDER_COLOR, rules_text.get_rect(topleft=rules_pos), 2) 
        else:
            screen.blit(rules_text, rules_pos)  

        # Quit Button
        if is_text_button_hovered(quit_text, quit_pos, mouse_pos):
            screen.blit(render_text("Quit", HOVER_TEXT_COLOR), quit_pos) 
            pygame.draw.rect(screen, HOVER_BORDER_COLOR, quit_text.get_rect(topleft=quit_pos), 2)  
        else:
            screen.blit(quit_text, quit_pos)  

        # Check for events (clicking and quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(mouse_pos)

        pygame.display.flip()

# Show Rules Screen
def rules_screen():
    while True:
        screen.fill(BLACK)

        title = large_font.render("Game Rules", True, WHITE)
        rules = [
            "1. Avoid the boxes falling from the top!",
            "2. Red boxes slow you down.",
            "3. Blue boxes speed you up.",
            "4. Collect power-ups to boost your speed or avoid being slowed.",
            "5. Each level becomes harder as you avoid more obstacles.",
        ]
        
        screen.blit(title, (300, 50))

        # Display the rules
        y_offset = 120
        for rule in rules:
            rule_text = render_text(rule, WHITE)
            screen.blit(rule_text, (50, y_offset))
            y_offset += 40

        back_text = font.render("Press 'B' to Go Back", True, WHITE)
        screen.blit(back_text, (300, 500))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()

        pygame.display.flip()

def save_score():
    try:
        with open("high_scores.txt", "w") as file:
            file.write(str(score)) 
    except Exception as e:
        print(f"Error saving score: {e}")

def load_score():
    try:
        with open("high_scores.txt", "r") as file:
            saved_score = int(file.read())  
            return saved_score
    except FileNotFoundError:
        return 0  
    except Exception as e:
        print(f"Error loading score: {e}")
        return 0

def show_score():
    saved_score = load_score() 

    while True:
        screen.fill(BLACK)

        title = large_font.render(f"High Scores - {difficulty}", True, WHITE)
        screen.blit(title, (200, 50))

        score_text = font.render(f"High Score: {saved_score}", True, WHITE)
        screen.blit(score_text, (300, 150))

        back_text = font.render("Press 'B' to Go Back", True, WHITE)
        screen.blit(back_text, (300, 350))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  
                    main_menu()

        pygame.display.flip()


# Settings 
def settings_screen():
    global difficulty
    while True:
        screen.fill(BLACK)

        title = large_font.render("Settings", True, WHITE)
        screen.blit(title, (300, 50))

        difficulty_text = font.render(f"Current Difficulty: {difficulty}", True, WHITE)
        screen.blit(difficulty_text, (300, 150))

        easy_button = font.render("Easy", True, WHITE)
        normal_button = font.render("Normal", True, WHITE)
        hard_button = font.render("Hard", True, WHITE)

        screen.blit(easy_button, (300, 220))
        screen.blit(normal_button, (300, 290))
        screen.blit(hard_button, (300, 360))

        back_text = font.render("Press 'B' to Go Back", True, WHITE)
        screen.blit(back_text, (300, 450))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.get_rect(topleft=(300, 220)).collidepoint(mouse_pos):
                    difficulty = "Easy"
                elif normal_button.get_rect(topleft=(300, 290)).collidepoint(mouse_pos):
                    difficulty = "Normal"
                elif hard_button.get_rect(topleft=(300, 360)).collidepoint(mouse_pos):
                    difficulty = "Hard"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  
                    main_menu()

        pygame.display.flip()

# Add obstacles randomly
def spawn_obstacle():
    x = random.randint(0, 750)
    y = -obstacle_height  
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

# Add power-ups randomly
def spawn_power_up():
    x = random.randint(0, 750)
    y = -power_up_height  
    power_up_type = random.choice([SPEED_BOOST, SLOWDOWN])
    power_ups.append((pygame.Rect(x, y, power_up_width, power_up_height), power_up_type))

# Set difficulty settings
def set_difficulty_settings():
    global obstacle_speed, spawn_probability
    if difficulty == EASY:
        obstacle_speed = 3
        spawn_probability = 0.01
    elif difficulty == NORMAL:
        obstacle_speed = 5
        spawn_probability = 0.02
    elif difficulty == HARD:
        obstacle_speed = 7
        spawn_probability = 0.03

# Game loop with difficulty scaling
def game_loop():
    pygame.mixer.music.load(resource_path('assets/background_music.wav'))
    pygame.mixer.music.play(loops=-1, start=0.0)

    global score, obstacles, player, obstacle_speed, spawn_probability, player_speed, power_ups, speed_boost_duration, slowdown_duration, level

    score = 0
    level = 1
    obstacles = []
    power_ups = []
    player_speed = original_player_speed
    speed_boost_duration = 0
    slowdown_duration = 0
    player = pygame.Rect(player_x, player_y, player_size, player_size)

    clock = pygame.time.Clock()
    while True:
        screen.blit(background, (0, 0))

        # Level
        if score >= level * 25:
            level += 1
            print(f"Level Up! Current Level: {level}")

        # Display score and level
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Handle events (key presses, window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Move the player within the window boundaries
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < 750:  
            player.x += player_speed
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y < 550: 
            player.y += player_speed

        # Randomly spawn obstacles
        if random.random() < spawn_probability:
            spawn_obstacle()

        # Randomly spawn power-ups
        if random.random() < 0.01: 
            spawn_power_up()

        # obstacles downwards and remove off-screen
        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            if obstacle.y > 600:
                obstacles.remove(obstacle)
                score += 1  

            # Crush between player and obstacles
            if player.colliderect(obstacle):
                game_over_screen()

        # Move power-ups downwards
        for power_up, power_type in power_ups[:]:
            power_up.y += power_up_speed
            if power_up.y > 600:
                power_ups.remove((power_up, power_type))
            if player.colliderect(power_up):
                if power_type == SPEED_BOOST:
                    speed_boost_duration = 20  
                    player_speed = 10 
                elif power_type == SLOWDOWN:
                    slowdown_duration = 20  
                    player_speed = 2 
                power_ups.remove((power_up, power_type))

        # Draw the player (red square)
        if speed_boost_duration > 0:
            pygame.draw.rect(screen, BOOST_COLOR, player)  
        elif slowdown_duration > 0:
            pygame.draw.rect(screen, SLOW_COLOR, player) 
        else:
            pygame.draw.rect(screen, RED, player) 

        # Draw obstacles (green squares)
        for obstacle in obstacles:
            pygame.draw.rect(screen, GREEN, obstacle)

        # Draw power-ups
        for power_up, power_type in power_ups:
            if power_type == SPEED_BOOST:
                pygame.draw.rect(screen, BLUE, power_up)
            elif power_type == SLOWDOWN:
                pygame.draw.rect(screen, SLOW_COLOR, power_up)

        # Render the score text and display it on the screen
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10)) 
        
        # Apply speed boost or slowdown effects
        if speed_boost_duration > 0:
            speed_boost_duration -= 1
            if speed_boost_duration == 0:
                player_speed = original_player_speed

        if slowdown_duration > 0:
            slowdown_duration -= 1
            if slowdown_duration == 0:
                player_speed = original_player_speed

        pygame.display.flip()

        clock.tick(60)

# Game Over
def game_over_screen():
    pygame.mixer.music.stop()
    game_over_sound.play()
    global score, level
    save_score()

    while True:
        screen.fill(BLACK)

        # Game Over and score
        game_over_text = large_font.render("Game Over!", True, WHITE)
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(game_over_text, (300, 200))
        screen.blit(score_text, (300, 250))

        # Try Again and Main Menu buttons
        try_again_text = font.render("Press 'R' to Try Again", True, WHITE)
        main_menu_text = font.render("Press 'M' to Main Menu", True, WHITE)
        screen.blit(try_again_text, (300, 300))
        screen.blit(main_menu_text, (300, 350))

        # Handle events for restarting or going to the main menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()  
                elif event.key == pygame.K_m:
                    main_menu()  

        pygame.display.flip()

# Start main menu
main_menu()
