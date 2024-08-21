import random
import sqlite3
from constants import *


class Player:
    def __init__(self, name):
        self.name = name
        self.image = player_img
        self.score = 0 
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.speed = 12
        self.bullets = []

    def move(self, dx, dy):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - self.image.get_width():
            self.x = WIDTH - self.image.get_width()

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        
    def shoot(self):
        bullet = Bullet(self.x + self.image.get_width() // 2, self.y)
        self.bullets.append(bullet)

class Enemy:
    def __init__(self, speed):
        self.image = enemy_img
        self.x = random.randint(0, WIDTH - self.image.get_width())
        self.y = random.randint(-100, -40)
        self.speed = speed

    def draw(self):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.speed

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.x = x
        self.y = y
        self.speed = 10

    def draw(self):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.speed


class Database:
    def __init__(self, db_name="scores.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)"
            )

    def insert_score(self, player):
        with self.connection:
            self.connection.execute(
                "INSERT INTO scores (name, score) VALUES (?, ?)",
                (player.name, player.score)
            )

    def get_top_scores(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
        return cursor.fetchall()