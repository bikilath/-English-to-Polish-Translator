# Name Bikila Hunde ID- N0 54101
# Python Programming Project
# Title: "Translation App: English to Polish Language Translator"
import tkinter as tk
from translate import Translator


def translate_text():
    # Get the text entered by the user
    text = entry.get()

    # Target language (Polish)
    target_language = "pl"

    # Create a translator instance
    translator = Translator(to_lang=target_language)

    # Translate the text
    translated_text = translator.translate(text)

    # Update the label with the translated text
    label.config(text=translated_text)


# Create the main window
window = tk.Tk()
window.title("English to Polish Translation App")

# Create and configure the entry widget
entry = tk.Entry(window, width=100)
entry.pack()

# Create the translate button
button = tk.Button(window, text="Translate", command=translate_text)
button.pack()

# Create and configure the label to display the translated text
label = tk.Label(window, text="")
label.pack()

# Create a label for submission
submission_label = tk.Label(window, text="Submitted by: Bikila Hunde")
submission_label.pack()

# Run the application
window.mainloop()

'''In this code, we import the necessary libraries, create a window using tkinter, and
define the translate_text function to handle the translation process. The function gets the text from 
the entry widget, performs the translation, and updates the label widget with the translated text.

The GUI elements such as the entry widget, translate button, and label are created and 
configured within the main window. The translate_text function is called when the translate button is clicked.'''


