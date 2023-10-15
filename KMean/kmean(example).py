import pygame
from random import randint
import math
from sklearn.cluster import KMeans

def distance(x1, x2):
    return math.sqrt((x1[0]-x2[0])*(x1[0]-x2[0])+(x1[1]-x2[1])*(x1[1]-x2[1]))

pygame.init()

running = True

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("K-mean Tri Ne")

BACKGROUND = (214, 214, 214)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

K = 0
error = 0
COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]
points = []
clusters = []
labels = []

font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_tru = font.render('-', True, WHITE)
text_run = font.render('RUN', True, WHITE)
text_random = font.render('RANDOM', True, WHITE)
text_algorithm = font.render('ALGORITHM', True, WHITE)
text_reset = font.render('RESET', True, WHITE)

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    #Draw panel
    pygame.draw.rect(screen, BLACK, (34, 36, 883, 622))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (39, 41, 872, 609))

    #Draw button

    pygame.draw.rect(screen, BLACK, (930, 38, 53, 50))
    screen.blit(text_plus, (945, 37))

    pygame.draw.rect(screen, BLACK, (1002, 38, 53, 50))
    screen.blit(text_tru, (1020, 37))

    text_K = font.render('K = ' + str(K), True, BLACK)
    screen.blit(text_K, (1068, 37))

    text_error = font.render('ERROR = ' + str(int(error)), True, BLACK)
    screen.blit(text_error, (933, 325))

    pygame.draw.rect(screen, BLACK, (930, 138, 238, 50))
    screen.blit(text_run, (1000, 139))

    pygame.draw.rect(screen, BLACK, (930, 229, 238, 50))
    screen.blit(text_random, (967, 235))

    pygame.draw.rect(screen, BLACK, (930, 411, 238, 50))
    screen.blit(text_algorithm, (955, 410))

    pygame.draw.rect(screen, BLACK, (930, 518, 238, 50))
    screen.blit(text_reset, (982, 519))
    #End draw
    mx, my = pygame.mouse.get_pos()
    #create pos
    if 34 <=mx <=917 and 36 <= my <= 658:
        text_mouse = font_small.render("(" + str(mx-34) + "," + str(my-36) + ")", True, BLACK)
        screen.blit(text_mouse, (mx + 10, my))
    #Create application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Create point
            labels = []
            if 39 <= mx <= 911 and 41 <= my <= 650:
                point = [mx,my]
                points.append(point)
                print("create points")
            elif 930 <= mx <= 983 and 38 <= my <= 88:
                if K < 9: K+=1
                print("pressed K+")
            elif 1002 <= mx <= 1055 and 38 <= my <= 88:
                if K > 0: K-=1
                print("pressed K-")
            elif 930 <= mx <= 1168 and 138 <= my <= 188 and clusters != []:
                #Calcu color points
                labels = []
                for i in range(len(points)):
                    distance_cluster = []
                    for j in range(len(clusters)):
                        dis = int(distance(clusters[j],points[i]))
                        distance_cluster.append(dis)
                    min_dis = min(distance_cluster)
                    label = distance_cluster.index(min_dis)
                    labels.append(label)
                #Move cluster
                for i in range(K):
                    sumx = 0
                    sumy = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            count += 1
                            sumx += points[j][0]
                            sumy += points[j][1]
                    if count != 0: clusters[i] = [int(sumx/count),int(sumy/count)]
                #Calcu Error
                error = 0
                if labels != [] and clusters!=[] and points != []:
                    for i in range(len(points)):
                        error += distance(points[i], clusters[labels[i]])
                print("pressed run")
            elif 930 <= mx <= 1168 and 229 <= my <= 279:
                #Create random cluster
                clusters = []
                error = 0
                for i in range(K):
                    new_cluster = [randint(39+6, 911-6), randint(41+6, 650-6)]
                    clusters.append(new_cluster)
                print("pressed random")
            elif 930 <= mx <= 1168 and 411 <= my <= 461 and K!=0 and points != [] :
                kmeans = KMeans(n_clusters=K).fit(points)
                #print(kmeans.cluster_centers_) #in toa do cua cluster
                clusters = kmeans.cluster_centers_ #dua toa do cua ham vao list clusters cua minh
                labels = kmeans.predict(points) #tim thu tu cluster maf point thuoc vao va tra ve 1,2,3...gi day
                print("pressed algorithm")
            elif 930 <= mx <= 1168 and 518 <= my <= 568:
                #Clear data
                clusters = []
                points = []
                labels = []
                error = 0
                K = 0
                print("pressed reset")

    #Draw cluster
    for i in range(len(clusters)):
        pygame.draw.circle(screen,COLORS[i],(clusters[i][0],clusters[i][1]),12)
    # Draw point and change color points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0], points[i][1]), 6)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0], points[i][1]), 4)
        else:
            for c in clusters:
                pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0], points[i][1]), 4)
    pygame.display.flip()

pygame.quit()