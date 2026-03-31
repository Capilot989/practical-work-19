
class TrafficLight:
    def __init__(self) -> None:
        self.permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']
        self.current_signal_index = 0
        self.current_signal = self.permissible_values[self.current_signal_index]

    def next_signal(self) -> None:
        self.current_signal_index += 1
        self.current_signal = self.permissible_values[self.current_signal_index % 4]
