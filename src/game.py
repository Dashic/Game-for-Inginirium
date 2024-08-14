import pygame
from classes import *

pygame.init()

def main():
    name = input("Введите ваше имя: ")
    player = Player(name)
    db = Database()
    run = True
    clock = pygame.time.Clock()
    enemies = [Enemy(1) for i in range(5)]
    missed_enemies = 0
    killed_enemies = 0
    enemy_speed = 1

    while run:
        clock.tick(30)
        win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed, -12)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed, 12)
        if keys[pygame.K_SPACE]:
            player.shoot()

        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                player.bullets.remove(bullet)

        for enemy in enemies[:]:
            enemy.move()
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies.append(Enemy(enemy_speed))
                missed_enemies += 1
                if missed_enemies >= 5:
                    run = False
            for bullet in player.bullets[:]:
                if (enemy.x < bullet.x < enemy.x + enemy.image.get_width() and
                        enemy.y < bullet.y < enemy.y + enemy.image.get_height()):
                    enemies.remove(enemy)
                    player.bullets.remove(bullet)
                    enemies.append(Enemy(enemy_speed))
                    killed_enemies += 1
                    break
        score = killed_enemies
                

        if killed_enemies % 20 == 0 and killed_enemies > 0:
            enemy_speed += 0.02

        player.draw()
        for bullet in player.bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {killed_enemies}', True, WHITE)
        win.blit(score_text, (10, 10))

        pygame.display.update()

    win.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    score_text = font.render(f'Score: {killed_enemies}', True, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + text.get_height()))
    pygame.display.update()
    pygame.time.wait(3000)

    pygame.quit()


    db.insert_score(player)

    top_scores = db.get_top_scores()
    print("\nТоп-5 игроков:")
    for idx, (name, score) in enumerate(top_scores, start=1):
        print(f"{idx}. {name} - {score} очков")

    pygame.quit()

if __name__ == "__main__":
    main()