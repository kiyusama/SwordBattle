import pygame

pygame.init()

width = 700
height = 700
charawid = 100
charahei = 100
pos_1px = width * 0.40
pos_1py = height * 0.40
pos_2px = width * 0.60
pos_2py = height * 0.60
life1p = 3
life2p = 3
FrameCount = 0
attackframe1p = 0
attackframe2p = 0
attackframecount1p = 0
attackframecount2p = 0
hitcount1p = 0
hitcount2p = 0
backgroundcolor = (46,139,87)
FPS = 60
clock = pygame.time.Clock()

moving1p = False
moving2p = False
attacking1p = False
attacking2p = False
guarding1p = False
guarding2p = False
hit1p = False
hit2p = False
invincible1p = False
invincible2p = False
atsoundplayed1p = False
atsoundplayed2p = False
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("1p:F,G 2p:K,L")

soundattack = pygame.mixer.Sound("Python/Game/assets/soundattack.mp3")
soundattack.set_volume(0.2)
soundhit = pygame.mixer.Sound("Python/Game/assets/soundhit.mp3")
soundhit.set_volume(0.2)
soundguard = pygame.mixer.Sound("Python/Game/assets/soundguard.mp3")

img_ground = pygame.transform.scale(pygame.image.load("Python/Game/assets/ground.png"), (width, height))

img_heart1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/heart1.png"), (75, 75))
img_heart2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/heart2.png"), (75, 75))

img_attack1p_1 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack1p_1_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack1p_2 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack1p_2_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack1p_3 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack1p_3_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack1p_4 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack1p_4_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack2p_1 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack2p_1_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack2p_2 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack2p_2_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack2p_3 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack2p_3_{i}.png"), (charawid, charahei)) for i in range(1, 4)]
img_attack2p_4 = [pygame.transform.scale(pygame.image.load(f"Python/Game/assets/attack2p_4_{i}.png"), (charawid, charahei)) for i in range(1, 4)]

img_idle1p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle1p_1.png"), (charawid, charahei))
img_idle1p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle1p_2.png"), (charawid, charahei))
img_idle1p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle1p_3.png"), (charawid, charahei))
img_idle1p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle1p_4.png"), (charawid, charahei))
img_move1p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move1p_1.png"), (charawid, charahei))
img_move1p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move1p_2.png"), (charawid, charahei))
img_move1p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move1p_3.png"), (charawid, charahei))
img_move1p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move1p_4.png"), (charawid, charahei))
img_guard1p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard1p_1.png"), (charawid, charahei))
img_guard1p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard1p_2.png"), (charawid, charahei))
img_guard1p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard1p_3.png"), (charawid, charahei))
img_guard1p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard1p_4.png"), (charawid, charahei))

img_idle2p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle2p_1.png"), (charawid, charahei))
img_idle2p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle2p_2.png"), (charawid, charahei))
img_idle2p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle2p_3.png"), (charawid, charahei))
img_idle2p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/idle2p_4.png"), (charawid, charahei))
img_move2p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move2p_1.png"), (charawid, charahei))
img_move2p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move2p_2.png"), (charawid, charahei))
img_move2p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move2p_3.png"), (charawid, charahei))
img_move2p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/move2p_4.png"), (charawid, charahei))
img_guard2p_1 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard2p_1.png"), (charawid, charahei))
img_guard2p_2 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard2p_2.png"), (charawid, charahei))
img_guard2p_3 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard2p_3.png"), (charawid, charahei))
img_guard2p_4 = pygame.transform.scale(pygame.image.load("Python/Game/assets/guard2p_4.png"), (charawid, charahei))

pygame.display.set_icon(img_idle1p_2)

def action1p (pos_1px, pos_1py, moving1p, attacking1p, guarding1p, life1p):
    keys = pygame.key.get_pressed()  
    if not attacking1p and not guarding1p:
        if 0 <= pos_1px <= width and 0<= pos_1py <= height:
            if keys[pygame.K_d]:
                moving1p = True
                pos_1px += 2
            if keys[pygame.K_a]:
                moving1p = True
                pos_1px -= 2
            if keys[pygame.K_w]:
                moving1p = True
                pos_1py -= 2
            if keys[pygame.K_s]:
                moving1p = True
                pos_1py += 2   
    
        
    if pos_1px > width:
        soundhit.play()
        life1p -= 1
        pos_1px -= 50
        #pos_1py = height * 0.40
    elif pos_1px < 0:
        soundhit.play()
        life1p -= 1
        pos_1px += 50
        #pos_1py = height * 0.40
    elif pos_1py > height:
        soundhit.play()
        life1p -= 1
        #pos_1px = width * 0.40
        pos_1py -= 50
    elif pos_1py < 0:
        soundhit.play()
        life1p -= 1
        #pos_1px = width * 0.40
        pos_1py += 50
    if keys[pygame.K_g]:
        attacking1p = True
    if keys[pygame.K_f]:
        guarding1p = True
    return pos_1px, pos_1py, moving1p, attacking1p, guarding1p, life1p

def action2p (pos_2px, pos_2py, moving2p, attacking2p, guarding2p, life2p):
    keys = pygame.key.get_pressed()
    if not attacking2p and not guarding2p: 
        if 0 <= pos_2px <= width and 0<= pos_2py <= height:
            if keys[pygame.K_RIGHT]:
                moving2p = True
                pos_2px += 2
            if keys[pygame.K_LEFT]:
                moving2p = True
                pos_2px -= 2
            if keys[pygame.K_UP]:
                moving2p = True
                pos_2py -= 2
            if keys[pygame.K_DOWN]:
                moving2p = True
                pos_2py += 2
         
    if pos_2px > width:
        soundhit.play()
        life2p -= 1
        pos_2px -= 50
        #pos_2py = height * 0.60
    elif pos_2px < 0:
        soundhit.play()
        life2p -= 1
        pos_2px += 50
        #pos_2py = height * 0.60
    elif pos_2py > height:
        soundhit.play()
        life2p -= 1
        #pos_2px = width * 0.60
        pos_2py -= 50
    elif pos_2py < 0:
        soundhit.play()
        life2p -= 1
        #pos_2px = width * 0.60
        pos_2py += 50
    if keys[pygame.K_l]:
        attacking2p = True
    if keys[pygame.K_k]:
        guarding2p = True
    return pos_2px, pos_2py, moving2p, attacking2p, guarding2p, life2p


running = True


while running:

    window.blit(img_ground, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            moving1p = False
            moving2p = False
            guarding1p = False
            guarding2p = False
    
    pos_1px, pos_1py, moving1p, attacking1p, guarding1p, life1p= action1p(pos_1px, pos_1py, moving1p, attacking1p, guarding1p, life1p)
    pos_2px, pos_2py, moving2p, attacking2p, guarding2p, life2p= action2p(pos_2px, pos_2py, moving2p, attacking2p, guarding2p, life2p)

    FrameCount += 1

    dx1p = pos_2px - pos_1px
    dy1p = pos_2py - pos_1py
    distance1p = (dx1p**2 + dy1p**2)**0.5
    dx1p /= distance1p
    dy1p /= distance1p
    dx1p *= 5
    dy1p *= 5

    dx2p = pos_1px - pos_2px
    dy2p = pos_1py - pos_2py
    distance2p = (dx2p**2 + dy2p**2)**0.5
    dx2p /= distance2p
    dy2p /= distance2p
    dx2p *= 5
    dy2p *= 5

    if attacking1p:

        if pos_1px >= pos_2px and pos_1py < pos_2py:
            window.blit(img_attack1p_1[attackframe1p], (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px < pos_2px and pos_1py <= pos_2py:
            window.blit(img_attack1p_2[attackframe1p], (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px <= pos_2px and pos_1py > pos_2py:
            window.blit(img_attack1p_3[attackframe1p], (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px > pos_2px and pos_1py >= pos_2py:
            window.blit(img_attack1p_4[attackframe1p], (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        
        if attackframecount1p % 10 == 9:
            attackframe1p += 1

        if attackframe1p >= len(img_attack1p_1):
            attackframe1p = 0
            attacking1p = False
            atsoundplayed1p = False
            

        if attackframe1p == 1:
            pos_1px += dx1p
            pos_1py += dy1p


            
            if distance1p <= charawid * 0.5 * 0.75 + 10:
                hit2p = True
                
                if not guarding2p and not invincible2p:
                    life2p -= 1
                    attacking2p = False
                    guarding2p = False
                    soundhit.play()
                elif guarding2p:
                    soundguard.play()
            if not atsoundplayed1p:
                soundattack.play()
                atsoundplayed1p = True
            

        attackframecount1p += 1
        
            
    if attacking2p:
        if pos_1px >= pos_2px and pos_1py < pos_2py:
            window.blit(img_attack2p_3[attackframe2p], (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px < pos_2px and pos_1py <= pos_2py:
            window.blit(img_attack2p_4[attackframe2p], (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px <= pos_2px and pos_1py > pos_2py:
            window.blit(img_attack2p_1[attackframe2p], (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px > pos_2px and pos_1py >= pos_2py:
            window.blit(img_attack2p_2[attackframe2p], (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        
        if attackframecount2p % 10 == 9:
            attackframe2p += 1

        if attackframe2p >= len(img_attack2p_1):
            attackframe2p = 0
            attacking2p = False
            atsoundplayed2p = False

        if attackframe2p == 1:

            pos_2px += dx2p
            pos_2py += dy2p

            if distance2p <= charawid * 0.5 * 0.75 + 10:
                hit1p = True
                
                if not guarding1p and not invincible1p:
                    life1p -= 1
                    attacking1p = False
                    guarding1p = False
                    soundhit.play()
                elif guarding1p:
                    soundguard.play()

            if not atsoundplayed2p:
                soundattack.play()
                atsoundplayed2p = True
            

        attackframecount2p += 1

    if guarding1p and not attacking1p:
        if pos_1px >= pos_2px and pos_1py < pos_2py:
            window.blit(img_guard1p_1, (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px < pos_2px and pos_1py <= pos_2py:
            window.blit(img_guard1p_2, (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px <= pos_2px and pos_1py > pos_2py:
            window.blit(img_guard1p_3, (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
        if pos_1px > pos_2px and pos_1py >= pos_2py:
            window.blit(img_guard1p_4, (pos_1px - charawid / 2,pos_1py - charahei / 2)) 
    if guarding2p and not attacking2p:
        if pos_1px >= pos_2px and pos_1py < pos_2py:
            window.blit(img_guard2p_3, (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px < pos_2px and pos_1py <= pos_2py:
            window.blit(img_guard2p_4, (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px <= pos_2px and pos_1py > pos_2py:
            window.blit(img_guard2p_1, (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
        if pos_1px > pos_2px and pos_1py >= pos_2py:
            window.blit(img_guard2p_2, (pos_2px - charawid / 2,pos_2py - charahei / 2)) 
    

    if hit2p and hitcount2p <= 7:
        invincible2p = True
        hitcount2p += 1
        pos_2px -= dx2p * 3
        pos_2py -= dy2p * 3
        if hitcount2p == 7:
            hitcount2p = 0
            hit2p = False
            invincible2p = False
        
    if hit1p and hitcount1p <= 7:
        invincible1p = True
        hitcount1p += 1
        pos_1px -= dx1p * 3
        pos_1py -= dy1p * 3
        if hitcount1p == 7:
            hitcount1p = 0
            hit1p = False
            invincible1p = False


        
    if not guarding1p and not attacking1p:
        if moving1p:
            if FrameCount % 20 < 10:
                if pos_1px >= pos_2px and pos_1py < pos_2py:
                    window.blit(img_idle1p_1, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px < pos_2px and pos_1py <= pos_2py:
                    window.blit(img_idle1p_2, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px <= pos_2px and pos_1py > pos_2py:
                    window.blit(img_idle1p_3, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px > pos_2px and pos_1py >= pos_2py:
                    window.blit(img_idle1p_4, (pos_1px - charawid / 2,pos_1py - charahei / 2))    
            else:
                if pos_1px >= pos_2px and pos_1py < pos_2py:
                    window.blit(img_move1p_1, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px < pos_2px and pos_1py <= pos_2py:
                    window.blit(img_move1p_2, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px <= pos_2px and pos_1py > pos_2py:
                    window.blit(img_move1p_3, (pos_1px - charawid / 2,pos_1py - charahei / 2))
                if pos_1px > pos_2px and pos_1py >= pos_2py:
                    window.blit(img_move1p_4, (pos_1px - charawid / 2,pos_1py - charahei / 2))
        else:
            if pos_1px >= pos_2px and pos_1py < pos_2py:
                window.blit(img_idle1p_1, (pos_1px - charawid / 2,pos_1py - charahei / 2))
            if pos_1px < pos_2px and pos_1py <= pos_2py:
                window.blit(img_idle1p_2, (pos_1px - charawid / 2,pos_1py - charahei / 2))
            if pos_1px <= pos_2px and pos_1py > pos_2py:
                window.blit(img_idle1p_3, (pos_1px - charawid / 2,pos_1py - charahei / 2))
            if pos_1px > pos_2px and pos_1py >= pos_2py:
                window.blit(img_idle1p_4, (pos_1px - charawid / 2,pos_1py - charahei / 2))

    if not guarding2p and not attacking2p:
        if moving2p:
            if FrameCount % 20 < 10:
                if pos_1px >= pos_2px and pos_1py < pos_2py:
                    window.blit(img_idle2p_3, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px < pos_2px and pos_1py <= pos_2py:
                    window.blit(img_idle2p_4, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px <= pos_2px and pos_1py > pos_2py:
                    window.blit(img_idle2p_1, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px > pos_2px and pos_1py >= pos_2py:
                    window.blit(img_idle2p_2, (pos_2px - charawid / 2,pos_2py - charahei / 2))  
            else:
                if pos_1px >= pos_2px and pos_1py < pos_2py:
                    window.blit(img_move2p_3, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px < pos_2px and pos_1py <= pos_2py:
                    window.blit(img_move2p_4, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px <= pos_2px and pos_1py > pos_2py:
                    window.blit(img_move2p_1, (pos_2px - charawid / 2,pos_2py - charahei / 2))
                if pos_1px > pos_2px and pos_1py >= pos_2py:
                    window.blit(img_move2p_2, (pos_2px - charawid / 2,pos_2py - charahei / 2))
        else:
            if pos_1px >= pos_2px and pos_1py < pos_2py:
                window.blit(img_idle2p_3, (pos_2px - charawid / 2,pos_2py - charahei / 2))
            if pos_1px < pos_2px and pos_1py <= pos_2py:
                window.blit(img_idle2p_4, (pos_2px - charawid / 2,pos_2py - charahei / 2))
            if pos_1px <= pos_2px and pos_1py > pos_2py:
                window.blit(img_idle2p_1, (pos_2px - charawid / 2,pos_2py - charahei / 2))
            if pos_1px > pos_2px and pos_1py >= pos_2py:
                window.blit(img_idle2p_2, (pos_2px - charawid / 2,pos_2py - charahei / 2))
    
    if life1p >= 3:
        window.blit(img_heart1, (width / 12 , height / 12))
        window.blit(img_heart1, (2 * width / 12 -10, height / 12))
        window.blit(img_heart1, (3 * width / 12 -20, height / 12))
    if life1p == 2:
        window.blit(img_heart1, (width / 12 , height / 12))
        window.blit(img_heart1, (2 * width / 12 -10, height / 12))
        window.blit(img_heart2, (3 * width / 12 -20, height / 12))
    if life1p == 1:
        window.blit(img_heart1, (width / 12 , height / 12))
        window.blit(img_heart2, (2 * width / 12 -10, height / 12))
        window.blit(img_heart2, (3 * width / 12 -20, height / 12))
    if life1p <= 0:
        window.blit(img_heart2, (width / 12 , height / 12))
        window.blit(img_heart2, (2 * width / 12 -10, height / 12))
        window.blit(img_heart2, (3 * width / 12 -20, height / 12))

    if life2p >= 3:
        window.blit(img_heart1, (8 * width / 12 , height / 12))
        window.blit(img_heart1, (9 * width / 12 - 10, height / 12))
        window.blit(img_heart1, (10 * width / 12 - 20, height / 12))
    if life2p == 2:
        window.blit(img_heart1, (8 * width / 12 , height / 12))
        window.blit(img_heart1, (9 * width / 12 - 10, height / 12))
        window.blit(img_heart2, (10 * width / 12 - 20, height / 12))
    if life2p == 1:
        window.blit(img_heart1, (8 * width / 12 , height / 12))
        window.blit(img_heart2, (9 * width / 12 - 10, height / 12))
        window.blit(img_heart2, (10 * width / 12 - 20, height / 12))
    if life2p <= 0:
        window.blit(img_heart2, (8 * width / 12 , height / 12))
        window.blit(img_heart2, (9 * width / 12 - 10, height / 12))
        window.blit(img_heart2, (10 * width / 12 - 20, height / 12))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()