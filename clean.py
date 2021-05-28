import os
import tqdm


def remove():
    for each in tqdm.tqdm(os.listdir('.\\txt')):
        os.remove(each + '.aw')
        os.remove(each + '.aw.txt')
        os.remove(each + '.csv')
        os.remove('storey_' + each + '.csv')


if __name__ == '__main__':
    remove()
