#ImageAppをimageとしてインポート
#MusicAppをmusicとしてインポート


print("What do you want to do?")
print("1.Display Picture \n2.Play Music")
inputNum = input("Enter: ")

if inputNum == "1":
    print("Which picture do you want to see?")
    #imageのリストを表示
    imageNum = input("Enter: ")
    #imageNumを使って画像を表示
    

elif inputNum == "2":
    print("Which music do you want to listen?")
    #musicのリストを表示
    musicNum = input("Enter: ")
    #musicNumを使って音楽を再生

else: 
    print("You don't have that option")