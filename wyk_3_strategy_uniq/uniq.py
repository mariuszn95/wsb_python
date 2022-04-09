import sys

class Reader:
    def readline(self):
        pass

    def close(self):
        pass

class FileReader(Reader):
    def __init__(self, filename):
        self.file_to_read = open(filename)

    def readline(self):
        line = self.file_to_read.readline()
        if line == '':
            raise EOFError

        line = line[:-1]

        return line

    def close(self):
        self.file_to_read.close()

class ConsoleReader(Reader):
    def readline(self):
        return input()

def uniq(reader):
    try:
        last_line = ''
        while True:
            line = reader.readline()

            if line != last_line:
                print(line)
                last_line = line
    except EOFError:
        pass

def main():
    print("Argumenty do programu:", sys.argv)

    should_read_from_file = (len(sys.argv) == 2)

    if should_read_from_file:
        reader = FileReader(sys.argv[1])
    else:
        reader = ConsoleReader()

    uniq(reader)

    reader.close()


if __name__ == "__main__":
    main()

