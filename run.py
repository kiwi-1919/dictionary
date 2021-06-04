import os

os.chdir(os.curdir)


def run():
    try:
        os.mkdir(".\\txt")
        os.mkdir(".\\df")
    except:
        pass
    string = input('''setup:1
compare:2
match:3''')
    if string == '1':
        os.system(".\\setup_dataframe.bat")
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
    else:
        print("again")
        os.system("pause")
    os.system("python -m run")


if __name__ == '__main__':
    run()
