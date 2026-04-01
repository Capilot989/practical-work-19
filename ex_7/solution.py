class TrafficLight:
    """
    A class representing a traffic light with cyclic signal changes.

    This class models a traffic light that cycles through signals in the
    order: green -> yellow -> red -> yellow -> green -> ...
    It maintains the current signal and provides a method to advance to the next signal.

    Attributes:
        permissible_values: List of valid signal states in cycle order
        current_signal_index: Index of the current signal in permissible_values
        current_signal: Current signal state as a string
    """
    def __init__(self) -> None:
        """
        Initialize a new TrafficLight instance with initial signal set to 'зеленый'.
        """
        self.permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']
        self.current_signal_index = 0
        self.current_signal = self.permissible_values[self.current_signal_index]

    def next_signal(self) -> None:
         """
        Advance the traffic light to the next signal in the cycle.

        The cycle order is: зеленый -> желтый -> красный -> желтый -> зеленый -> ...
        The index wraps around using modulo to create an infinite cycle.
        """
        self.current_signal_index += 1
        self.current_signal = self.permissible_values[self.current_signal_index % 4]
