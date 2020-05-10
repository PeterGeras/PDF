import os
from tkinter import *
from tkinter.filedialog import askopenfilename


# Window
root = Tk()
root.title(".doc to .pdf")
root.configure(background="white")


# Click function
def click():
    root.filename = askopenfilename(initialdir=".",
                                    title="Select a word document",
                                    filetypes=(("word documents", ".doc* .dot*"),))

    filename = os.path.basename(root.filename)

    if filename:
        print(1)
        Label(root, text=filename)\
            .grid(row=3, column=0, sticky=S)
    else:
        print(2)
        for label in root.grid_slaves():
            print(str(label.grid_location(1,0)))



    # Conversion button
    # Button(root, text="Choose File", width=10, command=click) \
    #     .grid(row=2, column=0, sticky=S)

    return


# Photo
img_word_pdf = PhotoImage(file="word-pdf.ppm")
Label(root, image=img_word_pdf, bg="white")\
    .grid(row=0, column=0, sticky=N)

# Information
Label(root, text="Select a word document to convert to PDF", bg="white", fg="black", font="arial 14 bold")\
    .grid(row=1, column=0, sticky=E)

# File select button
Button(root, text="Choose File", width=10, command=click)\
    .grid(row=2, column=0, sticky=S)


root.mainloop()
