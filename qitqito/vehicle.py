class Vehicle:
    def __init__(self, velocity):
        self.velocity = velocity

    def __call__(self, velocity):
        self.velocity += velocity
        
    def __len__(self): # len関数
        return self.velocity
    
    def __repr__(self):
        return 'Velocity is {}.'.format(self.velocity)
    
    def __add__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(self.velocity + other.velocity)
        elif isinstance(other, int):
            return Vehicle(self.velocity + other)
        else:
            raise TypeError()
    
    def __radd__(self, other):
        if isinstance(other, int):
            return Vehicle(other + self.velocity)
        else:
            raise TypeError()
    
    def __mul__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(self.velocity * other.velocity)
        elif isinstance(other, int):
            return Vehicle(self.velocity * other)
        else:
            raise TypeError()
    
    def __rmul__(self, other):
        if isinstance(other, int):
            return Vehicle(other * self.velocity)
        else:
            raise TypeError()
    
    def run(self):
        raise NotImplementedError()


class Car(Vehicle):
    @property
    def run(self):
        print('Run at {}.'.format(self.velocity))
