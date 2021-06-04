import match
import compare
import os
import add_txt
import set_up
import set_up_more
import dataframe
import clean

os.chdir(os.curdir)
if __name__ == '__main__':
    try:
        os.mkdir(".\\txt")
        os.mkdir(".\\df")
    except:
        pass
    string = input('''setup:1
compare:2
match:3''')
    if string == '1':
        add_txt.main()
        set_up.run()
        set_up_more.setup()
        os.system("pause")
        dataframe.setup()
        clean.remove()
    elif string == '2':
        if os.listdir('.\\txt'):
            compare.compare()
        else:
            print("there is nothing")
    elif string == "3":
        if os.listdir('.\\txt'):
            match.main()
        else:
            print("there is nothing")
    else:
        print("again")
        os.system("pause")
    os.system("start run.exe")
