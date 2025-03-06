
# The Atom class as provided by the course


GLOBAL_NAME = "Francis"

def say_hi(global_name):
    """
    Description: say_hi is a function defined outside of main. 
    """
    print(f"Hello, I am {global_name}!")


class Atom:

    global_name = "Keith"

    def __init__(self, atomic_number, symbol, name, atomic_mass):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_mass = atomic_mass

    @staticmethod
    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.atomic_number}"

    def neutrons(self):
        number = self.atomic_mass - self.atomic_number
        print(f"{self.name} has {number} neutrons")
        return number

    def grams_to_moles(self, grams):
        moles = grams / self.atomic_mass
        print(f"{grams:.1f} g is {moles:.1f} moles of {self.symbol}")
        return moles

    def say_hi_inside_a_class(self):
        say_hi(self.global_name)


if __name__ == "__main__":
    """
    Description: My main function creates instances of Atom and calls some class methods.

    """
    oxygen = Atom(8, 'O', 'Oxygen', 15.999)
    carbon = Atom(6, 'C', 'Carbon', 12.001)

    # Call class methods
    oxygen.neutrons()
    oxygen.grams_to_moles(24)
    carbon.grams_to_moles(24)

    # Call the global function from inside the class
    oxygen.say_hi_inside_a_class()

    # Print the global variable from inside the class
    print(f"Global variable inside the class definition (class variable): {Atom.global_name}")

    # Print the global variable from outside the class
    print(f"Global variable outside the class definition: {GLOBAL_NAME}")




