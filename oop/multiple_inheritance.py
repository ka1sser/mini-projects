# Topic: multiple inheritance [ C(A,B) ] and multilevel inheritance C(B) <- B(A) <- A


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")


class Rabbit(Prey):

    def run(self):
        print(f"{self.name} is running!")


class Hawk(Predator):

    def fly(self):
        print(f"{self.name} is flying!")


class Fish(Prey, Predator):

    def swim(self):
        print(f"{self.name} is swimming!")


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.eat()
fish.sleep()
fish.hunt()
fish.flee()
fish.swim()
