from audioplayer import AudioPlayer 
import time

player = AudioPlayer("./musics/フレディマーキュリーのやつ.mp3")


player.play(block=False)
time.sleep(5)


