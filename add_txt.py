import os
import random
import tqdm


def add():
    l = list()
    while True:
        if input('continue/not:y/o') == 'y':
            l.append(input('add from where'))
        else:
            break
    try:
        for each in tqdm.tqdm(l):
            os.system(
                f'copy {each} {os.path.join(os.curdir, "txt", str(random.randint(0, 1000000000000000000)) + ".txt")} '
                f'/-Y')
    except:
        print('fail')
        pass


if __name__ == '__main__':
    add()
