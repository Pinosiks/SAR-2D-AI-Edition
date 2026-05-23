import pygame as py
clock = py.time.Clock()
import time
import tkinter as tk

py.init()# / хз что это ваще
screen = py.display.set_mode((1024, 720))# / экран размера
py.display.set_caption('SAR 2D game')# / название
icon = py.image.load('C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/Sar_icon.png').convert_alpha()# / загружаю эконку
py.display.set_icon(icon)# / устанавливаю эконку







mr_gameplay8=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/оу оу оуоуоуоуоуоуоуо.png")














picksel__txt = py.font.Font("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Textes/better-vcr5.1.ttf")
picksel_1txt = picksel__txt.render('Тебе пердется бежать через...',False,'White')


def new_blit(wtf,xx,yy):
    txte1=picksel__txt.render(wtf,False,'White')
    screen.blit(txte1,(xx,yy))













def new_red_blit(wtf,xx,yy):
    txte=picksel__txt.render(wtf,False,'Red')
    screen.blit(txte,(xx,yy))



if True:
    another_lift=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт1.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт2.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт3.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт4.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт5.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт6.png").convert_alpha(),
    py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/лифт7.png").convert_alpha()
    ]
    
    domes=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/x.png")
    
    schoola=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/school.png")
    somDom=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/somedome.png")
    
    tipo_da_vot_school=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/roofSchool2Right.png")
    dom_Tipo=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/roofDom2Left.png")
    
    zladeus=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/photo_2023-12-10_23-15-04.jpg").convert_alpha()
    
    yelka=[
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка2.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка3.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка4.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка5.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/елка6.png").convert_alpha()
        
    ]
    
    
    
    ekarniybabay=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/кароче вот ебааааат.png")
    
    klaun=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/ооченьстрашныйкляун!!!1.png").convert_alpha()
    sup_door=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/doorAnimation1.png").convert_alpha(),
              py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/doorAnimation2.png").convert_alpha(),
              py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/doorAnimation3.png").convert_alpha(),
              py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/doorAnimation4.png").convert_alpha(),
              py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/doorAnimation5.png").convert_alpha()
              ]
    
    chair=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/cheir.png").convert_alpha()
    wall_n=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-0002.png").convert_alpha()
    wall=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-000па1.png").convert_alpha()
    screen_gameplay_7=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/klaunroom.png").convert_alpha()
    menu_start=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/START_menu.png").convert_alpha()
    menu_wat_button=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/Menu_button.png").convert_alpha()
    menu_settings=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/menu_settings.png")
    
    
    kkiy_ico=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/kiy_ico.png").convert_alpha()
    spez_laser_effect=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/laserpng_spec.png").convert_alpha()
    zamock=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/замок.png").convert_alpha()
    
    pich_gme1=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/pichnom2.png").convert_alpha()
    pichmissBIG=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/photo_2023-11-21_10-54-49.jpg").convert_alpha()
    pichTVfase=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/pichFase.png").convert_alpha()
    pichGUY=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/pichGay.png").convert_alpha()
    pichlitlbiss=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/pichMissGuy.png").convert_alpha()
    
    
    new_E_button=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading1.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading2.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading3.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading4.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading5.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading6.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading7.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading8.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/e_button_loading9.png").convert_alpha()
           ]
    
    # звуки
    button_on_menu=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/zvuk11.mp3")
    open_dor_sound=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/door_open.mp3")
    vistuplenie_1=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/вступление1.mp3")
    vistuplenie_2=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/вступление 2.mp3")
    lift_button=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/elevator-button.mp3")
    lift_door=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/elevator-door-open-1.mp3")
    liter_sound=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/ligtf.ogg")
    lift_musick=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/lift_musick.mp3")
    Rn1=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/RUN1.mp3")
    sared_Sound=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/scared.mp3")
    
    
    # загрузка
    loading=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading1.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading2.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading3.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading4.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading5.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading6.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading7.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading8.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading9.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading10.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading11.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading12.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading13.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading14.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading15.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading16.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading17.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading18.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/loading19.png").convert_alpha()
    ]
    
    
    monster1=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_1.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_1.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_2.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_2.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_2.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_3.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_3.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/monst1_3.png").convert_alpha(),]
    

    screen_game_6=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/laserroom.png").convert_alpha()
    kkeypng=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/key.png").convert_alpha()
    laser=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/laser.png").convert_alpha()
    
    
    
    blaking=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/black_1.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/black_2.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/black_3.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/black_2.png").convert_alpha(),
             py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/black_1.png").convert_alpha()]
    
    a=1
    aa=0
    
    like = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/like.png")
    
    liftOpen=[py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
          py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),  
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(),
        
        
        
        
        ]
    lift=[
        
        

        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim2.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
         py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/liftanim1.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/lift.png").convert_alpha(),
          ]
    
    background_2= py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/беттон.png")
    sound_fire= py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/fire_Sound.mp3")

    back_screen_lobby = py.Surface((1024,720))
    back_screen_lobby = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/gress.png").convert_alpha()# / задний экран

    short_ht=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/short123.png")
    ghi=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/door.png").convert_alpha()
    ht = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/123.png").convert_alpha()
    board = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/board.png").convert_alpha()
    button_E = [py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-1.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-1.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-2.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-2.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-3.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-3.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-4.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-4.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-3.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-3.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-2.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-2.png").convert_alpha(),
                py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/E-1.png").convert_alpha()
                ]
    fire = [py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire001ng3.png").convert_alpha(),
            
            
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire001ng3.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire002ng3.png").convert_alpha(),
            
            
            
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire002ng3.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire002ng3.png").convert_alpha(),
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire0012.png").convert_alpha(),
            
            
            
            py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/fire0012.png").convert_alpha(),
            
            ]
    log = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/log.png").convert_alpha()
    # / Игровые правила
    no_player = False
    on_log=False
    E_push1 = False
    E_push2 = False
    nosing=False
    screen_black = True
    SETTings=None
    gwtf=False
    monsterf1=False
    nosing1=False
    nosing2=False
    button1=False
    button2=False
    musick1g=True
    uded=False
    scrd=False
    laser_sound=False
    laser_on=False
    batonmenus=True
    yobich=False
    # игровые режимы
    event_tipe=False
    Run_game = True
    gameplay_4_Shop=None
    gameplay_4_game=None
    game5=False
    gameplay_1 = False
    gameplay_6=False
    gameplay_6N=False
    gameplay_3lift=None
    gameplay_2 = None
    gameplay_7=None
    player_sitting=False
    gameplay_8 = False
    gameplay_9=False
    
    
    menu=True
    menuS=True
    menuB=None
    menuSET=None
    # инвентарь:
    screen_blit_like = False
    kkiy_ico_icoF2=False
    kkiy_ico_icoF3=False
    
    
    wrsf= py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/blackskreen_wis_lite.png").convert_alpha()
    
    # / игрок
    walk_left = [
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево стоит.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево стоит.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево стоит.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево стоит.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево идет.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/сабака 1 лево идет.png").convert_alpha()        ]
    walk_right = [
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака стоит право.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака стоит право.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака 1 право идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака 1 право идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака стоит право.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака стоит право.png").convert_alpha(), 
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака 1 право идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака 1 право идет.png").convert_alpha()]
    walk_up = [
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебяСТОИТ.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебяСТОИТ.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебяСТОИТ.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебя.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебя.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебя2.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебя2.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака идет от тебя2.png").convert_alpha()]
    walk_down = [
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, стоит.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, стоит.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, стоит.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, идет.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, идет2.png").convert_alpha(),
        py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/собака тебе в глаза смотрит, идет2.png").convert_alpha()]

    player_sit=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/игрок/sitting.png").convert_alpha()

    player_x = 400
    player_y = 470
    player_speed=8

    player_watch = 'up'
    # / монстор

    # / коунты
    count=0
    count_f=0
    count_button_E=0
    count_lift=0
    count_liftc=0
    count_b=0
    i = 0
    monster1_count=0
    generalcount5=1
    loading_count=0
    loading_sooper_count=0
    sup_door_count=0
    oyoy_count=0
    
    
    
    df=0
    ghtjeldgd=0
    
    monster_count_2_x=110
    monster_count_2_y=110
    
    monster_zladeus_count_x=512
    monster_zladeus_count_y=400  
    
    x=0
    y=0
    
    mouse_x =0
    mouse_y=0
    
    
    
    woleume=0.1
    
    some_another_lift_count=0
    n= player_speed
    
    icolite=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/icon_liter_box.png").convert_alpha()


class monster:
    speed = None
    pikcher = None
    mx = None
    my = None
    pikcher_m_count=None
    scrimer_sound=None
    
    # def went(self,mx=400,my=470,picher):
        
    # def __init__(self, speed, pikcher, mx, my, pikcher_m_count, scrimer_sound):
    #     if mx+x<player_x:
    #         screen.blit(pikcher[pikcher_m_count],(mx+x,my+y))
    #         mx+=speed
    #         monster1_count+=1
    #     if monster1_count==7:
    #         monster1_count=0
    #     if mx+x>=player_x:
    #         screen.blit(monster1[monster1_count],(mx+x,my+y))
    #         mx-=speed
    #         monster1_count+=1
    #     if monster1_count==7:
    #         monster1_count=0
    #     if my+y<=player_y:
    #         my+=speed
    #     if my+y>=player_y:
    #         my-=speed
    #     monster_hitbox1=monster1[0].get_rect(topleft=(mx+x,my+y))
    #     self.picher = picher
         
    
# Shirniy = monster(16,py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/monsters/photo_2023-11-01_20-42-03.jpg"))

# wayl//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

while Run_game:
    
    kiy=py.key.get_pressed()
    mouse_x, mouse_y = py.mouse.get_pos()
    
    # if screen_blit_like ==True:
    #     screen.blit()
    
    # ЗВУКИ ЗВУКОВ
    if True:
        button_on_menu.set_volume(woleume+0.01)
        open_dor_sound.set_volume(woleume+0.01)
        vistuplenie_1.set_volume(woleume+0.01)
        vistuplenie_2.set_volume(woleume+0.01)
        lift_button.set_volume(woleume+0.2)
        lift_door.set_volume(woleume+0.01)
        liter_sound.set_volume(woleume+4)
        lift_musick.set_volume(woleume+0.01)
        Rn1.set_volume(woleume+0.1)
        sared_Sound.set_volume(woleume+0.1)
        sound_fire.set_volume(woleume+0.3)

    
    
    if gameplay_1:
        
        
        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
        dor_hitbox = ghi.get_rect(topleft=(900,player_y))
        if nosing1==False:
            vistuplenie_1.play()
            nosing1=True
            
        screen.blit(back_screen_lobby,(0,0 )) # / Устанавливаю задний фон
        new_blit('ДОБРО ПОЖАЛОВАТЬ!',500,300)
        screen.blit(pich_gme1,(300,300))
        
        ht_hitbox = ht.get_rect(topleft=(570,470))
        
        log_hitbox = log.get_rect(topleft=(50,510))
        board_hitbox = board.get_rect(topleft=(450,430))
        
        
        # / встать с бревна
        if on_log==True and kiy[py.K_e]:
            player_x = 250
            player_y= 500
            no_player = False
            on_log=False
        
        
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        
        # EXIT
        if player_hitbox.colliderect(dor_hitbox):
            screen.blit(button_E[count_button_E],(960,400))
            count_button_E+=1
            if count_button_E==12:
                count_button_E =0
            if kiy[py.K_e]:
                gameplay_1=False
                gameplay_2=True
                
            
            
            
        
        # /управление персом
        if no_player == False:
            if kiy[py.K_w]and player_y >0:
                
                screen.blit(walk_up[count],(player_x,player_y))
                player_y-=player_speed
                player_watch='up'
                count+=1
            elif kiy[py.K_d]and player_x <1000:
                screen.blit(walk_right[count],(player_x,player_y))
                count+=1
                player_x+=player_speed
                player_watch='right'
            elif kiy[py.K_s]and player_y <700:
                screen.blit(walk_down[count],(player_x,player_y))
                count+=1
                player_y+=player_speed
                player_watch='down'
            elif kiy[py.K_a]and player_x >10:
                screen.blit(walk_left[count],(player_x,player_y))
                count+=1
                player_x-=player_speed
                player_watch='left'
        
        
        
        if on_log == False:
            sound_fire.stop()
        # / спаун постоянных спрайтов
        if True:
            screen.blit(fire[count_f],(50,510))
            count_f+=1
            screen.blit(log,(50,510))
            screen.blit(board, (450,430))
            
            screen.blit(ht,(570,470))
            screen.blit(ghi, (900,400))
        # / сажусь на бревно
        if player_hitbox.colliderect(log_hitbox):
            screen.blit(player_sit,(185,570))
            
            on_log=True
            screen.blit(button_E[count_button_E],(player_x,player_y))
            count_button_E+=1
            no_player = True
            
            if musick1g:
                sound_fire.play()
                musick1g=False
            
        # доска
        if player_hitbox.colliderect(board_hitbox):
            screen.blit(button_E[count_button_E],(550,400))
            count_button_E+=1
            if kiy[py.K_e]:
                E_push1 = True
                no_player= True
        # в доске
        if E_push1==True:
            dd=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/BOARDin.png").convert_alpha()
            screen.blit(dd,(30,50))
            if kiy[py.K_q]:
                player_x = 400
                player_y = 470
                no_player = False
                E_push1=False
        
        
        # столбики если нажал на е
        if E_push2==True:
            screen.blit(short_ht,(0,0))
            player_x = 500
            player_y = 520
            if kiy[py.K_q]:
                
                no_player = False
                E_push2=False
        # если дотронулся до столбов славы
        if player_hitbox.colliderect(ht_hitbox):
            screen.blit(button_E[count_button_E],(700,500))
            count_button_E+=1
            if kiy[py.K_e]:
                
                E_push2 = True
                no_player= True
        
        
        clock.tick(17)
    
    if gameplay_2:
        vistuplenie_1.stop()
        # геймплей 2:
        if nosing2==False:
            open_dor_sound.play()
            vistuplenie_2.play()
            nosing2=True

        picch_miss_hitbox=pichlitlbiss.get_rect(topleft=(x+400,y+40))
        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
        # / Устанавливаю задний фон
        screen.blit(background_2,(x-100,y-100 ))
        player_x=400
        player_y=400
        
        like_hitbox = like.get_rect(topleft=(x+50,y+100))
        lift_hitbox = lift[0].get_rect(topleft=(x+10,y+400))
        # если фанарик:
        if kiy[py.K_1]:
            screen_black=False
            liter_sound.play()
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        # /управление персом
        if no_player == False:
            if kiy[py.K_w]and y <410:
                screen.blit(walk_up[count],(player_x,player_y))
                y+=player_speed
                player_watch='up'
                count+=1
                
            elif kiy[py.K_d]and x >=-550:
                screen.blit(walk_right[count],(player_x,player_y))
                count+=1
                x-=player_speed
                player_watch='right'
                
            elif kiy[py.K_s]and y >-250:
                screen.blit(walk_down[count],(player_x,player_y))
                count+=1
                y-=player_speed
                player_watch='down'
                
            elif kiy[py.K_a]and x <370:
                screen.blit(walk_left[count],(player_x,player_y))
                count+=1
                x+=player_speed
                player_watch='left'
        # /Спаун простых объектов
        if True:
            screen.blit(pichlitlbiss,(x+400,y+40))
            if nosing==False:
                screen.blit(liftOpen[0],(x+10,y+400))
            if nosing:
                screen.blit(lift[0],(x+10,y+400))
            screen.blit(icolite,(450,680))
            if not screen_blit_like:
                screen.blit(like,(x+50,y+100))
        if kiy[py.K_2]and screen_blit_like:
            screen.blit(like,(player_x+5,player_y-30))
        # Если дотронусь до лифта:
        if player_hitbox.colliderect(lift_hitbox) and nosing==False:
            
            screen.blit(liftOpen[count_lift],(x+10,y+400))
            count_lift+=1
            lift_door.play(0,200)
            
            if count_lift==9:
                nosing=True
        elif player_hitbox.colliderect(lift_hitbox):
            screen.blit(button_E[count_button_E],(x-30,y+400))
            count_button_E+=1
            if kiy[py.K_e]:
                gameplay_2=False
                gameplay_3lift=True
                
        
        elif not player_hitbox.colliderect(lift_hitbox):
            if nosing:
                screen.blit(lift[count_liftc],(x+10,y+400))

                count_liftc+=1       
                if count_liftc==9:
                    nosing=False
        
        # если дотронулся до мисс
        if player_hitbox.colliderect(picch_miss_hitbox):
            screen.blit(button_E[count_button_E],(x+420,y+60))
            count_button_E+=1
            if kiy[py.K_e]:
                screen.blit(pichmissBIG,(0,0))
                
        
        if player_hitbox.colliderect(like_hitbox)and screen_blit_like == False:
            screen.blit(button_E[count_button_E],(x+30,y+200))
            count_button_E+=1
            if kiy[py.K_e]:
                screen_blit_like = True
                        
                   
        if screen_blit_like:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/like_iconiid.png").convert_alpha(),(500,680)) 
            
            
        if not screen_black:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/blackskreen_wis_lite.png").convert_alpha(),(mouse_x-1000,mouse_y-1000))
        if screen_black:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/blackskreen.png").convert_alpha(),(0,0))          
        
        

        
        clock.tick(24)
        
    if gameplay_3lift: 
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/iftScreen.png").convert(),(0,0))
        button2=False
        button1=False
        lift_musick.play()
        
        if 656>=mouse_x >=577 and 259<=mouse_y<=289:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/game_butan_lift.png").convert_alpha(),(577,259))
            if py.mouse.get_pressed()[0]:
                gameplay_3lift=False
                gameplay_4_game=True
                gameplay_4_Shop=False
                lift_musick.stop()
        
        
        if 656>=mouse_x >=577 and 300<=mouse_y<=330:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/shop_button_lift.png").convert_alpha(),(577,300))
            if py.mouse.get_pressed()[0]:
                gameplay_3lift=False
                gameplay_4_Shop=True
                gameplay_4_game=False
                lift_musick.stop()
        
    if gameplay_4_Shop:
        if button1==False:
            lift_button.play()
            button1=True
        
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/shopeg.png").convert_alpha(),(0,0))  
        if 69<mouse_x<97 and 411<mouse_y<446:    
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/ИФСЛ.png").convert_alpha(),(69,411))
            if py.mouse.get_pressed()[0]:
                gameplay_4_Shop=False
                gameplay_3lift=True
        
    if gameplay_4_game:
        screen.blit(blaking[count_b],(0,0))
        count_b+=1
        if button2==False:
            lift_button.play()
            button2=True
        
        elif count_b==4:
            gameplay_4_game=False
            game5=True
            screen.blit(picksel_1txt,(512,360))
            time.sleep(4)
            count_b=0
            generalcount5=1
            uded=False
            monsterf1=False
            monster1_x = 400
            monster1_y=470
            player_x=512
            player_y=360
            musick5g=True
            x=0
            y=0
            new_CEB=0
            count_new_E_button=0
            screen_black=True

        
        
            
        time.sleep(0.3)
         
    if game5:
        player_speed=20
        if musick5g:
            Rn1.play()
            musick5g=False
        # геймплей 5:
        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
        # / Устанавливаю задний фон
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/screen5.png"),(x-2047,y))
        
        # player_y+=50
        
        if True:

            kerpich_Rurru2 = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-0004.png").get_rect(topleft=(x-1330,y+393))
            kerpich_rR2 = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-0004.png").get_rect(topleft=(x-1357,y+393))
            
            kerpich_Rurru = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-0004.png").get_rect(topleft=(x-1330,y-20))
            kerpich_rR = py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/hitboxes/Sprite-0004.png").get_rect(topleft=(x-1357,y-20))
            # screen.blit(kerpich_rR,(x-1357,y))
        
        
            
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))


        monster_hitbox1=monster1[0].get_rect(topleft=(monster1_x+x,monster1_y+y))
        
        
        if not no_player:
            if kiy[py.K_w] and y <360 and not player_hitbox.colliderect(kerpich_rR) and not player_hitbox.colliderect(kerpich_Rurru):
                # if i == player_speed:
                #     i = 0
                # while i != player_speed:
                    
                #     if player_hitbox.top <= kerpich_rR.bottom and player_hitbox.bottom >= kerpich_rR.top:
                #         # y -= player_speed
                #         break
                #     else:
                    y += player_speed
                    player_watch = 'up'   
                    count += 1    
                    screen.blit(walk_up[count],(player_x, player_y))
                        # i += 1
                        # if count == 7:
                        #     count = 0
            elif kiy[py.K_d] and x > -260 and not player_hitbox.colliderect(kerpich_rR) and not player_hitbox.colliderect(kerpich_rR2):
                # if i == player_speed:
                    #     i = 0
                    # while i != player_speed:
                    #     if player_hitbox.left <= kerpich_rR.right and player_hitbox.right >= kerpich_rR.left:
                    #         break
                    #     else:
                    x -= player_speed
                    player_watch = 'right'   
                    count += 1    
                    screen.blit(walk_right[count],(player_x, player_y))
                            # i += 1
                            # if count == 7:
                            #     count = 0


            elif kiy[py.K_s] and y > -305 and not player_hitbox.colliderect(kerpich_rR2) and not player_hitbox.colliderect(kerpich_Rurru2):
                    # if i == player_speed:
                    #     i = 0
                    # while i != player_speed:
                    #     if player_hitbox.bottom <= kerpich_rR.top and player_hitbox.top >= kerpich_rR.bottom:
                    #         break
                    #     else:
                    y -= player_speed
                    player_watch = 'down'   
                    count += 1    
                    screen.blit(walk_down[count],(player_x, player_y))
                            # i += 1
                            # if count == 7:
                            #     count = 0


            elif kiy[py.K_a] and x < 2570 and not player_hitbox.colliderect(kerpich_Rurru) and not player_hitbox.colliderect(kerpich_Rurru2):
                    # if i == player_speed:
                    #     i = 0
                    # while i != player_speed:
                    #     if player_hitbox.left<=kerpich_rR.right and player_hitbox.right>=kerpich_rR:  
                    #         break
                    #     else:
                    x += player_speed
                    player_watch = 'left'   
                    count += 1    
                    screen.blit(walk_left[count],(player_x, player_y))
                            # i += 1
                            # if count == 7:
                            #     count = 0


        if monsterf1:
            if monster1_x+x<player_x:
                screen.blit(monster1[monster1_count],(monster1_x+x,monster1_y+y))
                monster1_x+=player_speed+1
                monster1_count+=1
                if monster1_count==7:
                    monster1_count=0
            if monster1_x+x>=player_x:
                screen.blit(monster1[monster1_count],(monster1_x+x,monster1_y+y))
                monster1_x-=player_speed+1
                monster1_count+=1
                if monster1_count==7:
                    monster1_count=0
            if monster1_y+y<=player_y:
                monster1_y+=player_speed+1
            if monster1_y+y>=player_y:
                monster1_y-=player_speed+1
        new_dor_hitbox=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/new desck.png").get_rect(topleft=(x-2004,y+440))#-230
        if ghtjeldgd == 61:
            ghtjeldgd=0
        if new_CEB==8:
            monsterf1=False
            screen.blit(blaking[2],(0,0))
            
            ghtjeldgd+=1
            if ghtjeldgd==60:
                game5=False
                gameplay_6N=True
                sdgfdbgfnxc=True
        # E button!
        if player_hitbox.colliderect(new_dor_hitbox) and not new_CEB==8:
            screen.blit(new_E_button[new_CEB],(x-1904,y+370))
            if kiy[py.K_e]:
                count_new_E_button+=1
                if count_new_E_button==12 or count_new_E_button==24 or count_new_E_button==36 or count_new_E_button==48 or count_new_E_button==64 or count_new_E_button==76 or count_new_E_button==88 or  count_new_E_button==100:
                    new_CEB+=1
        
        if generalcount5>=1:
            generalcount5+=1
        if generalcount5==160:
            monsterf1=True
        
        screen.blit(icolite,(450,680))    
        if kiy[py.K_1]:
            screen_black=False
            liter_sound.play()
        if kiy[py.K_2]and screen_blit_like:
            screen.blit(like,(player_x+5,player_y-30))   
        if screen_blit_like:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/like_iconiid.png").convert_alpha(),(500,680)) 
        if not screen_black:
           screen.blit(wrsf,(mouse_x-1000,mouse_y-1000))
        if screen_black:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/blackskreen.png").convert_alpha(),(0,0))          
        
        
        
            
        if monster_hitbox1.colliderect(player_hitbox):
            game5=False
            uded=True 
            scrd=True 
        clock.tick(24)
    
    if gameplay_6N and sdgfdbgfnxc:
        Rn1.stop()
        screen.blit(blaking[3],(0,0))  
        new_blit('Ты прошел!',500,500)
        new_blit('Но что дальше?',500,520)
        time.sleep(0.05)
        screen.blit(loading[loading_count],(50,50))
        loading_count +=1  
        if loading_sooper_count==10:
            loading_sooper_count=0
            scrd=False
            gameplay_6N=False
            gameplay_6=True
            x=0
            y=0
            player_x = 400
            player_y = 470
    
    if gameplay_6:
        
        screen.blit(screen_game_6,(x+0,y+0))
        # ключ лазер и тп
        screen.blit(pichGUY,(x+375,y+188))
        screen.blit(pichTVfase,(x+515,y+188))
        if laser_on==False:
            screen.blit(laser,(x+272,y+437))
        screen.blit(zamock,(x+271,407+y))
        if kkiy_ico_icoF2==False and kkiy_ico_icoF3==False:
            screen.blit(kkeypng,(300+x,y+245))
        player_speed=7
        # хитбоксы
        player_hitbox=walk_left[0].get_rect(topleft=(player_x,player_y))
        lazer_hitbox=laser.get_rect(topleft=(x+272,y+437))
        kkeypng_hitbox=kkeypng.get_rect(topleft=(x+300,y+245))
        zamock_hitbox=zamock.get_rect(topleft=(x+271,407+y))
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        # походка персанажа
        if not no_player:
            if kiy[py.K_w] and y <272:
             
                    y += player_speed
                    player_watch = 'up'   
                    count += 1    
                    screen.blit(walk_up[count],(player_x, player_y))
                    
            elif kiy[py.K_d] and x > -280:
                
                    x -= player_speed
                    player_watch = 'right'   
                    count += 1    
                    screen.blit(walk_right[count],(player_x, player_y))

            elif kiy[py.K_s] and y > 3:

                    y -= player_speed
                    player_watch = 'down'   
                    count += 1    
                    screen.blit(walk_down[count],(player_x, player_y))

            elif kiy[py.K_a] and x <121:
                    x += player_speed
                    player_watch = 'left'   
                    count += 1    
                    screen.blit(walk_left[count],(player_x, player_y))
        # подобрать ключ
        if player_hitbox.colliderect(kkeypng_hitbox) and kkiy_ico_icoF2==False and kkiy_ico_icoF3==False:
            screen.blit(button_E[count_button_E],(x+350,y+300))
            count_button_E+=1
            if kiy[py.K_e]:
                if screen_blit_like:
                    kkiy_ico_icoF3=True 
                if screen_blit_like==False:
                    kkiy_ico_icoF2=True    
        # ключевая иконка
        if kkiy_ico_icoF2==True and laser_on==False:
            screen.blit(kkiy_ico,(500,680))
        if kkiy_ico_icoF3==True and laser_on==False:
            screen.blit(kkiy_ico,(542,680))
        # иконка фанарика И НЕ ТОЛЬКО!
        
        
        screen.blit(icolite,(450,680))
        
        # если лазер испипелить!!
        if player_hitbox.colliderect(lazer_hitbox) and laser_on==False:
            screen.blit(spez_laser_effect,(x+290,y+460))
            df+=1
            if df ==6:
                screen.blit(spez_laser_effect,(x+292,y+465))
            if df ==12:
                screen.blit(spez_laser_effect,(x+297,y+479))
            if df ==18:
                screen.blit(spez_laser_effect,(x+288,y+471))
            if df ==24:
                screen.blit(spez_laser_effect,(x+280,y+451))
            if df ==30:
                screen.blit(spez_laser_effect,(x+275,y+445))
            if df == 50:
                uded=True
                laser_sound=True
                gameplay_6=False
            if df == 51:
                df=0
        # иконка таблички
        if screen_blit_like:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/like_iconiid.png").convert_alpha(),(500,680))
        
        # если табличка нажата 
        if kiy[py.K_2]and screen_blit_like:
            screen.blit(like,(player_x+5,player_y-30))   
        # если фанарик:
        if kiy[py.K_1]:
            screen_black=False
            liter_sound.play()    
        if not screen_black:
           screen.blit(wrsf,(mouse_x-1000,mouse_y-1000))
        if screen_black:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/blackskreen.png").convert_alpha(),(0,0))          
        if player_hitbox.colliderect(zamock_hitbox) and (kkiy_ico_icoF2==True or kkiy_ico_icoF3==True)and laser_on==False: 
            screen.blit(button_E[count_button_E],(x+350,y+300))
            count_button_E+=1         
            if kiy[py.K_e]:
                laser_on = True
       
        if player_hitbox.colliderect(lazer_hitbox) and laser_on:
            gameplay_6=False
            gameplay_7=True
            x=0
            y=0
            monster1_x = 400
            monster1_y=470
            player_x = 400
            player_y = 470
            laser_sound=False
            scrd=True
    
        clock.tick(24)
    
    if gameplay_7:
        klaun_hitbox=klaun.get_rect(topleft=(monster_count_2_x+x,monster_count_2_y+y))
        gameplay_6N=False
        screen.blit(screen_gameplay_7,(x+0,y+0))
        # screen.blit(wall,(79,340))
        screen.blit(chair,(x+122,y+560))
        chair_hitbox=chair.get_rect(topleft=(x+122,y+560))
        
        wall_wall_hitbox_R= wall_n.get_rect(topleft=(x+688,y+318))
        wall_wall_hitbox= wall_n.get_rect(topleft=(x+557,y+318))
        
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/портал 1.png"),(666+x, 90+y))
        portal1_hitbox=py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/портал 1.png").get_rect(topleft=(666+x, 90+y))
        
        
        wall_hitbox_n = wall.get_rect(topleft=(x+688,335))
        wall_hitbox_up_n = wall.get_rect(topleft=(x+688,y+320))
        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
        wall_hitbox = wall.get_rect(topleft=(x+76,y+335))
        wall_hitbox_up = wall.get_rect(topleft=(x+76,y+320))
        sup_door_hitbox=sup_door[0].get_rect(topleft=(x+531,y+316))
        
        if player_hitbox.colliderect(sup_door_hitbox) and sup_door_count!=5:
            screen.blit(sup_door[sup_door_count],(x+531,y+316))
            sup_door_count+=1
        
        if sup_door_count==0:
            screen.blit(sup_door[0],(x+531,y+316))
        
        if player_hitbox.colliderect(portal1_hitbox):
            gameplay_7=False
            gameplay_8=True
            count=0
            x=0
            y=300
            player_speed=15
        if player_hitbox.colliderect(klaun_hitbox):
            uded=True
            scrd=True
            gameplay_7=False
        
        
        
        if sup_door_count==5:
            screen.blit(sup_door[4],(x+531,y+316))
        #  and y < 148 
        if count == 7:
            count = 0
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        # походка персанажа
        if not no_player:
            if kiy[py.K_w] and not (player_hitbox.colliderect(wall_hitbox)) and not (player_hitbox.colliderect(wall_hitbox_n)):
                    y += player_speed
                    player_watch = 'up'   
                    count += 1    
                    screen.blit(walk_up[count],(player_x, player_y))
                    
            elif kiy[py.K_d] and x > -369 and not (player_hitbox.colliderect(wall_wall_hitbox_R)):
                    x -= player_speed
                    player_watch = 'right'   
                    count += 1    
                    screen.blit(walk_right[count],(player_x, player_y))

            elif kiy[py.K_s] and y > -90 and not (player_hitbox.colliderect(wall_hitbox_up)) and not (player_hitbox.colliderect(wall_hitbox_up_n)):
                    y -= player_speed
                    player_watch = 'down'   
                    count += 1    
                    screen.blit(walk_down[count],(player_x, player_y))

            elif kiy[py.K_a] and x <323 and not (player_hitbox.colliderect(wall_wall_hitbox)):
                    x += player_speed
                    player_watch = 'left'   
                    count += 1    
                    screen.blit(walk_left[count],(player_x, player_y))
    
        if player_sitting==True:
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/sitttting.png"),(x+112,y+530))
            no_player=True
            
        if player_sitting==True and kiy[py.K_q]:
            no_player=False
            player_sitting=False
            
            
        if player_hitbox.colliderect(chair_hitbox) and player_sitting==False:
            screen.blit(button_E[count_button_E],(x+111,y+400))
            count_button_E+=1
            if kiy[py.K_e]:
                player_sitting=True
        
        # monster klaun
        if monster_count_2_x+x<player_x:
            screen.blit(klaun,(monster_count_2_x+x,monster_count_2_y+y))
            monster_count_2_x+=1
            if monster1_count==7:
                monster1_count=0
        if monster_count_2_x+x>=player_x:
            screen.blit(klaun,(monster_count_2_x+x,monster_count_2_y+y))
            monster_count_2_x-=1
            if monster1_count==7:
                monster1_count=0
        if monster_count_2_y+y<=player_y:
            monster_count_2_y+=1
        if monster_count_2_y+y>=player_y:
            monster_count_2_y-=1
            
        # if klaun_hitbox.colliderect(player_hitbox):
            
     
            
        #     ghtjeldgd+=1
        #     if ghtjeldgd==10:
        #         game5=False
        #         gameplay_6N=True
        #         sdgfdbgfnxc=True
        
        
        
        
        clock.tick(24)
    
    if gameplay_8:
        screen.blit(mr_gameplay8,(x+0,y-1000))

        
        if monster_zladeus_count_x+x<player_x:
            screen.blit(zladeus,(monster_zladeus_count_x+x,monster_zladeus_count_y+y))
            monster_zladeus_count_x+=9
            if monster1_count==7:
                monster1_count=0
        if monster_zladeus_count_x+x>player_x:
            screen.blit(zladeus,(monster_zladeus_count_x+x,monster_zladeus_count_y+y))
            monster_zladeus_count_x-=9
            if monster1_count==7:
                monster1_count=0
        if monster_zladeus_count_y+y<player_y:
            monster_zladeus_count_y+=9
        if monster_zladeus_count_y+y>player_y:
            monster_zladeus_count_y-=9
        
        zladeus_hitbox=zladeus.get_rect(topleft=(x+monster_zladeus_count_x,y+monster_zladeus_count_y))
        
        if zladeus_hitbox.colliderect(player_hitbox):
            scrd=True
            uded=True
        
        
        screen.blit(another_lift[some_another_lift_count],(x+129,y-871))
        
        another_lift_hitbox = another_lift[0].get_rect(topleft=(x+129,y-871))
        
        
         # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        
        # походка персанажа
        if not no_player:
            if kiy[py.K_w] and y <1300:
                    y += player_speed
                    player_watch = 'up'   
                    count += 1    
                    screen.blit(walk_up[count],(player_x, player_y))
                    
            elif kiy[py.K_d]and x >=-500:
                    x -= player_speed
                    player_watch = 'right'   
                    count += 1    
                    screen.blit(walk_right[count],(player_x, player_y))

            elif kiy[py.K_s]and y >0:
                    y -= player_speed
                    player_watch = 'down'   
                    count += 1    
                    screen.blit(walk_down[count],(player_x, player_y))

            elif kiy[py.K_a]and x <290:
                    x += player_speed
                    player_watch = 'left'   
                    count += 1    
                    screen.blit(walk_left[count],(player_x, player_y))
        

        
        if player_hitbox.colliderect(another_lift_hitbox):
            screen.blit(button_E[count_button_E],(x+229,y-871))
            count_button_E+=1
            if kiy[py.K_e]:
                yobich=True
        
        if yobich and some_another_lift_count!=7:
            some_another_lift_count+=1
            
        if some_another_lift_count==7:
            gameplay_8=False
            gameplay_9=True
            x=0
            y=0
            player_speed=6
        
        
        
        
        screen.blit(blaking[0],(0,0))
    
        clock.tick(24)
        
    if gameplay_9:
        
        screen.blit(ekarniybabay,(x-1100,y-3300))
       
        
        hitbox_with_1_SCHOLA_BOTTOM = domes.get_rect(topleft=(x+106+349,y-2154-220+923))
        hitbox_with_1_SCHOLA_TOP = domes.get_rect(topleft=(x+106+760,y-2154-220+60))
        hitbox_with_1_SOM_DOM = domes.get_rect(topleft=(x-850+469, y-1270+295))
        
        
        # if kiy[py.K_f]:
        #     print(mouse_x+x,mouse_y+y)
        
        
        screen.blit(somDom,(x-850, y-1270))
        screen.blit(schoola,(x+106,y-2154-100)) 
        
        screen.blit(domes,(x+106+349,y-2154-220+923))
        screen.blit(domes,(x+106+760,y-2154-220+60))
        screen.blit(domes,(x-850+469, y-1270+295))
        
        
        dom_hitbox = dom_Tipo.get_rect(topleft=(x-757,y-1270))
        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
        shchola_hitbox = tipo_da_vot_school.get_rect(topleft=(x+160,y-2049-220))
        
        # / куда повернут игрок
        if no_player == False:
            if player_watch=='right':
                screen.blit(walk_right[0],(player_x,player_y))
            if player_watch=='up':
                screen.blit(walk_up[0],(player_x,player_y))
            if player_watch=='down':
                screen.blit(walk_down[0],(player_x,player_y))
            if player_watch=='left':
                screen.blit(walk_left[0],(player_x,player_y))
        
        # походка персанажа
        if not no_player:
            if kiy[py.K_w] and y <3300:
                    
                    while n!=0 and (player_hitbox.top!=shchola_hitbox.bottom or (player_x<shchola_hitbox.left or player_x>shchola_hitbox.right)) and (player_hitbox.top!=dom_hitbox.bottom or (player_x<dom_hitbox.left or player_x>dom_hitbox.right)):
                        y +=1
                        n-=1
                        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
                        shchola_hitbox=tipo_da_vot_school.get_rect(topleft=(x+106,y-2049-220))
                        dom_hitbox = dom_Tipo.get_rect(topleft=(x-757,y-1270))
                        
                    n=player_speed
                    
                    player_watch = 'up'   
                    oyoy_count+=1
                    if oyoy_count==2:
                        count += 1    
                        oyoy_count=0
                    screen.blit(walk_up[count],(player_x, player_y))
                    
            elif kiy[py.K_d]and x >=-2000:
                
                    while n!=0 and (player_hitbox.right!=shchola_hitbox.left or (player_y<shchola_hitbox.top or player_y>shchola_hitbox.bottom))and (player_hitbox.right!=dom_hitbox.left or (player_y<dom_hitbox.top or player_y>dom_hitbox.bottom)):
                        x -=1
                        n-=1
                        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
                        shchola_hitbox=tipo_da_vot_school.get_rect(topleft=(x+106,y-2049-220))
                        dom_hitbox = dom_Tipo.get_rect(topleft=(x-757,y-1270)) 
                    n=player_speed
                    
                    player_watch = 'right'   
                    oyoy_count+=1
                    if oyoy_count==2:
                        count += 1    
                        oyoy_count=0
                    screen.blit(walk_right[count],(player_x, player_y))

            elif kiy[py.K_s]and y >-110:
                    while n!=0 and (player_hitbox.bottom!=shchola_hitbox.top or (player_x<shchola_hitbox.left or player_x>shchola_hitbox.right)) and (player_hitbox.bottom!=dom_hitbox.top or (player_x<dom_hitbox.left or player_x>dom_hitbox.right)):
                        y -=1
                        n-=1
                        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
                        shchola_hitbox=tipo_da_vot_school.get_rect(topleft=(x+106,y-2049-220))
                        dom_hitbox = dom_Tipo.get_rect(topleft=(x-757,y-1270)) 
                        
                    n=player_speed
                    
                    player_watch = 'up'   
                    oyoy_count+=1
                    if oyoy_count==2:
                        count += 1    
                        oyoy_count=0
                    screen.blit(walk_up[count],(player_x, player_y))
                    player_watch = 'down'   
                    oyoy_count+=1
                    if oyoy_count==2:
                        count += 1    
                        oyoy_count=0  
                    screen.blit(walk_down[count],(player_x, player_y))

            elif kiy[py.K_a]and x <1100:
                    while n!=0 and (player_hitbox.left!=shchola_hitbox.right or (player_y<shchola_hitbox.top or player_y>shchola_hitbox.bottom)) and (player_hitbox.left!=dom_hitbox.right or (player_y<dom_hitbox.top or player_y>dom_hitbox.bottom)):
                        x +=1
                        n-=1
                        player_hitbox = walk_left[0].get_rect(topleft=(player_x,player_y))
                        shchola_hitbox=tipo_da_vot_school.get_rect(topleft=(x+106,y-2049-220))
                        dom_hitbox = dom_Tipo.get_rect(topleft=(x-757,y-1270)) 
                        
                    n=player_speed
                    
                    player_watch = 'left' 
                    oyoy_count+=1  
                    if oyoy_count==2:
                        count += 1    
                        oyoy_count=0 
                    screen.blit(walk_left[count],(player_x, player_y))
                    
                   
        if player_hitbox.colliderect(hitbox_with_1_SCHOLA_TOP) or player_hitbox.colliderect(hitbox_with_1_SCHOLA_BOTTOM):
            print('rre')           
                    
                    
        screen.blit(yelka[0],(x-50, y-400))
        screen.blit(yelka[5],(x+0, y+0))
        screen.blit(yelka[0],(x+800, y+210))
        screen.blit(yelka[0],(x+1400, y-74))
        screen.blit(yelka[0],(x-800, y-210))
        screen.blit(yelka[0],(x-410, y-14))
        screen.blit(yelka[0],(x-530, y-1510))
        screen.blit(yelka[5],(x+509, y-1500))
        screen.blit(yelka[0],(x-500, y-2010))
        screen.blit(yelka[0],(x+1520, y-1710))
        screen.blit(yelka[0],(x+2090, y-1550))
        screen.blit(yelka[5],(x+1490, y-2510))
        screen.blit(yelka[0],(x+2030, y-2150))
        screen.blit(yelka[0],(x+1490, y-510))
        
        screen.blit(yelka[1],(x+200+0, y+0+70))
        screen.blit(yelka[1],(x+200+800, y+210+70))
        screen.blit(yelka[1],(x+200+1400, y-74+70))
        screen.blit(yelka[5],(x+200-800, y-210+70))
        screen.blit(yelka[1],(x+200-410, y-14+70))
        screen.blit(yelka[1],(x+200-530, y-1510+70))
        screen.blit(yelka[5],(x+200+509, y-1500+70))
        screen.blit(yelka[1],(x+200-500, y-2010+70))
        screen.blit(yelka[1],(x+200+1520, y-1710+70))
        screen.blit(yelka[5],(x+200+2090, y-1550+70))
        screen.blit(yelka[5],(x+200+1490, y-2510+70))
        screen.blit(yelka[1],(x+200+2030, y-2150+70))
        screen.blit(yelka[1],(x+200+1490, y-510+70))
        
        screen.blit(yelka[3],(x+500+0, y+0-50))
        screen.blit(yelka[3],(x+500+800, y+210-50))
        screen.blit(yelka[3],(x+500+1400, y-74-50))
        screen.blit(yelka[3],(x+500-800, y-210-50))
        screen.blit(yelka[5],(x+500-410, y-14-50))
        screen.blit(yelka[3],(x+500-530, y-1510-50))
        screen.blit(yelka[3],(x+500+509, y-1500-50))
        screen.blit(yelka[5],(x+500-500, y-2010-50))
        screen.blit(yelka[3],(x+500+1520, y-1710-50))
        screen.blit(yelka[5],(x+500+2090, y-1550-50))
        screen.blit(yelka[5],(x+500+1490, y-2510-50))
        screen.blit(yelka[3],(x+500+2030, y-2150-50))
        screen.blit(yelka[3],(x+500+1490, y-510-50))
        
        screen.blit(yelka[4],(x-720-50, y-400-40))
        screen.blit(yelka[4],(x-720+0, y+0-40))
        screen.blit(yelka[4],(x-720+800, y+210-40))
        screen.blit(yelka[5],(x-720+1400, y-74-40))
        screen.blit(yelka[4],(x-720-800, y-210-40))
        screen.blit(yelka[4],(x-720-410, y-14-40))
        screen.blit(yelka[5],(x-720-530, y-1510-40))
        screen.blit(yelka[4],(x+520+509, y-1500-40))
        screen.blit(yelka[5],(x+520-500, y-2010-40))
        screen.blit(yelka[5],(x+520+1520, y-1710-40))
        screen.blit(yelka[4],(x+520+2090, y-1550-40))
      
        
        
        
        
        
        
        
        
        
        
        
        clock.tick(48)
        
        
        
    
    # меню START TP AND TD
    if menu:


        if menuS:
            
            screen.blit(menu_start,(0,0))
            
            new_blit('Играть',135,300)
            new_blit('Настройки',135,360)
            new_blit('Раскладка',135,390)
            new_blit('Выйти',135,420)
            # играть
            if 130<mouse_x<190 and 300<mouse_y<310:
                new_red_blit('Играть',135,300)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                if py.mouse.get_pressed()[0]:
                    time.sleep(0.2)
                    gameplay_1=True
                    menu=False
            # Настройки
            if 130<mouse_x<218 and 360<mouse_y<371:
                new_red_blit('Настройки',135,360)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                if py.mouse.get_pressed()[0]:
                    menuS=False
                    menuSET=True
                    time.sleep(0.2)
            # Раскладка
            if 130<mouse_x<217 and 390<mouse_y<401:
                new_red_blit('Раскладка',135,390)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                if py.mouse.get_pressed()[0]:
                    menuS=False
                    menuB=True
                    time.sleep(0.2)
            # Выйти
            if 130<mouse_x<182 and 420<mouse_y<432:
                new_red_blit('Выйти',135,420)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                if py.mouse.get_pressed()[0]:
                    event_tipe = True
                    

            if not( 130<mouse_x<182 and 420<mouse_y<432) and not( 130<mouse_x<217 and  390<mouse_y<401) and not( 130<mouse_x<218 and  360<mouse_y<371) and not( 130<mouse_x<190 and  300<mouse_y<310):
                batonmenus=True
                   
        if menuSET:
            
            screen.blit(menu_settings,(0,0))
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/sound.png"),(535,360))
            screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/nsound.png"),(535,360))
            
            new_blit('cдесь начего пока нет((',135,360)
            new_blit('cдесь начего пока нет((',135,390)
            new_blit('Назад',135,420)
            # if 535<mouse_x<660 and 360<mouse_y<392 and py.mouse.get_pressed()[0]:
            if 130<mouse_x<182 and 420<mouse_y<432:
                new_red_blit('Назад',135,420)
                if py.mouse.get_pressed()[0]:
                    menuS=True
                    menuSET=False
                    time.sleep(0.2)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                    
            # играть в последнюю версию
            if 130<mouse_x<190 and 300<mouse_y<310:
                new_red_blit('Играть в (для разроботчиков)',135,300)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False
                if py.mouse.get_pressed()[0]:
                    
                    gameplay_7=True
                    menu=False    
               
            if not(130<mouse_x<182 and 420<mouse_y<432) and not( 130<mouse_x<217 and  390<mouse_y<401) and not( 130<mouse_x<218 and  360<mouse_y<371) and not( 130<mouse_x<190 and  300<mouse_y<310):
                batonmenus=True        
                                
        if menuB:
            screen.blit(menu_wat_button,(0,0))
            new_blit('W A S D - чтобы ходить',235,220)
            new_blit('E - чтобы взаимодействовать',235,250)
            new_blit('Q - чтобы отменить',235,280)
            new_blit('1 2 3 и т.д. - чтобы выбрать предмет',235,310)
            new_blit('Esc - чтобы выйти в меню',235,340)
            new_blit('Приятной игры!',235,370)
            new_blit('Назад',135,420)   
            if 130<mouse_x<182 and 420<mouse_y<432:
                new_red_blit('Назад',135,420)
                if py.mouse.get_pressed()[0]:
                    menuS=True
                    menuB=False
                    time.sleep(0.2)
                if batonmenus:
                    button_on_menu.play()
                    batonmenus=False 
            if not(130<mouse_x<182 and 420<mouse_y<432):
                batonmenus=True   
        
        clock.tick(24)

    
    # Если умер 
    if uded:
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/imgonline-com-ua-pixelizationZXzxieU4NUO1.png").convert_alpha(),(0,0))     
        sdgfdbgfnxc=False
        Rn1.stop()
        if scrd:
            sared_Sound.play()
            scrd=False
        if laser_sound:
            dfghggxfnm=py.mixer.Sound("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/Sounds/laser-descend_gjps9oe_ — копия.mp3")
            dfghggxfnm.play()
            laser_sound=False
            
        new_blit("Начать заново",350,650)
        new_blit('Выйти в меню',600,650)
        if 350<mouse_x<460 and 660>mouse_y>643:
            if batonmenus:
                button_on_menu.play()
                batonmenus=False
            new_red_blit("Начать заново",350,650)
            if py.mouse.get_pressed()[0]:
                game5=False
                gameplay_3lift=True
                uded=False
                scrd=True
        if not (350<mouse_x<460 and 660>mouse_y>643):
            batonmenus=True    
            
        if 600<mouse_x<710 and 660>mouse_y>643:
            new_red_blit("Выйти в меню",600,650)
            # if py.mouse.get_pressed()[0]:
    
    
    
            
    # если вышел в Esc
    if kiy[py.K_ESCAPE] or gwtf==True:
        screen.blit(py.image.load("C:/Users/Dniko/Desktop/Проекты По питону/pygame_code_zakaz/SARs_pngs/ecs.png").convert_alpha(),(0,0))
        gwtf=True
        if kiy[py.K_q]:
            gwtf=False
            
            
    
    
    
    # каунты
    if count_button_E==12:
        count_button_E =0
    if count == 7:
        count = 0
    if count_f == 7:
        count_f = 0
    if count_lift == 9:
        count_lift = 0
    if count_liftc == 10:
        count_liftc=0
    if loading_count==19:
        loading_count=0
        loading_sooper_count+=1
    
    
    
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:# / если жмут на крестик
            py.quit()# / выключать
            Run_game = False
        if event_tipe == True:# / если жмут на крестик
            py.quit()# / выключать
            Run_game = False

