from solution import NotSleeping


if __name__ == "__main__":
    human = NotSleeping('Мистер Смит')
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    human.add_sheep()
    mr_bean = NotSleeping('Мистер Бин', 9)
    mr_bean.add_sheep()
    mr_bean.add_sheep()
    mr_bean.add_sheep()
    print(human.name, 'насчитал', human.count_sheeps, 'овец')
    print(mr_bean.name, 'насчитал', mr_bean.count_sheeps, 'овец')
