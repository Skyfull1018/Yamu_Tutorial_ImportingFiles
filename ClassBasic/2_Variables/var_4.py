#以下のクラスはtemplateが定義されておらず、エラーがはかれます。templateを追加してください。
#期待される出力は Hello my name is {arbitrary name}　です
class Greeting:

  

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(self.template + self.name)


Tenma = Greeting("Tenma")
Iruma = Greeting("Iruma")

Tenma.say_hello()
Iruma.say_hello()