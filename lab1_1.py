class UpCounter:
    def __init__(self, stepsize=1):
        self.count_value = 0
        self.stepsize = stepsize
        
    def count(self):
        return self.count_value
    
    def update(self):
        self.count_value += self.stepsize

class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.stepsize


up = DownCounter(2)
up.update()
up.update()
print(up.count())