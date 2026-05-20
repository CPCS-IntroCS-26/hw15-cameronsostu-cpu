import pgzrun
WIDTH = 800
HEIGHT = 1000

# Player variables
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False

# Platforms
platforms = [
    Rect((0, 470), (750, 30)), # the first floor
    Rect((0,970), (800, 30)),
    Rect((200, 380), (150, 20)),
    Rect((450, 300), (150, 20)),
    Rect((650, 220), (100, 20)),
    Rect((0, 250), (120, 20)),
    Rect((400, 100), (120, 20)),
   Rect((150, 150), (120, 20)),
    Rect((0,50), (120, 20)),
    # bottom floor
    Rect((300, 820), (300, 20) ),
    Rect((700, 850), (80, 20)),
    Rect((450, 740), (50, 20)),
    Rect((430, 640), (90, 20)),
    Rect((50, 750,), (100,20)),
    Rect((200, 620),(150,20))
]

# Collectibles
coins = [
    Rect((250, 340), (20, 20)),
    Rect((500, 260), (20, 20)),
    Rect((690, 180), (20, 20)),
    Rect((465, 720), (20, 20)),
    Rect((100, 850), (20, 20)),
    Rect((20, 180), (20, 20)),
    Rect((50, 20), (20, 20)),
    Rect((450, 20), (20, 20)),
    Rect((275, 570), (20,20))
    ]
    
score = 0
lives = 3

# Hazards and goal
lavas =  [
    
    Rect((350, 450), (100, 20)),
    Rect((600,820), (20, 150)),
    Rect((450,450), (50, 200)),
    Rect((450, 750), (50,70)),
    Rect((100,250), (20,100)),
    Rect((0,800),(200, 20)),
    Rect((200,800), (20,130))


]

goal = Rect((530, 900), (40, 50 ))
game_won = False
game_over = False

def draw():
    screen.clear()
    screen.draw.filled_rect(player, "aqua")

    for platform in platforms:
        screen.draw.filled_rect(platform, "saddlebrown")

    for coin in coins:
        screen.draw.filled_rect(coin, "yellow")
    
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    screen.draw.text(f"Lives: {lives}", (100, 10), fontsize=30, color="white")
    for lava in lavas:
        screen.draw.filled_rect(lava, "red")
    screen.draw.filled_rect(goal, "indigo")
    if game_won and score > 8:
        screen.clear()
        screen.draw.text("You Win!", center=(400, 250), fontsize=60, color="yellow")
    if game_over:
        screen.clear()
        screen.draw.text("Game Over!", center=(400, 250), fontsize=60, color="red")
def update():
    global velocity_y, on_ground, score, game_won, lives, game_over
    velocity_y += gravity
    player.y += velocity_y

    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH
    
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    if keyboard.space and on_ground:
        velocity_y = -15
        on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
    for lava in lavas[:]:
        if player.colliderect(lava):
            player.x = 100
            player.y = 400
            velocity_y = 0
            lives -= 1
    if lives == 0:
        game_over = True
    if player.colliderect(goal):
        game_won = True
pgzrun.go()








