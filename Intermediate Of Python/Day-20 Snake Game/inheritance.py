class Animal:
    def __int__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathing under water.")

    def swim(self):
        print("Moving in Water.")

nemo = Fish()
nemo.breathe()
nemo.swim()
