from solution import TrafficLight


if __name__ == "__main__":
    seven_roads = TrafficLight()
    print(seven_roads.current_signal)
    for _ in range(5):
        seven_roads.next_signal()
    print(seven_roads.current_signal)
