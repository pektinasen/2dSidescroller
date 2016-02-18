class Char():

    def __init__(self,image,position):
        self.pos = position
        self.image = image
        self.instance = 0
        self.acceleration = 0
        self.life_count = 3
        self.in_air = False

    def __str__(self):
        return str(self.instance)+" : "+str(self.acceleration)
    
    def accelerate(self):
        pass

    def deccelerate(self):
        pass

    def jump(self):
        self.pos[1] -= 10 
  
    #Char turns small after getting hit
    def got_hit(self):
        self.instance = 0

    # instance 0 == little ; 1 == Big ; 2 == Flower ; 3 == Item2 
    def check_instance(self,instance):
        return self.instance != instance and not (instance == 1 and self.instance > 1)

    #collecting an item, which can change chars instance
    def change_instance(self,item_instance):
        if(self.check_instance(item_instance)):
            self.instance = item_instance
        print("current instance ", str(self.instance))
        
    #character died... losing instance and life
    def die(self):
        self.instance = 0
        self.life_count -= 1 
        print("character died... you suck!")
    
    def show_yourself(self):
        return self.image
