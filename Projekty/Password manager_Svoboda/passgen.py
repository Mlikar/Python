from tkinter import *
from random import randint


def passGenerator():
    # Password Generator window.
    window = Tk()

    window.title("Password Generator")

    myPassword = chr(randint(33,126))

    def newRand():
        pwEntry.delete(0, END)
        pwLength = int(myEntry.get())

        myPass = ""

        for x in range(pwLength):
            myPass += chr(randint(33, 126))

        pwEntry.insert(0, myPass)

    def clipper():
        window.clipboard_clear()
        window.clipboard_append(pwEntry.get())


    # Label frame.
    lf = LabelFrame(window, text="Pozadovany pocet znaku hesla?")
    lf.pack(pady=20)

    # Create Entry Box for number of characters.
    myEntry = Entry(lf, font=("Helvetica", 12))
    myEntry.pack(pady=20, padx=20)

    # Create entry box for returned password.
    pwEntry = Entry(window, text="", font=("Helvetica", 12), bd=0, bg="systembuttonface")
    pwEntry.pack(pady=20)

    # Frame for buttons.
    myFrame = Frame(window)
    myFrame.pack(pady=20)

    # Create buttons
    myButton = Button(myFrame, text="Generovat heslo", command=newRand)
    myButton.grid(row=0, column=0, padx=10)

    clipBtn = Button(myFrame, text="Kopirovat", command=clipper)
    clipBtn.grid(row=0, column=1, padx=10)


    window.mainloop()