n=18
g=1
print("You've total 9 guesses")
while (True):
    i=int(input("Enter any number : "))
    print("you are done with",g,"guesses")
    g=g+1
    if i==n:
        print("You won",n,"is the correct answer")
        break
    elif i>=15 and i<18:
        print("you are close",g)
        continue
    elif i>18 and i<=20:
        print("you are close",g)
        continue
    elif g==10:
        print("game over! you are done with your 9 guesses")
        print("You have took",g,"guesses")
        break
