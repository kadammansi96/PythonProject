import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_Label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_Label["text"] = "New text"
my_Label.config(text="New text")
my_Label.pack()

# Button

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_Label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_click)
button.pack()


# Entry

input = tkinter.Entry(width=10)
print(input.get())
input.pack()




class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)











window.mainloop()