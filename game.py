import tkinter as tk

mytk = tk.Tk()
mytk.geometry("500x500")

def createCanvas(root):
    canvas = tk.Canvas(root, height=100, width=100,bg="white")
    return canvas

def createDot(event):
        m = event.x - 2
        n = event.y - 2
        o = event.x + 2 
        p = event.y + 2
        canvas.create_oval(m, n, o, p, fill="black",width=0)

def clearCanvas(canvas):
    canvas.delete("all")

canvas = createCanvas(mytk)
canvas.bind("<Button-1>", createDot)
canvas.bind("<B1-Motion>", createDot)
canvas.bind("<ButtonRelease-1>", createDot)    
canvas.grid(row=0,column=0)


button1 = tk.Button(mytk, text="clear", command = lambda : clearCanvas(canvas))
button1.grid(row=0,column=1)

mytk.mainloop()