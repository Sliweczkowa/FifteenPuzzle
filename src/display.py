import sys
import pygame

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAME_SIZE = 400
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 30
FONT_SIZE = 48  # Set font size to a larger value

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Sample frames (replace with actual frames)
frames = [
    [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],
    [3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15],
    [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15],
    [1, 2, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15],
    # Add more frames as needed
]

# Initialize variables
current_frame_index = 0

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frame Viewer")
font = pygame.font.Font(None, FONT_SIZE)

def draw_frame(frame):
    screen.fill(WHITE)
    frame_x = (WINDOW_WIDTH - FRAME_SIZE) // 2
    frame_y = (WINDOW_HEIGHT - FRAME_SIZE) // 2
    for i in range(4):
        for j in range(4):
            value = frame[i * 4 + j]
            rect = pygame.Rect(frame_x + j * (FRAME_SIZE // 4), frame_y + i * (FRAME_SIZE // 4), FRAME_SIZE // 4, FRAME_SIZE // 4)
            pygame.draw.rect(screen, GRAY, rect, 1)
            if value != 0:
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def draw_buttons():
    prev_button = pygame.Rect(10, WINDOW_HEIGHT - 100 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    next_button = pygame.Rect(WINDOW_WIDTH - BUTTON_WIDTH - 10, WINDOW_HEIGHT - 100 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, prev_button)
    pygame.draw.rect(screen, GRAY, next_button)
    prev_text = font.render("<", True, BLACK)
    next_text = font.render(">", True, BLACK)
    screen.blit(prev_text, prev_button.center)
    screen.blit(next_text, next_button.center)
    return prev_button, next_button

def draw_text_input():
    input_box = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 50, 100, 30)
    pygame.draw.rect(screen, GRAY, input_box)
    index_text = font.render(str(current_frame_index), True, BLACK)
    screen.blit(index_text, input_box.center)
    return input_box

def main():
    global current_frame_index
    clock = pygame.time.Clock()
    input_active = False
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if prev_button.collidepoint(event.pos):
                    current_frame_index = max(0, current_frame_index - 1)
                elif next_button.collidepoint(event.pos):
                    current_frame_index = min(len(frames) - 1, current_frame_index + 1)
                elif input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    try:
                        current_frame_index = int(input_text)
                        current_frame_index = max(0, min(len(frames) - 1, current_frame_index))
                    except ValueError:
                        pass
                    input_text = ""
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)
        draw_frame(frames[current_frame_index])
        prev_button, next_button = draw_buttons()
        input_box = draw_text_input()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()