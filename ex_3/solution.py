

class NotSleeping:
    """
      A class representing a person who cannot fall asleep and counts sheep.

      This class tracks the number of sheep counted as a method to help
      the person fall asleep.

      Attributes:
          name: The name of the person who can't sleep
          count_sheeps: The number of sheep counted so far
    """
    def __init__(self, name: str, count: int=0) -> None:
        """
            Initialize a new NotSleeping instance.

            Args:
                name: The name of the person who can't sleep
                count: Initial number of sheep counted (default: 0)
        """
        self.name = name
        self.count_sheeps = count

    def add_sheep(self) -> None:
        """
               Increment the sheep count by one.

               This method represents counting one additional sheep in an attempt
               to fall asleep.
        """
        self.count_sheeps += 1

    def lost(self) -> None:
        """
        Reset the sheep count to zero.

        This method represents losing count of the sheep and starting over.
        """

        self.count_sheeps = 0

    def get_count_sheeps(self) -> int:
        """
        Get the current number of sheep counted.

        Returns:
            The current sheep count
        """
        return self.count_sheeps
