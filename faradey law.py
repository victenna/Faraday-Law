import pygame,sys
pygame.init()
screen = pygame.display.set_mode((1200,900))
clock = pygame.time.Clock()
BLACK=(255,255,255)
font = pygame.font.SysFont('Corbel',35)
text = font.render('Start' , True , BLACK)
Q=5
images=['img0.png','img1.png','img2.png','img3.png','img4.png']
x,y=[590,600,600,540,800],[425,350,350,395,800]
img=[0]*Q
rect=[0]*Q
a,angle,i,delta=0,0,0,5
X,Y=800,800# start_stop button position

def button():
    global a
    mouse=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if abs(mouse[0] - X)<50 and abs(mouse[1] - Y) <50: a=1
def position(q1,q2,m):
    x[1]=x[1]+q1*delta
    y[1]=y[1]+q2*2*delta
    x[2]=x[2]+q1*delta
    y[2]=y[2]+q2*2*delta
    x[3]=x[3]+q1*delta
    y[3]=y[3]+q2*2*delta
    base(m,350,460,0)
    base(0,1132,577,0)
    base(3,450,360,0)
def base(i,scalex,scaley,angle):
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    rect[i]=img[i].get_rect(center=(x[i],y[i]))
    screen.blit(img[i],rect[i])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button()

    screen.fill((128,128,128))
    pygame.draw.rect(screen,(183,168,249), (X, Y,100,50))
    screen.blit(text,(X+10,Y+5))

    if a==0:
        base(1,350,460,0)
        base(0,1132,577,0)
        base(3,450,360,0)

    if a==1:
        pygame.draw.rect(screen,((128,128,128)), (X, Y,100,50))
        i=i+1
        i1=i%60
        if i1<2: position(-1,1,1)
        if i1>1 and i1<25: position(-1,1,2)
        if i1>24 and i1<30: position(-1,1,1)
        if i1>29 and i1<40: position(1,-1,1)
        if i1>39: position(1,-1,2)
    clock.tick(10)
    pygame.display.update()
