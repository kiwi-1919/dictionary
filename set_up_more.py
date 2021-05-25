import parse


def setup():
    for each in parse.pyfind_by_suf('.\\txt', '.aw'):
        parse.choose(each)
    for each in parse.pyfind_by_suf('.\\txt', '.csv'):
        parse.parse_sents_to_words(each)


if __name__ == '__main__':
    setup()
