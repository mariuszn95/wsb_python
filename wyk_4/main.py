# wzorzec polecenie
# kazdy wpis w menu jest osobnym obiektem
#
# 1. tekst programisty
# 2. tekst ....
# 3. ....
#
# Wybor: 1
#
# 1. tekst programisty
# 2. tekst ....
# 3. exit
#
# Wybor: 3

from menu import Menu, MenuCommand, ExitCommand


class HelloCommand(MenuCommand):
    def execute(self):
        print("Hello")

    def description(self):
        return "Print hello"


def main():
    menu = Menu()

    menu.register(HelloCommand())
    menu.register(ExitCommand(menu))

    menu.run()


if __name__ == "__main__":
    main()
