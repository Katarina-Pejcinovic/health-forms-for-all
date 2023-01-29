# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
import tkinter as tk
  
# import filedialog module
from tkinter import filedialog
import tkinter.ttk as ttk
import fitz, os
from script import *
from pathlib import Path



class Checkbar(Frame):
    def __init__(self, parent=None, picks={}, side=LEFT, anchor=W, list_keys=[]):
        Frame.__init__(self, parent)
        self.vars = []
        maxwidth = len(max(list_keys, key=len))

        for key, value in picks.items():
            var = IntVar()
            chk = Checkbutton(self, text=key, variable=var, width=maxwidth, anchor='w')
            # button_ttp = ToolTip(chk, value)
            chk.pack(side=side, anchor=anchor, expand=YES, )


list_keys = ['Healthcare', 'Government', 'Research', 'Marketing']
# from tkPDFViewer import tkPDFViewer as pdf
  
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PDF files",
                                                        "*.pdf"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    fileLabel.configure(text="File Opened: "+filename)
    # v1 = pdf.ShowPdf()
    # v2 = v1.pdf_view(window, pdf_location = filename)
    if(filename != ""):
        print("run script")
        print(filename)
        newName = filename[:-4] + '_modified.pdf'
        downloads_path = str(Path.home() / "Downloads")
        newName = downloads_path + '/' + os.path.basename(newName)
        
        print('try --> ', newName)
        lint_pdf(filename, newName)



                                                                                                  
# Create the root window
window = Tk()
# style = Tk.Style(window)
# style.theme_use('aqua')
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("800x600")

#Set window background color
window.config()



Description = ttk.Label(window,
                            text = "Form This Way is a PDF scanner and annotating tool, designed to help companies and providers patient intake forms' inclusivity",
                            font=('Helvetica', 12, 'italic'),
                            background="white", justify='left'
                            )
# Create a File Explorer label
label_file_explorer = ttk.Label(window,
                            text = "Form This Way",
                            font=('Helvetica', 18, 'bold'),
                            background="white", justify="center",
                            )
fileLabel = ttk.Label(window, text = "",  font=('Helvetica', 12, 'bold'),
                            background="white", justify="center", )
fileLabel.grid(column = 0, row = 6)
      
button_explore = ttk.Button(window,
                        text = "Browse Files",
                        command = browseFiles, style='TButton'
                        )
  
button_exit = ttk.Button(window,
                     text = "Exit",
                     command = exit, )
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

# create a notebook
notebook = ttk.Notebook(window)
notebook.grid(column=0, row=5)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook, width=400, height=280)
frame4 = ttk.Frame(notebook, width=400, height=280)

frame1.grid(column=1, row=6)
frame2.grid(column=1, row=6)
frame3.grid(column=1, row=6)
frame4.grid(column=1, row=6)

# add frames to notebook


Checkbar(window, picks={k: k for k in list_keys[:4]}, list_keys=list_keys).grid(row=3, column=0, sticky='w', padx=200)
notebook.add(frame1, text='About')
notebook.add(frame2, text='Issue')
notebook.add(frame3, text='Background')
notebook.add(frame4, text='Resources')

label_file_explorer.grid(column = 0, row = 0)

Description.grid(column = 0, row = 1)

aboutSection = ttk.Label(frame1, 
          text ="About Section \n\nFirst, select the file you would like to scan using the 'Browse File'. \nThe file you have selected will be scanned and annotated by our program. \nThe modified file will be automatically be stored in your Downloads folder.\n").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  


  
button_explore.grid(column = 0, row = 4)
  
# button_exit.grid(column = 1,row = 4)
  
# Let the window wait for any events

window.mainloop()
