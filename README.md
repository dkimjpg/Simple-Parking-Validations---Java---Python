# About this app:
This is just a simple app I made to handle giving out parking validation codes. I don't intend to use it for any commercial purposes, 
it's just something I coded up in about half an hour during some off time during work. Boredom will do that to you.

Anyway, it's meant to address some of the most common requests at the front desk of an office's main lobby. It's still in development as 
of this writing (which would be 1/13/2025, and if I decide to update this further, I'll probably leave some updates near the bottom) and
I plan on improving it with a more modern but simplistic design as I work on this. If for some reason you decide to use this for your
own parking validation code system, you're putting a lot of sensitive employee data at risk. This is just a personal project, nothing
special.

For the JavaScript version of this app, click here: [https://github.com/dkimjpg/Simple-Parking-Validations](https://github.com/dkimjpg/Simple-Parking-Validations)

# How parking validation code distribution works:
When an employee enters their name and alias information into the designated areas, a preexisting csv file with the parking validation codes 
will be checked to see what the next available code is and it will put that code along with the date and the employee's name and alias onto a csv file
that is intended to hold used parking validation codes. Then it will display that code on the website by redirecting the employee to the 
parking code webpage with their code on it. The important part about the parking codes is that they need to already be in the same folder as
this application, and when the codes run out, new codes need to be added. Plus, the csv file with all the used codes may also need to be updated
depending on specific usage.

For those of you who don't know what a csv file is, it's a basic spreadsheet file where columns are separated by commas, and rows are separated
line by line.

UPDATE (1/28/2025): This project now uses Excel files (.xlsx) instead of CSV files (.csv) for spreadsheets, to make it more convenient for users.

# Features
- Offers parking validation codes to employees
- Handles a few other potential requests that a front desk might get from employees and visitors

# To-Do
- [ ] Implement Python version  
  - [x] GUI
  - [ ] Read operation
  - [x] Write operation
- [ ] Implement Java version
  - [ ] GUI
  - [ ] Read operation
  - [ ] Write operation
