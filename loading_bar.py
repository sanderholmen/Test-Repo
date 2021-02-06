import sys
from time import sleep


def gen_list():
    list = []
    for i in range(1,8213):
        list.append(i)
    return list



def loading(list):
    N = len(list)
    print(N)
    loadbar = {}
    for index in range(1,101):
        symbol = '|' * index
        loadbar[index] = symbol

    step = len(list)//100
    counter = 0
    key = 1
    for item in (list):
        counter += 1
        print('Loading'+ str(key))
        print(loadbar[key].ljust(100, '-'))
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sleep(0.001)

        if counter >= step and key <100:
            counter = 0
            key += 1
    print('\n\n')


def loading_list(count,list):
    progress = len(list)/100
    step = len(list)/50
    base = 0
    N = 0
    while count > int(base):
        N += 1
        base += progress
        if N == 1:
            input()
    percentage = N
    base = 0
    N = 0
    while count > int(base):
        N += 1
        base += step
    symbol = ''
    symbol = '|' * N

    print(f'{percentage}%')
    print(symbol.ljust(50, '-'))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    if count == len(list):
        print('\n\nDone\n')


def loading_number(count,total):

    progress = total/100
    step = total/50
    base = 0
    N = 0
    while count > int(base):
        N += 1
        base += progress
    percentage = N
    base = 0
    N = 0
    while count > int(base):
        N += 1
        base += step
    symbol = ''
    symbol = '|' * N

    print(f'{percentage}%')
    print(symbol.ljust(50, '-'))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    if count == total:
        print('\n\nDone\n')


def loading_number2(count,total):
    symbol = ''
    if total < 10:
        if count == total-1:
            print('Processing...')
            print(symbol.ljust(5, '|'))
            print('Done')
            return count
        symbol = '|' * count
        print('Processing...')
        print(symbol.ljust(5, ' '))
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        return count
    elif total < 100:
        if count == 0:
            print('0%')
            print(symbol.ljust(50, '-'))
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            return count
        elif count == total-1:
            print('100%')
            print(symbol.ljust(50, '|'))
            print('Done')
            return count
        else:
            progress = total/10
            add_bar = 0
            for i in range(1,11):
                if progress * i > count:
                    symbol = '|' * i*5
                    if i > 9:
                        i = 9
                    print(f'{i*10}%')
                    print(symbol.ljust(10, '-'))
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[F")
                    return count
    else:
        if count == 0:
            print('0%')
            print(symbol.ljust(50, '-'))
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            return count
        elif count == total-1:
            print('100%')
            print(symbol.ljust(50, '|'))
            print('Done')
            return count
        else:
            progress = total/100
            add_bar = 0
            for i in range(1,101):
                if i % 2 == 0:
                    add_bar += 1
                if progress * i > count:
                    symbol = '|' * add_bar
                    if i > 99:
                        i = 99
                    print(f'{i}%')
                    print(symbol.ljust(50, '-'))
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[F")
                    return count


def load_hyphen(count, total):
    symbol = ''
    if total < 200:
        if count % 10 == 0:
            print(symbol.ljust(10, ' '))
        elif count % 10 == 1:
            symbol = '-' * 1
            print(symbol.ljust(10, ' '))
        elif count % 10 == 2:
            symbol = '-' * 2
            print(symbol.ljust(10, ' '))
        elif count % 10 == 3:
            symbol = '-' * 3
            print(symbol.ljust(10, ' '))
        elif count % 10 == 4:
            symbol = '-' * 4
            print(symbol.ljust(10, ' '))
        elif count % 10 == 5:
            symbol = '-' * 5
            print(symbol.ljust(10, ' '))
        elif count % 10 == 6:
            symbol = '-' * 6
            print(symbol.ljust(10, ' '))
        elif count % 10 == 7:
            symbol = '-' * 7
            print(symbol.ljust(10, ' '))
        elif count % 10 == 8:
            symbol = '-' * 8
            print(symbol.ljust(10, ' '))
        elif count % 10 == 9:
            symbol = '-' * 9
            print(symbol.ljust(10, ' '))
        else:
            None
        sys.stdout.write("\033[F")
    else:

        for i in range(1,51):
            if count % i == 0:
                input()
                symbol = '-' * i
                print(symbol.ljust(50, ' '))
                sys.stdout.write("\033[F")






if __name__ == '__main__':
    list = gen_list()

    # loading(iter_list)

    N = 0
    for n,i in enumerate(list):
        N += 1
        sleep(0.07)

        # loading_number(n, len(list))
        load_hyphen(n, len(list))
