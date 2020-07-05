import pygame
clock = pygame.time.Clock()

def fill_point(color, display, x, y):
    COLOR = color
    pygame.draw.rect(display, COLOR, (x * 20 - 20, y * 20 - 20 , 19, 19))
    pygame.display.update((x*20 - 20, y*20 - 20, 19, 19))
    clock.tick(400)
    

def get_near(board, point):
    #Example (5,3)
    near = []
    if point[0] > 1:
        near.append((point[0] - 1, point[1])) #For the example (4, 3)
    if point[1] > 1:
        near.append((point[0], point[1] - 1)) #For the example (5, 2)
    if point[1] < len(board):
        near.append((point[0], point[1] + 1)) # For the example (6, 3)
    if point[0] < len(board[point[1] - 1]):
        near.append((point[0] + 1, point[1])) #For the example (5, 4)
    real_near = []
    for point_near in near:
        if not board[point_near[1] - 1][point_near[0] - 1] == 1:
            real_near.append(point_near)
    return real_near

def find_path(display, board, start, exit_point):
    queue = [(start, [])]
    visited = []
    time = 0 
    
    while len(queue) > 0:
        point, path = queue.pop(0)
        if not point == start:
            fill_point((0, 255, 255), display, point[0], point[1])
        path.append(point) #The point is now part of the path
        visited.append(point)

        if point == exit_point:
            return path
        
        near_points = get_near(board, point)
        for near_point in near_points:
            if not (near_point in visited):
                visited.append(near_point)
                queue.append((near_point, path[:]))
    return None


def main():
    print ("First draw your obsticales, press enter, and then draw the start point and the end point")
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    current_x = 0
    current_y = 0
    for i in range(30):
        for j in range(40):
            pygame.draw.rect(display, WHITE, (current_x, current_y, 20, 20))
            pygame.draw.rect(display, BLACK, (current_x + 19, current_y, 2, 20))
            pygame.draw.rect(display, BLACK, (current_x, current_y + 19, 20, 2))
            current_x += 20
        current_y += 20
        current_x = 0
    
    pygame.display.flip()
    
    board = []
    for i in range(30):
        new_list = []
        for j in range (40):
            new_list.append(0)
        board.append(new_list)


    ISMOUSEDOWN = False
    BREAK = False
    #Draw obsticales
    while True:
        clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ISMOUSEDOWN = True
            if event.type == pygame.MOUSEBUTTONUP:
                ISMOUSEDOWN = False
            if event.type == pygame.KEYDOWN:
                BREAK = True
        if ISMOUSEDOWN:
            possition = pygame.mouse.get_pos()
            point = (possition[0] // 20 + 1, possition[1] // 20 + 1)
            fill_point((255, 0, 255), display, point[0], point[1])
            board[point[1] - 1][point[0] - 1] = 1
        if BREAK:
            break
    
    #Draw Start and End:
    Start = 0
    End = 0
    BREAK = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                possition = pygame.mouse.get_pos()
                point = (possition[0] // 20 + 1, possition[1] // 20 + 1)
                Start = point
                BREAK = True
        if BREAK:
            break
    fill_point((0, 0, 0), display, Start[0], Start[1])
    BREAK = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                possition = pygame.mouse.get_pos()
                point = (possition[0] // 20 + 1, possition[1] // 20 + 1)
                End = point
                BREAK = True
        if BREAK:
            break
                

    fill_point((0, 0, 0), display, End[0], End[1])
    path = find_path(display, board, Start, End)
    if path == None:
        print ("A path could not be found")
    else:
        for point in path:
            fill_point((0, 0, 0), display, point[0], point[1])

if __name__ == "__main__":
    main()
