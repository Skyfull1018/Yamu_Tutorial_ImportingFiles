
class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)


#コンストラクタ（作成時）に引数を渡してインスタンスを作成し、そのインスタンスでsay_helloを実行