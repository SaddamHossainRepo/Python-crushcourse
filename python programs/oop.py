class Computer:

    def config(self):
        print("i5, 4gb, 1Tb")


comp1 = Computer()
comp2 = Computer()

Computer.config(comp1)
Computer.config(comp2)