#login and signup
from tkinter import *
from PIL import Image, ImageTk

def click_me():
    email = email_entry.get()
    password = password_entry.get()
    print("Email:", email)
    print("Password:", password)


# -------- Signup Window --------
def open_signup():

    signup = Toplevel(root)
    signup.title("Create Amazon Account")
    signup.geometry("500x500")
    signup.configure(bg="white")

    Label(signup,
          text="Create Account",
          font=("Helvetica",20,"bold"),
          bg="white").pack(pady=20)

    # Name
    Label(signup,text="Your Name",bg="white",
          font=("Helvetica",10,"bold")).pack(anchor="w", padx=40)

    name_entry = Entry(signup,font=("Helvetica",12),relief="solid")
    name_entry.pack(padx=40,pady=5,fill="x")

    # Email
    Label(signup,text="Email",bg="white",
          font=("Helvetica",10,"bold")).pack(anchor="w", padx=40)

    email_signup = Entry(signup,font=("Helvetica",12),relief="solid")
    email_signup.pack(padx=40,pady=5,fill="x")

    # Password
    Label(signup,text="Password",bg="white",
          font=("Helvetica",10,"bold")).pack(anchor="w", padx=40)

    pass_signup = Entry(signup,font=("Helvetica",12),
                        show="*",relief="solid")
    pass_signup.pack(padx=40,pady=5,fill="x")

    # Register Button
    Button(signup,
           text="Register",
           font=("Helvetica",12,"bold"),
           bg="#FFD814",
           relief="flat").pack(pady=25)



# -------- Hover Effects --------
def on_enter(e):
    sign_btn['bg'] = "#F7CA00"

def on_leave(e):
    sign_btn['bg'] = "#FFD814"


root = Tk()
root.title("Amazon Sign-In")
root.geometry("900x600")
root.configure(bg="#EAEDED")
root.resizable(False, False)


# -------- Amazon Logo --------
logo = Image.open("Projects/a2.png")
logo = logo.resize((150,85))
logo = ImageTk.PhotoImage(logo)

logo_label = Label(root, image=logo, bg="#EAEDED")
logo_label.pack(pady=20)


# -------- Main Card --------
frame = Frame(root, bg="white", bd=1, relief="solid")
frame.pack(pady=10, ipadx=10, ipady=10)


# -------- Title --------
Label(frame,text="Sign in",
      font=("Helvetica",22,"bold"),
      bg="white").pack(anchor="w", padx=25, pady=(20,10))


# -------- Email --------
Label(frame,text="Email or mobile phone number",
      font=("Helvetica",10,"bold"),
      bg="white").pack(anchor="w", padx=25)

email_entry = Entry(frame,font=("Helvetica",12),relief="solid")
email_entry.pack(padx=25,pady=6,ipady=4,fill="x")


# -------- Password --------
Label(frame,text="Password",
      font=("Helvetica",10,"bold"),
      bg="white").pack(anchor="w", padx=25,pady=(10,0))

password_entry = Entry(frame,font=("Helvetica",12),
                       show="*",relief="solid")
password_entry.pack(padx=25,pady=6,ipady=4,fill="x")


# -------- Sign In Button --------
sign_btn = Button(frame,
       text="Sign-In",
       font=("Helvetica",12,"bold"),
       bg="#FFD814",
       activebackground="#F7CA00",
       relief="flat",
       command=click_me,
       cursor="hand2")

sign_btn.pack(fill="x", padx=25, pady=18, ipady=6)

sign_btn.bind("<Enter>", on_enter)
sign_btn.bind("<Leave>", on_leave)


# -------- Terms --------
Label(frame,
      text="By continuing, you agree to Amazon's\nConditions of Use and Privacy Notice.",
      font=("Helvetica",9),
      fg="gray",
      bg="white",
      justify="left").pack(padx=25,pady=(0,20))


# -------- Divider --------
Label(root,
      text="────────────  New to Amazon?  ────────────",
      bg="#EAEDED",
      fg="gray",
      font=("Helvetica",10)).pack(pady=10)


# -------- Create Account Button --------
Button(root,
       text="Create your Amazon account",
       font=("Helvetica",11),
       width=32,
       bg="white",
       relief="solid",
       bd=1,
       cursor="hand2",
       command=open_signup).pack(ipady=4)


root.mainloop()