class Reader:
    def readline(self):
        '''Ta funkcja zwraca dane, jeżeli danych nie ma, to powinna rzucić wyjątek EOFError.'''
    def close(self):
        pass


class ConsoleReader(Reader):
    def readline(self):
        return input()

class FileReader(Reader):
    # init/open

    def readline(self):
        ...

    def close(self):
        ...


def uniq(reader):
    last_line = ''

    while True:
        line = reader.readline()
        if line != last_line:
            print(line)
            last_line = line

import sys

def main():
    print("argv:", sys.argv)
    if len(sys.argv) == 1:
        reader = ConsoleReader()
    else:
        reader = FileReader(sys.argv[1])


    try:
        uniq(reader)
    except (EOFError, KeyboardInterrupt):
        pass

    reader.close()





if __name__ == '__main__':
    main()