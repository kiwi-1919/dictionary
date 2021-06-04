import os

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
        os.system("setup_dataframe.bat")
    elif string == '2':
        os.system("compare.bat")
    elif string == "3":
        os.system("match.bat")
    else:
        print("again")
        os.system("pause")
    os.system("python -m run")
