import tkinter as tk

def main_page(root):
    page = tk.Frame(root)
    page.grid(sticky="nsew")

    for i in range(4):  # Configure all 4 columns
        page.grid_columnconfigure(i, weight=1)
    #page.grid_rowconfigure(0, weight=1)  # Give weight to rows
    #page.grid_rowconfigure(1, weight=1)

    tk.Label(page, text="This is the main page").grid(row=0, column=1, columnspan=2, pady=20)
    tk.Button(page, text="Parking Validation", justify="left", padx=10, pady=5, command=change_page).grid(row=1, column=1, sticky="nsew", padx=10)
    tk.Button(page, text="Temporary Badge", padx=10, pady=5).grid(row=1, column=2, sticky="nsew", padx=10)
    
    

def parking_validation(root):
    page = tk.Frame(root)
    page.grid(padx=40, pady=40)
    tk.Label(page, text="Parking Validation done here").grid(row=0)
    tk.Button(page, text="Back to main page", justify="left", padx=10, pady=5, command=change_page).grid(row=1)

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
        
def center_window(window, width=400, height=400):
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate center position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # Set window size and position
    window.geometry(f"{width}x{height}+{x}+{y}")

def button_clicked():
    print("button clicked!")

root = tk.Tk()
root.title("Parking Validations")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

center_window(root)
#root.geometry("400x400")
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