grade = int(input("성적을 입력해주세요 : "))

if 89 < grade< 101 :
    print("성적은 A 입니다.")
elif 79 < grade< 90 :
    print("성적은 B 입니다.")
elif 69 < grade< 80 :
    print("성적은 C 입니다.")
elif 59 < grade< 70 :
    print("성적은 D 입니다.")
elif -1<grade< 60 :
    print("성적은 F 입니다.")
else
    print("성적은 0점~100점 입니다.")