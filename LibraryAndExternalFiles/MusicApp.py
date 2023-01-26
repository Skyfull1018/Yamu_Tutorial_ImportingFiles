#audioplayerからAudioPlayerをインポート
import keyboard


def playMusic(musicNum):
    selectedMusic = ""
    if musicNum == "1" :
        #ダブルクォーテーションの中にパスを入力してください
        selectedMusic = ""
       
    
    elif musicNum == "2":
        #ダブルクォーテーションの中にパスを入力してください
        selectedMusic = ""


    elif musicNum == "3":
        #ダブルクォーテーションの中にパスを入力してください
        selectedMusic = ""

    
    
    else: 
        print("You don't have that option")
        return 
    
    player = AudioPlayer(selectedMusic)
    player.play(block=False)

    input("Stop Music with Enter Key")
    player.stop()
 
    


def displayList():
    print("1.フレディマーキュリーのやつ")
    print("2.サイダーガール _シンデレラ")
    print("3.Rhythmic Toy World 僕の声")
