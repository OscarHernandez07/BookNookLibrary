import tkinter as tk

root = tk.Tk()
w = root.winfo_height
root.geometry("1000x1000+1100+1000")

lab1 = tk.Label(root,
  text="Book Nook Library",
  font="Arial 20")
lab1.pack()

frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="This is the best Library in the nation.")
label_a.pack()
frame_a.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    fg="black",
)
button.pack()

entry = tk.Entry(fg="black", width=50)
entry.pack()



root.mainloop()
                 
#print a message welcoming the user to the library
  
print("This is the Book Nook Library.")
print(" ")
  
bag = []
  #check how what books you have
def check():
  print("Books available.")
  print(bag) 
  if len(bag) == 1:
    print("There is " + str(len(bag)) + " book.")
    print(" ")
  #otherwise say "books"
  else:
    print("There are " + str(len(bag)) + " books.")
    print(" ")
#add a book
def add_book():
  newbook = input("What book are you adding?:")
  bag.append(newbook)
  print(newbook + " was added.")
  print(" ")
  


#remove a book
def remove_book():
  remove = input("What book are you removing?:")
  print(" ")
  bag.remove(remove)
  print(remove + " was removed.")
  print(" ")
#make a loop
while True:
  book = input("Would you like to add a book?(add), Would you like to remove a book?(remove), or Would you like to check what books are available?(check.) ").lower()
  print(" ")
  #see if anything was added, removed, or check list
  if book == "check":
    check()

  if book == "add":
    add_book()

  if book == "remove":
    remove_book()
