def entry():
    n=input("Enter the vehicle Number :\n")
    if n not in s:
        s[s.index(-1)]=n
        print(f"Your vehicle {n} has been registered.\nYou can park on {s.index(n)+1}.")
    else:
        print("Oops! ,It seems you entered it wrong\n\tTry again.")

def checkout():
    n=input("Enter your Vehicle Number :\n")
    if n in s:
        s.insert(s.index(n),-1)
        s.remove(n)
        #print(s)
        print("Your vehicle is ready to checkout.")
        
    else:
        print("Oops! ,It seems you entered it wrong\n\tTry again.")


def main():
    while True:
        if -1 not in s:
            s.append(-1)
        #print("\t\t",s)
        print("\nGreetings,\nEnter any option\n1.Entry\n2.Checkout\n3.Exit")
        try:
            e=int(input())
            if e==1:
                entry()
            elif e==2:
                checkout()
            elif e==3:
                break
            if e>3:
                raise Exception
        except:
            print("Oops! ,It seems you entered it wrong\n\tTry again.")
s=[]
main()
