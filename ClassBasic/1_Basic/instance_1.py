
class Car:
    #__init__はインスタンス作成時に一回呼ばれる関数
    #この関数は必ず作らないといけないわけでなく、初期設定が必要ない場合は入れなくて良い 
    def __init__(self,color,brand):
        #self.変数でプロパティを作る。
        self.myColor=color
        self.myBrand=brand
    
    def move(self):
        print(self.myColor,self.myBrand,'car is moving now')


#インスタンスを作成して新しい車を作ってください。

#そのあと、move関数を実行してください。