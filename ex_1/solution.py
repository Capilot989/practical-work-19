

class Dog:
    """
       A class representing a dog.

       This class provides basic functionality for a dog, including
       storing its name and making it bark.

       Attributes:
           name: The name of the dog
       """
    def __init__(self, name: str) -> None:
        """
              Initialize a new Dog instance.

              Args:
                  name: The name of the dog
              """
        self.name = name

    def say(self) -> None:
        """
               Make the dog bark.

               Prints 'Гав!' to the console.
               """
        print('Гав!')
