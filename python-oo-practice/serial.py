"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
# Makes the SerialGenerator starts at (start = 100)
    def __init__(self,start = 100):
        self.start = self.next = start
    
# Representation
    def __repr__(self):
        return(f'The first SerialGenerator: {self.start}, next SerialGenerator: {self.next}')

# Count next serial number and return it
    def generate(self):
        self.next += 1
        return self.next -1
    
# Reset the count to starting serial 
    def reset(self):
        self.next = self.start