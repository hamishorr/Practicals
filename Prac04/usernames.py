def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("enter username:")
    check(username,usernames)

def check(name,list):
    finished = False
    while not finished:
        if name in list:
            print("access granted")
            finished = True
        else:
            print("access is denied")
            name = input("enter username:")


main()
