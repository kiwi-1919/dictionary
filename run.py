import os
import add_txt
import sys

os.chdir(os.curdir)


def run():
    try:
        os.mkdir(".\\txt")
        os.mkdir(".\\df")
    except:
        pass
    string = input('''setup:1
compare:2
match:3
exit:4''')
    if string == '1':
        if os.listdir('.\\txt'):
            os.system(".\\setup_dataframe.bat")
        else:
            add_txt.add()
    elif string == '2':
        if os.listdir('.\\txt'):
            os.system(".\\compare.bat")
        else:
            print("there is nothing")
    elif string == "3":
        if os.listdir('.\\txt'):
            os.system(".\\match.bat")
        else:
            print("there is nothing")
    elif string == '4':
        sys.exit()
    else:
        print("again")
        os.system("pause")
    os.system("python -m run")


if __name__ == '__main__':
    run()
