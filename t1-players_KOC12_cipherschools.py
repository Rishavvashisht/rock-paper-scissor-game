import random 
Cchoice=["Rock","Paper"," Scissor"]
while True:
    print("Rock Paper Scissor Game ")
    youwin,computerwin=0,0
    for i in range (1,4):
        print("Round",i,"Start:")
        print(" your choice:")
        print("1.Rock" , "2.Paper" , "3.scissor",sep="\n")
        yourchoice=int(input())
        if yourchoice==1:
            print("you selected Rock")
            yourchoice="Rock"
        elif yourchoice==2:
            print("you selected Paper")
            yourchoice="Paper"
        elif yourchoice==3:
            print("you selected Scissor")
            yourchoice="scissor"
        else:
            print("invalid choice")
            break
        computerchoice= random.choice(Cchoice)
        print("computer select :",computerchoice)
        if yourchoice==computerchoice:
           print("This round is Drawn")
        elif(yourchoice=="paper" and computerchoice=="rock") or (yourchoice=="Rock" and computerchoice=="Scissor") or (yourchoice=="Scissor" and copmuterchoice=="paper") :
            youwin+=1
            print("You win this Round")
        else:
            computerwin+=1
            print("Compter win this Round")
        
    if youwin>computerwin:
        print("You win this Game:")
        print (" Score is:" , "Your score:",youwin,"Computer score:",computerwin,sep="")
    elif computerwin>youwin:
        print("You lose the Game:")
        print("Score is :","your score:",youwin,"computer score:",computerwin,sep="")
    else:
        print("Match is Drawn")
        print("Score is :","your score:",youwin,"computer score:",computerwin,sep="")
    break
