class ReplApplication:
    def __init__(self):
        self.should_quit = False
    
    def run(self):
        self.on_start()

        while self.should_quit is False:
            self.on_promt()
            text = input()
            self.on_input(text)

    def on_start(self):
        pass

    def on_promt(self):
        pass

    def on_input(self, text):
        pass

class MyApp(ReplApplication):
    def on_start(self):
        print("Hello in MyApp")

    def on_input(self, text):
        if text == 'exit':
            print('Zamykanie...')
            self.should_quit = True
        else:
            print(text)
        
def main():
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()