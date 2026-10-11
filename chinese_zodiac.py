doğum_ili=int(input("daxil et:"))
bürc=doğum_ili%12
if bürc==0:
    print("year of monkey ")
elif bürc==1:
    print("year of rooster ")
elif bürc==2:
    print("year of dog ")
elif bürc==3:
    print("year of pig ")
elif bürc==4:
    print("year of rat ")
elif bürc==5:
    print("year of ox ")
elif bürc==6:
    print("year of tiger ")
elif bürc==7:
    print("year of rabbit ")
elif bürc==8:
    print("year of dragon ")
elif bürc==9:
    print("year of snake ")
elif bürc==10:
    print("year of horse ")
else:
    print("year of sheep ")
