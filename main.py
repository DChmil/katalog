from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import pygame

if __name__ == '__main__':
    print(calculate_salary(3, 13))
    get = get_employees()
    print(datetime.datetime.now().strftime("%Y-%m-%d"))
    pygame.init()

    window_size = (300, 300)
    pygame.display.set_caption("Синий фон")
    screen = pygame.display.set_mode(window_size)
    background_color = (0, 0, 255)
    screen.fill(background_color)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()