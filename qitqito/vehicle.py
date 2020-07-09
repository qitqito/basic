class Vehicle:
    def __init__(self, velocity, name):
        self.velocity = velocity
        self.name = name

    def __call__(self, velocity):
        self.velocity += velocity
        
    def __len__(self): # len関数
        return self.velocity
    
    def __repr__(self):
        return 'Velocity is {}.'.format(self.velocity)
    
    def __getitem__(self, key):
        return self.name[key]

    def __setattr__(self, name, value):
        super().__setattr__(name, value) # これが無いとプロパティに代入されない
        message = "{} is {}"
        print(message.format(name, value))

    def __iter__(self):
        return self

    def __next__(self):
        if self.velocity >= 110:
            raise StopIteration()
        self.velocity += 1
        return self.velocity

    def __add__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(self.velocity + other.velocity, self.name)
        elif isinstance(other, int):
            return Vehicle(self.velocity + other, self.name)
        else:
            raise TypeError()
    
    def __radd__(self, other):
        if isinstance(other, int):
            return Vehicle(other + self.velocity, self.name)
        else:
            raise TypeError()
    
    def __mul__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(self.velocity * other.velocity, self.name)
        elif isinstance(other, int):
            return Vehicle(self.velocity * other, self.name)
        else:
            raise TypeError()
    
    def __rmul__(self, other):
        if isinstance(other, int):
            return Vehicle(other * self.velocity, self.name)
        else:
            raise TypeError()
    
    def run(self):
        raise NotImplementedError()


class Car(Vehicle):
    @property
    def run(self):
        print('Run at {}.'.format(self.velocity))
