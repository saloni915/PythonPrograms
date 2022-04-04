from tkinter import *

root= Tk()

# Email verification pop up window
def verifyMessage():
    x=Toplevel(root)
    x.geometry("500x60+80+200")
    x.title('Verify Notification')
    Label(x,text='A confimation mail for verification is sent to your given mail id.').pack()


# Sign in successful pop up window
def SignInSuccessMessage():
    x=Toplevel(root)
    x.geometry("500x60+80+200")
    x.title('Signed In successfully')
    Label(x,text='You have signed in successfully.').pack()


#Tkinter main window
def main():
    root.geometry("500x300")
    root.title('Sign in')
    Label(root,text='Create a New Account',font='arial 20 bold').pack()
    Label(root,text='First Name').place(x=20,y=50)
    Entry(root,width=50).place(x=100,y=50)
    Label(root,text='Last Name').place(x=20,y=100)
    Entry(root,width=50).place(x=100,y=100)
    Label(root,text='Email address').place(x=20,y=150)
    Entry(root,width=50).place(x=100,y=150)
    Button(root,text='Verify Email',command=verifyMessage, bg='ghost white').place(x=190,y=200)
    Button(root,text='Sign In',command=SignInSuccessMessage,bg='ghost white').place(x=200,y=250)
    root.mainloop()          # runs the Tkinter eventloop and listens for the events


if __name__ == "__main__":
    main()

