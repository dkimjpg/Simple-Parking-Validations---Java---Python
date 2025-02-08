import tkinter as tk
import pandas as pd
from pathlib import Path
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1) #disables high dpi upscaling, which caused blurry text

def main_page(root): #home page
    page = tk.Frame(root)
    #page.grid(sticky="nsew")
    page.grid(padx=40, pady=40)

    #for i in range(4):  # Configure all 4 columns
        #page.grid_columnconfigure(i, weight=1)
    #page.grid_rowconfigure(0, weight=1)  # Give weight to rows
    #page.grid_rowconfigure(1, weight=1)

    welcome_label = tk.Label(page, text="Welcome!", font=("Segoe UI", 28, "bold")).grid(row=0, column=1, columnspan=2)
    option_label = tk.Label(page, text="Please select an option below.", font=("Segoe UI", 12, "bold")).grid(row=1, column=1, columnspan=2, pady=20)
    parking_val = tk.Button(page, text="Parking Validation", justify="left", padx=10, pady=5, command=validation_entry).grid(row=2, column=1, sticky="nsew", padx=10)
    temp_badge = tk.Button(page, text="Temporary Badge", padx=10, pady=5).grid(row=2, column=2, sticky="nsew", padx=10)
    
    

def parking_validation(root): #employee data entry
    page = tk.Frame(root)
    page.grid(padx=40, pady=40)
    entry_label = tk.Label(page, text="Please enter your Name and ID below.").grid(row=0, column=0, columnspan=2)
    name_label = tk.Label(page, text="Name").grid(row=1, column=0)    
    name_entry = tk.Entry(page).grid(row=1, column=1)
    id_name = tk.Label(page, text="ID").grid(row=2, column=0)
    id_entry = tk.Entry(page).grid(row=2, column=1)
    return_home = tk.Button(page, text="Cancel", padx=10, pady=5, command=home_return).grid(row=3, column=0)
    submit_data = tk.Button(page, text="Submit", padx=10, pady=5, command= lambda: parking_submit(name_entry.get(), id_entry.get())).grid(row=3, column=1, sticky="e")
    prepaid_code = tk.Button(page, text="I have a prepaid code", padx=10, pady=5).grid(row=4, column=0, columnspan=2)



def prepaid_code(root): #guest data entry with prepaid codes
    page = tk.Frame(root)



def validation_code(root): #provides validation code
    page = tk.Frame(root)
    page.grid(padx=40, pady=40)
    success_label = tk.Label(page, text="Your code!").grid(row=0)
    code = tk.Label(page, text="insert code here").grid(row=1)
    validation_tutorial = tk.Button(page, text="Learn more about how to use a Parking Validation Code", padx=10, pady=5).grid(row=2)
    return_home = tk.Button(page, text="Return to Start", padx=10, pady=5, command=home_return).grid(row=3)
    parking_val = tk.Button(page, text="Code not working? Get a new one here.", padx=10, pady=5, command=validation_entry).grid(row=4)



"""
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
"""

def home_return():
    for widget in root.winfo_children():
        widget.destroy()
    main_page(root)

def validation_entry():
    for widget in root.winfo_children():
        widget.destroy()
    parking_validation(root)

def prepaid_entry():
    for widget in root.winfo_children():
        widget.destroy()
    prepaid_code(root)

def parking_submit(name, id):
    for widget in root.winfo_children():
        widget.destroy()
    data = {
        'date':[pd.Timestamp.today().strftime("%m/%d/%Y")],
        'ID':[id],
        'Name':[name]
    }
    df = pd.DataFrame(data) #creates data frame from above data
    df.to_csv('/employee_logs/parkingDataTest1.xlsx', mode='a', index=False, header=False)
    validation_code(root)

def prepaid_submit():
    for widget in root.winfo_children():
        widget.destroy()
    validation_code(root)

#page_num = 1
        
def center_window(window, width=1000, height=720):
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate center position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # Set window size and position
    window.geometry(f"{width}x{height}+{x}+{y}")

#def button_clicked():
    #print("button clicked!")

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