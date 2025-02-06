import tkinter as tk

def main_page(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text="This is the main page").grid(row=0)
    tk.Button(page, text="Parking Validation", command=change_page).grid(row=1)

def parking_validation(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text="Parking Validation done here").grid(row=0)
    tk.Button(page, text="Back to main page", command=change_page).grid(row=1)

def change_page():
    global page_num, root
    for widget in root.winfo_children():
        widget.destroy()
    if page_num == 1:
        parking_validation(root)
        page_num = 2
    else:
        main_page(root)
        page_num = 1

page_num = 1
        

def button_clicked():
    print("button clicked!")

root = tk.Tk()
main_page(root)

"""
button = tk.Button(
    root,
    text="click me",
    command=button_clicked,
    activebackground="blue",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=10,
    pady=5,
    width=15,
    wraplength=100
    )

button.pack(padx=20, pady=20)
"""
root.mainloop()

def main():
    return