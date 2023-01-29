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
from PIL import ImageTk, Image
from fontTools import ttLib
import time

ttfFile = ttLib.TTFont("/Users/imody/Desktop/qwerHacks/health-forms-for-all/examples/pymupdf-example/gagaFont.ttf")
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
    fileLabel.grid_remove();
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PDF files",
                                                        "*.pdf"),
                                                       ("all files",
                                                        "*.*")))
    print("completed dialog")
    # Change label contents
    # fileLabel.configure(text="File successfully scanned! Please check your Downloads Folder")
    fileLabel.grid(column = 0, row = 6)
    fileLabel["text"]="file success updated"
    # v1 = pdf.ShowPdf()
    # v2 = v1.pdf_view(window, pdf_location = filename)
    if(filename != ""):
        print("run script")
        print(filename)
        newName = filename[:-4] + '_modified.pdf'
        print("path home --> ", Path.home())
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
window.geometry("900x800")

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
                            font= ('BORN THIS WAY', 20),
                            background="white", justify="center",
                            )
fileLabel = ttk.Label(window, text = "",  font=('Helvetica', 22, 'bold'),
                            background="white", justify="center", )
fileLabel.grid(column = 0, row = 6)
      
button_explore = ttk.Button(window,
                        text = "Browse Files",
                        command = browseFiles, style='TButton'
                        )
  
# button_exit = ttk.Button(window,
#                      text = "Exit",
#                      command = exit, )
  
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
notebook.add(frame3, text='Additional Steps')
notebook.add(frame4, text='Resources')

# label_file_explorer.grid(column = 1, row = 0)

Description.grid(column = 0, row = 2)

aboutSection = ttk.Label(frame1, 
          text ="About Section \n\nFirst, select the file you would like to scan using the 'Browse File'. \nThe file you have selected will be scanned and annotated by our program. \nThe modified file will be automatically be stored in your Downloads folder.\n").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  
issueSection = ttk.Label(frame2, 
          text ="The Issue \n\nThe LGBTQ+ population is at disproportionate risk for numerous medical \nrisks including chronic diseases such as asthma, diabetes, and heart disease; \nmental health conditions; and substance abuse. At the same time, they have \nlower rates of healthcare access and utilization. This may be attributed to \nfear of discrimination from healthcare providers and the stigmas \nsurrounding the LGBTQ+ community in the medical setting.\n\nFor many, microaggressions begin even before meeting with the physician. \nPatient intake forms being used in modern clinical practice use \noutdated and non inclusive terms that prevent medical practitioners \nfrom gathering important patient information and can make patients \nhesitant to share personal information. Historically, this has led to \nworse outcomes for patients of sexual and gender minority.\n\nAdopting inclusive medical practices at all levels will promote feelings of security \nand acceptance for members of the LGBTQ+ community, foster stronger \npatient-physician relationships, and improve overall quality and continuity of care. \nOur application serves as a tool to aid the implementation of inclusive language \nand educate on the importance of this language in the medical setting.\n").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  
backgroundSection = ttk.Label(frame3, 
          text ="Additional Steps\n\n-   Making sure team (doctors/nurses/secretary) are trained\n\n-   Provide an inclusive waiting room environment (images/pamphlets/etc…)\n\n-   Respecting a patient’s chosen name and pronouns\n").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  
resourcesSection = ttk.Label(frame4, 
          text ="Resources\n\nNational LGBTQIA+ Health Education: http://www.lgbthealtheducation.org/\n\nCreating an inclusive environment for LGBT patients: \nhttps://lgbtqiahealtheducation.org/wp-content/uploads/2017/08/Forms-and-Policy-Brief.pdf\n\nWorld Professional Association for Transgender Health: \nhttp://wpath.org/\n\nTrevor Project:\n https://www.thetrevorproject.org/ \n").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)
image1 = Image.open(os.getcwd() + "/logo-dark.png")
img = image1.resize((178,100))
test = ImageTk.PhotoImage(img)

image2 = Image.open(os.getcwd() + "/title-bright.png")
img2_height = 70
img2 = image2.resize((img2_height*6,img2_height))
gagaTest = ImageTk.PhotoImage(img2)

resourcesSection = ttk.Label(window, 
          image=test).grid(column = 0, 
                               row = 0,
                               padx = 0,
                               pady = 5,
                               columnspan=2)
gagaImage = ttk.Label(window, 
          image=gagaTest).grid(column = 0, 
                               row = 1,
                               padx = 0,
                               pady = 5,
                               columnspan=2)
# National LGBTQIA+ Health Education:

  
button_explore.grid(column = 0, row = 4)
  
# button_exit.grid(column = 1,row = 4)
  
# Let the window wait for any events

window.mainloop()
