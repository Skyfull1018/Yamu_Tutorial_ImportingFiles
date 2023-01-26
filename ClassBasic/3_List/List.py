#for loopを使い、teamリスト内のインスタンスのattack関数を呼び出してください。
#期待される出力：
    # 勇者はスライムを攻撃した
    # 戦士はスライムを攻撃した
    # 魔法使いはスライムを攻撃した

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

team = []
team.append(Player("勇者"))
team.append(Player("戦士"))
team.append(Player("魔法使い"))

for player in team:
    #ここにコードを追加してください
