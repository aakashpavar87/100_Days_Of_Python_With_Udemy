enemies = "Skeleton"
def increase_enemies():
    global enemies
    print(f"Before increase enemies {enemies}")
    enemies = "Skeleton Alien"
    print(enemies)
increase_enemies()