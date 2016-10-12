###pygame
import pygame
import random
import sys
from pygame.locals import *

pygame.init()

gameWindow = pygame.display.set_mode((800,600))

pygame.display.set_caption('Game Attempt One')

crashed = False

colorsrand = random.randint(0,254)

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
	else:return False
def die(screen, score):
	f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0));screen.blit(t, (10, 270));
	pygame.display.update();
	pygame.time.wait(2000);
	sys.exit(0)
xs = [290, 290, 290, 290, 290];
ys = [290, 270, 250, 230, 210];
dirs = 0;
score = 0;
dotlocation = (random.randint(0, 780), random.randint(0, 780));
pygame.init();
s = pygame.display.set_mode((800, 800));
pygame.display.set_caption('Snake');
dotinfo = pygame.Surface((10, 10));
dotinfo.fill((colorsrand, colorsrand, colorsrand));
img = pygame.Surface((20, 20));img.fill((0, 0, 255));
f = pygame.font.SysFont('Arial', 20, bold=True, italic=False);
clock = pygame.time.Clock()
while not crashed:
	clock.tick(10)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			crashed = True
		elif e.type == KEYDOWN:
			if e.key == K_UP and dirs != 0:dirs = 2
			elif e.key == K_DOWN and dirs != 2:dirs = 0
			elif e.key == K_LEFT and dirs != 1:dirs = 3
			elif e.key == K_RIGHT and dirs != 3:dirs = 1
	i = len(xs)-1
	while i >= 2:
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):die(s, score)
		i-= 1
	if collide(xs[0], dotlocation[0], ys[0], dotlocation[1], 20, 10, 20, 10):score+=1;xs.append(790);ys.append(790);dotlocation=(random.randint(0,790),random.randint(0,790))

	if xs[0] < 0 or xs[0] > 790 or ys[0] < 0 or ys[0] > 790: die(s, score)
	i = len(xs)-1
	while i >= 1:
		xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
	if dirs==0:ys[0] += 20
	elif dirs==1:xs[0] += 20
	elif dirs==2:ys[0] -= 20
	elif dirs==3:xs[0] -= 20	
	s.fill((255, 255, 255))	
	for i in range(0, len(xs)):
		s.blit(img, (xs[i], ys[i]))
	s.blit(dotinfo, dotlocation);t=f.render(str(score), True, (0, 0, 0));s.blit(t, (10, 10));pygame.display.update()

pygame.quit()
quit()