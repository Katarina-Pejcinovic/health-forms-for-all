# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
import tkinter.ttk as ttk
import fitz, os


# from tkPDFViewer import tkPDFViewer as pdf
  
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    # v1 = pdf.ShowPdf()
    # v2 = v1.pdf_view(window, pdf_location = filename)
    if(filename != ""):
        print("run script")
        # os.system('python3 script.py')

      
                                                                                                  
# Create the root window
window = Tk()
# style = Tk.Style(window)
# style.theme_use('aqua')
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("700x300")

#Set window background color
window.config()



Description = ttk.Label(window,
                            text = "Form This Way is a PDF scanner and annotating tool, designed to help companies and providers patient intake forms' inclusivity",
                            font=('Helvetica', 12, 'italic'),
                            background="white",
                            )
# Create a File Explorer label
label_file_explorer = ttk.Label(window,
                            text = "Form This Way",
                            font=('Helvetica', 18, 'bold'),
                            background="white", justify="center",
                            )
  
      
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

frame1.grid(column=1, row=6)
frame2.grid(column=2, row=6)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')

label_file_explorer.grid(column = 0, row = 0)

Description.grid(column = 0, row = 1)


  
button_explore.grid(column = 0, row = 4)
  
# button_exit.grid(column = 1,row = 4)
  
# Let the window wait for any events

window.mainloop()

# import PyPDF2
# from tkinter import *
# from tkinter import filedialog
# #Create an instance of tkinter frame
# win= Tk()
# #Set the Geometry
# win.geometry("750x450")
# #Create a Text Box
# text= Text(win,width= 80,height=30)
# text.pack(pady=20)
# #Define a function to clear the text
# def clear_text():
#    text.delete(1.0, END)
# #Define a function to open the pdf file
# def open_pdf():
#    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
#    if file:
#       #Open the PDF File
#       pdf_file= PyPDF2.PdfFileReader(file)
#       #Select a Page to read
#       page= pdf_file.getPage(0)
#       #Get the content of the Page
#       content=page.extractText()
#       #Add the content to TextBox
#       text.insert(1.0,content)

# #Define function to Quit the window
# def quit_app():
#    win.destroy()
# #Create a Menu
# my_menu= Menu(win)
# win.config(menu=my_menu)
# #Add dropdown to the Menus
# file_menu=Menu(my_menu,tearoff=False)
# my_menu.add_cascade(label="File",menu= file_menu)
# file_menu.add_command(label="Open",command=open_pdf)
# file_menu.add_command(label="Clear",command=clear_text)
# file_menu.add_command(label="Quit",command=quit_app)
# win.mainloop()