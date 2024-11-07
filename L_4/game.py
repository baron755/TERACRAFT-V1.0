from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from random import *
from direct.gui.OnscreenImage import OnscreenImage

#file = input("number file: (1,2,3):")
#normal_file = "save_" + file + ".txt"
#print(normal_file)

#if file != "1" or "2" or "3":
    #file = "3"

lol_test = input("random or plat (1,2)  ")

if lol_test == '1':
    max_max = randint(1, 5)

    with open("land.txt", 'w') as f:
        f.write("30")
        f.write('\n')
        for i in range(50):
            for i in range(49):
                seed_1 = randint(0, max_max)
                f.write(str(seed_1)+' ')
                seed_1 = randint(0, max_max)
            f.write(str(seed_1))
            f.write('\n')
            
if lol_test == '2':
    with open("land.txt", 'w') as f:
        f.write("30")
        f.write('\n')
        for i in range(50):
            for i in range(50):
                f.write("1" + " ")
            f.write("1" + " ")
            f.write('\n')

print("    ")
print("turn_left = q")
print("turn_right = e")
print("forward = w")
print("back = s")
print("left = a")
print("right = d")
print("    ")
print("switch_camera = c")
print("    ")
print("switch_mode = z")
print("    ")
print("up = space")
print("down = shift")
print("    ")
print("build = b")
print("destroy = v")
print("    ")
print("save = f1")
print("load = f2")
print("    ")
print("save_2 = f4")
print("load_2 = f5")
print("    ")
print("save_3 = f7")
print("load_3 = f8")
print("    ")
print("0-9 or 'r' = blocks")
print("have fun")
print("    ")
print("dont press r and then b")
print("please")
print("    ")
class Game(ShowBase):# напиши тут код основного вікна гри
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand("land.txt")
        x=10
        y=10
        self.hero = Hero(((x//2), (y//2), 2), self.land)
        base.camLens.setFov(90)
        
game = Game()
game.run()