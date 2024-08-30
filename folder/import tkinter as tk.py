import tkinter as tk
from tkinter import scrolledtext

class RealTimeEditor:
    def __init__(self,root):
        self.root=root
        self.root.title("Real-Time Text Editor")
        self.text_area=scrolledtext.ScrolledText(root,wrap=tk.WORD,undo=True)
        self.text_area.pack(expand=True,fill="both")
        self.text_area.bind("<KeyRelease>",self.on_text_change)
    def on_text_change(self,event):
        current_text=self.text_area.get("1.0",tk.END)
        print("Text changed:/n",current_text)
if __name__=="__main__":
  root=tk.Tk()
  app=RealTimeEditor(root)
  root.mainloop()