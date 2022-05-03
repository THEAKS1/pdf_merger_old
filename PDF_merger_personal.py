from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import asksaveasfilename
import os, PyPDF2, webbrowser

class merge_pdf():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("700x440")
        self.win.title("PDF - Merger")
        self.win.configure(background = "#d8e8e6")
        self.pictures()
        self.win.iconphoto(False, self.photo)

        self.i = 0
        self.selected_path_list = []

        self.frames()
        self.widgets()

        self.win.mainloop()

    def pictures(self):
        self.insta = PhotoImage(file = "D:\\python3\\PDF_MERGER\\icons\\insta.png")
        self.gmail = PhotoImage(file = "D:\\python3\\PDF_MERGER\\icons\\gmail.png")
        self.fb = PhotoImage(file = "D:\\python3\\PDF_MERGER\\icons\\fb.png")
        self.photo = PhotoImage(file = "D:\\python3\\PDF_MERGER\\icons\\icon.png")

    def frames(self):
        self.selected_frame = LabelFrame(self.win, text = "Selected PDFs", font = ("times new roman", 15, ["italic", "bold"]), bg = "#d8e8e6", fg = "black", bd = 5)
        self.selected_frame.configure(width = 400, height = 330)
        self.selected_frame.place(x = 10, y = 10)

        self.pdf_frame = LabelFrame(self.win, text = "All PDFs", font = ("times new roman", 15, ["italic", "bold"]), bg = "#d8e8e6", fg = "black", bd = 5)
        self.pdf_frame.configure(width = 270, height = 330)
        self.pdf_frame.place(x = 430, y = 10)

    def widgets(self):

        self.scrollbar_all = Scrollbar(self.pdf_frame, orient = VERTICAL)
        self.scrollbar_all.grid(row = 0, column = 1, rowspan = 5, sticky = "ns")

        self.scrollbar_selected = Scrollbar(self.selected_frame, orient = VERTICAL)
        self.scrollbar_selected.grid(row = 0, column = 1, rowspan = 5, sticky = "ns")

        self.selected = Listbox(self.selected_frame, height = 20, width = 65, bg = "#d8e8e6", fg = "black", yscroll = self.scrollbar_selected.set)
        self.selected.config(height = 18)
        self.selected.grid(row = 0, column = 0, rowspan = 5)

        self.up = Button(self.win, text = "Up", command = self.moveup, width = 5, fg = "black", bg = "#d8e8e6", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.up.place(x = 5, y = 340)

        self.remove_button = Button(self.win, text = "Remove", command = self.remove, width = 6, bg = "#d8e8e6", fg = "#0a1b66", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.remove_button.place(x = 90, y = 340)

        self.merge_button = Button(self.win, text = "Merge", command = self.merging, width = 10, bg = "#d8e8e6", fg = "#256306", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.merge_button.place(x = 180, y = 340)

        self.down = Button(self.win, text = "Down", command = self.movedown, width = 10, bg = "#d8e8e6", fg = "#523737", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.down.place(x = 300, y = 340)

        self.clear_button = Button(self.win, text = "Clear", command = self.clear, width = 10, bg = "#d8e8e6", fg = "#ad1010", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.clear_button.place(x = 170, y = 395)

        self.load_button = Button(self.win, text = "Select directory", command = self.load_pdfs, bg = "#d8e8e6", border = 0, font = ("Lucida Calligraphy", 13, "bold"))
        self.load_button.place(x = 480, y = 340)

        self.all_pdfs = Listbox(self.pdf_frame, height = 20, width = 40, bg = "#d8e8e6", fg = "black", yscroll = self.scrollbar_all.set)
        self.all_pdfs.config(height = 18)
        self.all_pdfs.grid(row = 0, column = 0, rowspan = 5)

        self.credit = Label(self.win, text = "created by AKASH KUMAR SINGH", fg = "#ff1493", bg = "#d8e8e6")
        self.credit.place(x = 475, y = 370)

        self.insta_button = Button(self.win, image = self.insta, command = self.openinsta, width = 20, height = 20, border = 0)
        self.insta_button.place(x = 510, y = 405)

        self.fb_button = Button(self.win, image = self.fb, command = self.openfb, width = 20, height = 20, border = 0)
        self.fb_button.place(x = 560, y = 405)

        self.gmail_button = Button(self.win, image = self.gmail, command = self.opengmail, width = 20, height = 20, border = 0)
        self.gmail_button.place(x = 605, y = 405)

        self.scrollbar_all.config(command = self.all_pdfs.yview)
        self.scrollbar_selected.config(command = self.selected.yview)

    def load_pdfs(self):

        self.all_pdf_list = []
        self.directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(self.directory):
            for file in files:
                if os.path.splitext(file)[1] == ".pdf":
                    path = (root_ + "/" + file).replace("\\", "/")
                    self.all_pdf_list.append(path)

        for index, song in enumerate(self.all_pdf_list):
            self.all_pdfs.insert(index, os.path.basename(song))

        self.all_pdfs.bind("<Double-1>", self.index)

    def index(self, event = None):
        self.selected_pdfs()
        self.i += 1

    def selected_pdfs(self, event = None):
        self.current = self.all_pdfs.curselection()[0]

        self.selected.insert(self.i, os.path.basename(self.all_pdf_list[self.current]))
        self.selected_path_list.append(self.all_pdf_list[self.current])

    def moveup(self, event = None):
        try:
            curr = self.selected.curselection()[0]
            if curr > 0:
                text = self.selected.get(curr)
                self.selected.delete(curr)
                self.selected.insert(curr - 1, text)

                self.selected_path_list[curr], self.selected_path_list[curr - 1] = self.selected_path_list[curr - 1], self.selected_path_list[curr]
        except:
            pass

    def movedown(self, event = None):
        try:
            curr = self.selected.curselection()[0]
            if curr < len(self.selected_path_list) - 1:
                text = self.selected.get(curr)
                self.selected.delete(curr)
                self.selected.insert(curr + 1, text)

                self.selected_path_list[curr], self.selected_path_list[curr + 1] = self.selected_path_list[curr + 1], self.selected_path_list[curr]        
        except:
            pass

    def remove(self):
        try:
            curr = self.selected.curselection()[0]
            self.selected.delete(curr)
            del self.selected_path_list[curr]
        except:
            pass

    def clear(self):
        self.selected.delete(0, END)
        self.selected_path_list = []
        self.index = 0

    def openfb(self):
        webbrowser.open_new(r"https://www.facebook.com/akashkumarsingh17272888/")

    def openinsta(self):
        webbrowser.open_new(r"https://www.instagram.com/pythonfriendly/")

    def opengmail(self):
        messagebox.showinfo("e-mail ME AT", "Email at: akashkumar8462@gmail.com")

    def merging(self):

        if self.selected_path_list:
                
            output_file = asksaveasfilename(initialfile = "Untitled.pdf", defaultextension = ".pdf", filetypes = [("PDF", "*.pdf")])
            
            if output_file: 

                pdfmerger = PyPDF2.PdfFileMerger()

                #loop through all PDFs
                for file in self.selected_path_list:
                    pdfmerger.append(PyPDF2.PdfFileReader(open(file, "rb")))
                
                pdfmerger.write(output_file)

                messagebox.showinfo("SUCCESS", "PDFs were successfully merged. Please visit the destination directory.")
        
        else:
            messagebox.showwarning("FILE NOT SELECTED", "Please select atleast one file.")


merge_pdf()