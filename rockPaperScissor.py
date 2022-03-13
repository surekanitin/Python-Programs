from random import randint
def gameWin(comp,you):
     # If two values are equal, declare a tie!
    if comp == you:
        return None
     # Check for all possibilities when computer chose rock  
    elif comp =='Rock':
        if you =='Paper':
            return True
        elif you =='Scissor':
            return False
      # Check for all possibilities when computer chose paper
    elif comp =='Paper':
        if you =='Scissor':
            return True
        elif you =='Rock':
            return False
    # Check for all possibilities when computer chose scissor
    elif comp =='Scissor':
        if you =='Rock':
            return True
        elif you =='Paper':
            return False
          

def main():
    print("Number of times you want to play this game: ")
    turns=int(input())
    for i in range(turns):
        print("Computer's Turn: Rock(r) Paper(p) or Scissor(s)")
        randNo= randint(1,3)
        if randNo == 1:
            comp = 'Rock'
        elif randNo == 2:
            comp = 'Paper'
        else:
            comp = 'Scissor'
        you=input("Your Turn: Rock(r) Paper(p) or Scissor(s) ") 
        #checks if the user enter corrects input or not
        if you == 'r' or you =='p' or you == 's':
            if you=='r':
                you='Rock'
            elif you =='s':
                you='Scissor'
            else:
                you='Paper'   
            result = gameWin(comp,you)
            print(f"Computer chose {comp}")
            print(f"You chose {you}")

            if result == None:
                print("The game is a tie!")
            elif result:
                print("You Win!")
            else:
                print("You Lose!Try Again")  
        else:    
              print("Wrong Input!")
            



if __name__ == '__main__':
    main()        

