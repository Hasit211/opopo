class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
    def start(self):
        print('started')
    def stop(self):
        print('stopped')

    def accelerate(self):
        print('accelerate')
    def change_gear(self,gear_type):
        print('gearchanged')
audi = Car('a6','red','audi','240')
print(audi.start())
