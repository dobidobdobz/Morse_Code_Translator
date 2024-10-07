from tkinter import *
from tkinter import messagebox

# dictionaries with data latin alphabet to morse code & vice versa
alphabet_morse = {" ": " ", "A": "·−", "B": "−···", "C": "−·−·", "D": "−··", "E": "·", "F": "··−·", "G": "−−·", "H": "····", "I": "··", "J": "·−−−", "K": "−·−", "L": "·−··", "M": "−−", "N": "−·", "O": "−−−", "P": "·−−·", "Q": "−−·−", "R": "·−·", "S": "···", "T": "−", "U": "··−", "V": "···−", "W": "·−−", "X": "−··−", "Y": "−·−−", "Z": "−−··", 0: "−−−−−", 1: "·−−−−", 2: "··−−−", 3: "···−−", 4: "····−", 5: "·····", 6: "−····", 7: "−−···", 8: "−−−··", 9: "−−−−·"}
morse_alphabet = {"": " ", "·−": "A", "−···": "B", "−·−·": "C", "−··": "D", "·": "E", "··−·": "F", "−−·": "G", "····": "H", "··": "I", "·−−−": "J", "−·−": "K", "·−··": "L", "−−": "M", "−·": "N", "−−−": "O", "·−−·": "P", "−−·−": "Q", "·−·": "R", "···": "S", "−": "T", "··−": "U", "···−": "V", "·−−": "W", "−··−": "X", "−·−−": "Y", "−−··": "Z", "−−−−−": 0, "·−−−−": 1, "··−−−": 2, "···−−": 3, "····−": 4, "·····": 5, "−····": 6, "−−···": 7, "−−−··": 8, "−−−−·": 9}

# research color schemes
BEIGE = "#E4C59E"
BLACK = "#1D1D1F"
WHITE = "#fefefe"
GREEN = "#32CD32"

SWITCHED = False


def invalid_entry():
    # popup error messagebox for tkinter and implemented, https://www.tutorialspoint.com/how-to-create-a-tkinter-error-message-box,
    # error displays according to the status of SWITCHED
    if not SWITCHED:
        messagebox.showerror('Error', 'Invalid Entry: The input is not in the latin alphabet!')
    else:
        messagebox.showerror('Error', 'Invalid Entry: The input is not written in Morse code!')


def switch_translate_to():
    # changes SWITCHED STATUS everytime button is clicked
    global SWITCHED
    if not SWITCHED:
        SWITCHED = True
    else:
        SWITCHED = False

    # clear morse-field
    translated_box.delete("1.0", END)

    # make labels global, so it can be used and changed within the function for it exists outside the scope.
    global latin_alphabet_label
    global morse_code_Label

    # changes text according to status of SWITCHED
    if SWITCHED:
        # recreate the labels with new texts if == True
        latin_alphabet_label.config(text="Morse")
        morse_code_Label.config(text="Latin Alphabet")
    else:
        # recreate the labels with new texts if == False
        latin_alphabet_label.config(text="Latin Alphabet")
        morse_code_Label.config(text="Morse")


def translate():
    # executes the translation code if SWITCHED STATUS is == False
    if not SWITCHED:
        translated_box.delete("1.0", END)

        # gets data from field to be translated and placed in a variable
        to_be_translated = translate_box.get().upper()

        # adds spaces between every character
        spaced_to_translate = " ".join(to_be_translated)

        try:
            # list comprehension, matching characters/keys from dictionery & returning the value in morse_code (list)
            morse_code = [alphabet_morse[f"{x}"] for x in spaced_to_translate]

            # looping through morse-code translated list & inserting it in the GUI text-box
            for x in morse_code:
                translated_box.insert(index="end", chars=f"{x}")
        except KeyError:
            # catches invalid entries and displays popup
            invalid_entry()

    else:
        # executes the translation code if SWITCHED STATUS is == True
        translated_box.delete("1.0", END)

        # gets data & splits it separating the words from one another
        to_split = translate_box.get().split("  ")

        # further splits the words into characters (we have lists with a list)
        split = [x.split(" ") for x in to_split]

        # list comp, to split the characters also acknowledges spaces as characters
        latin_text = [y for x in split for y in x]

        try:
            # list comprehension, matching characters/keys from dictionery & returning the value in translated_latin_text list
            translated_latin_text = [morse_alphabet[f"{x}"] for x in latin_text]

            # loops through list and inserts translation into GUI
            for x in translated_latin_text:
                translated_box.insert(index="end", chars=f"{x}")
        except KeyError:
            # catches invalid entries and displays popup
            invalid_entry()


# UI built here
# initialize tkinter  class
window = Tk()

# creates window, title of window, adds icon, background color set to black
window.title("Morse Code Translator")
window.iconbitmap("icon.ico")
window.config(bg=BLACK)

# setup_logo centered on grid system
morse_logo = PhotoImage(file="logo.png")
logo_label = Label(image=morse_logo, bg=BLACK)
logo_label.config(bg=BLACK)
logo_label.grid(column=1, row=0)

# set up the different fields & placed on grid
canvas = Canvas(width=900, height=50, bg=BLACK, highlightthickness=0)
canvas.create_text(450, 25, text="TRANSLATOR", font=("Twentieth Century", 40, "bold"), fill=BLACK, )
canvas.config(bg=GREEN, bd=1)
canvas.grid(column=1, row=1, pady=10)

# setup switch buttons translate from morse to latin / latin to morse
switch_translation_button = Button(text="Switch", font=("Twentieth Century", 10, "bold"), command=switch_translate_to, width=47, bg=BLACK, fg=BEIGE, bd=1)
switch_translation_button.grid(column=1, row=2)

# latin alphabet &  Morse_code field and placing them on the grid
latin_alphabet_label = Label(text="Latin Alphabet", font=("Twentieth Century", 13, "normal"), fg=WHITE, bg=BLACK, pady=6)
latin_alphabet_label.grid(column=1, row=3)
translate_box = Entry(window, width=62)
translate_box.grid(column=1, row=4)

morse_code_Label = Label(text="Morse Code", font=("Twentieth Century", 12, "normal"), fg=GREEN, bg=BLACK, pady=6)
morse_code_Label.grid(column=1, row=5)
translated_box = Text(window, width=47, height=3)
translated_box.grid(column=1, row=6)

# Translate button
translate_button = Button(text="Translate", font=("Twentieth Century", 10, "bold"), command=translate, width=47, bg=BLACK, fg=BEIGE, bd=1)
translate_button.grid(column=1, row=7, pady=6)

# keeps window running
window.mainloop()
