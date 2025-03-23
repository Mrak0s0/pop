import pygame

import math

pygame.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

def update(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, images, x, y, w, h, speed):

        self.images = images
        self.target_x = x
        self.target_y = y
        self.moving = False

    def move_to(self, x, y, direction):
        self.target_x = x
        self.target_y = y
        self.moving = True
        self.image = self.images[direction]

    def update(self, screen):
        if self.moving:
            dx = self.target_x - self.rect.x
            dy = self.target_y - self.rect.y
            distance = math.hypot(dx, dy)

            if distance > self.speed:
                self.rect.x += self.speed * (dx / distance)
                self.rect.y += self.speed * (dy / distance)

            else:
                self.rect.x, self.rect.y = self.target_x, self.target_y
                self.moving = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

width = 1280
height = 720

font = pygame.font.Font("20443.otf", 30)
locations = {
"forest": [
    {"text": "Пойти налево", "x": 350, "y": 575, "action": "go_left"}
],

"hijina": [
    {"text": "Пойти направо", "x": 900, "y": 600, "action": "go_right"}
]
}

current_location = "forest"

amplitude = 5

clock = pygame.time.Clock()
window_size = (width, height)
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

player_x = 600
player_y = 560

player_images = {
"idle": pygame.image.load("lol.png"),
"left": pygame.image.load("lol.png"),
}

try:
    fon = pygame.image.load('fon.jpg')
    next_fon = pygame.image.load('fon.jpg')
    player = Player(player_images, player_x, player_y, 49, 106, 3)
    play_button = pygame.image.load("lol.png")
    settings_button = pygame.image.load("lol.png")
    quit_button = pygame.image.load("lol.png")
    fon_menu = pygame.transform.scale(pygame.image.load("fon.jpg"), (1280, 720))

except pygame.error as e:
    print(f"Ошибка загрузки изображений: {e}")
    pygame.quit()
    exit()

buttons = [

{"sprite": play_button, "rect": play_button.get_rect(center=(640, 300)), "action": "play"},

{"sprite": settings_button, "rect": settings_button.get_rect(center=(640, 400)), "action": "settings"},

{"sprite": quit_button, "rect": quit_button.get_rect(center=(640, 500)), "action": "quit"},

]

run = True

in_menu = True

while run:

    while in_menu:
        window.blit(fon_menu, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            window.blit(button["sprite"], button["rect"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_menu = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        if button["action"] == "play":
                            print("Переход в игру")
                            in_menu = False
                            break

                        elif button["action"] == "settings":
                            print("Переход в настройки")

                        elif button["action"] == "quit":
                            pygame.quit()
                            exit()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    for item in locations[current_location]:
                        if "rect" in item and item["rect"].collidepoint(mouse_pos):
                            if item["action"] == "go_left":
                                player.move_to(800, 525, "left")
                            elif item["action"] == "go_right":
                                player.move_to(600, 560, "right")

        pygame.display.update()

        clock.tick(60)



