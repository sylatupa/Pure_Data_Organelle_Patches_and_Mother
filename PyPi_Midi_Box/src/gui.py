global xsize, ysize

#code attribution goes to PrashantMohta https://github.com/PrashantMohta/mlcd/blob/master/mlcd_example.py
try:
    import pygame
except:
    print('no pygame')


xsize = 128*12
ysize = 64*12
try:
    print("OLED INIT")
    import machine
    import libs.ssd1306 as ssd1306 
    import time
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    oled.fill(0) 
    oled.text('**DC Multi-Tool**', 0, 0)
    oled.text('****************', 0, 10)
    oled.text('', 0, 20)
    oled.text('', 0, 30)
    oled.show()
    time.sleep(1)
    print("OLED INIT")
except Exception as e:
    print(e)

prntDict = {"apps":"<|----APPS----|>","app":"<> ^-EXEC v-BACK"}
vowels = ('a', 'e', 'i', 'o', 'u')
def rmVwl(strng):
    return ''.join([l for l in strng if l not in vowels])

def prnt(menuo,pubsubs):
    #for key,val in menuo.events.items(): print("{} = {}".format(key, type(val)))
    fullPrint = []
    fullPrint.append(str(prntDict.get(menuo.state)) )

    fullPrint.append( str(menuo.indexApp)+"/"+str(menuo.maxAppIndex) +" "+ rmVwl(menuo.currentAppName) + " "+ str(menuo.app_st_menu[menuo.app_st_num]) )

    for app_pbr in pubsubs.app_pbrs: 
        fullPrint.append(app_pbr+":")
        for event in pubsubs.app_pbrs.get(app_pbr).events:
            for k,v in pubsubs.app_pbrs.get(app_pbr).events.items():
                callbacks = '    '
                for key in v.keys():
                    callbacks += str(key) + ', ' 
            #callbacks += str(key.__name__.split('.')[2]) + ', '        
            #fullPrint.append("-" + str((event)) + " " + (callbacks))
            fullPrint.append(str(prnt_data_dict.get(event)) + " ->" + str(rmVwl(event)) + " " + rmVwl(callbacks))
        #fullPrint +=pubs
        str_array = ""
        '''
        length = xsize /20
        for x in pubs:
            str_array +="--"
            for c in x:
                if len(str_array)<length:
                    str_array+=c
                else:
                    str_array+=c
                    fullPrint.append(str_array)
                    str_array=''
            str_array +=" --"
        fullPrint += str_array
        '''
        #draw([(menuo.state + " " + str(menuo.prntDict.get(menuo.state))  ),
        #    ( "App:"+ str(menuo.indexApp)+"/"+str(menuo.maxAppIndex) +" "+ menuo.currentAppName ),
        #    str(str_array
            
        #    ])
        print(fullPrint)
    try:
        draw(fullPrint)
    except Exception as e:
        pass
    try:
        drawOled(fullPrint)
    except Exception as e:
        pass
prnt_data_dict= dict()

def prnt_data(app_event,m):
    prnt_data_dict[app_event] = m
    n = 2
    '''
    for key,val in prnt_data_dict.items():
        oled.text(key + ": " + str(val), 0, n*10)
        oled.show()
        n += 1
    '''

def drawOled(fullPrint):
    oled.fill(0)
    for n in range(0,len(fullPrint)):
        oled.text(fullPrint[n], 0, n*10)
        oled.show()


def init(chars,lines):
   
    global screen
    global myfont
    pygame.init()
    #size = [12*chars,20*lines]
    size = [chars,lines]
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("Mock LCD")
    myfont = pygame.font.SysFont("monospace", 20)


def draw(args):
    i=0;
    global screen
    global myfont
    try:
        screen.fill((0,0,0))#erase screen contents
        while(i<len(args)):
            line= myfont.render(args[i], 2, (255,255,0))
            screen.blit(line, (0, 20*i))
            i+=1
        pygame.display.flip()
    except Exception as e:
        #print("pygame err:",e)
        pass

try:
    init(xsize,ysize) # initialize a 16x3 display#draw the three lines passed as a list
except Exception as e:
    print(e)
    print("no pygame")


