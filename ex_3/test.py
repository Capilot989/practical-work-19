from solution import NotSleeping


if __name__ == "__main__":
    human = NotSleeping('Мистер Смит')
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    print(human.name, 'насчитал', human.count_sheeps, 'овец')
    human.add_sheep()
    human.lost()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    print(human.name, 'насчитал', human.get_count_sheeps(), 'овец')
