# IF/Else Usage
Author: Yuvaansh Kapila
## Overview
* **Concepts Taught**: Introduction to BhashaX, using variables, getting input, and using if-else statements.
* **Project**: Create a simple app that asks the user for their age and displays a message based on the input.
* **Other Details**: This project will help you understand the basics of BhashaX and how to use variables, input, and if-else statements to create a simple interactive app.

## Learning plan:
Start by setting up your project on the BhashaX website.
Create a new page and add a title.
Use variables to store user input.
Use the @input function to get user input.
Use if-else statements to display different messages based on the input.
## Code
```
@app("Age Checker", "Developer Name", "#f0f0f0", "#333333")

// Display a welcome message
@displayH1("mainHeading", "Age Checker")

// Get user input for age
$age = parseInt(@input("Please enter your age"))

// Use if-else statements to display a message based on the age
if ($age < 18) {
  @displayH2("You are a minor.")
} else if ($age >= 18 && $age < 65) {
  @displayH3("You are an adult.")
} else {
  @displayH4("You are a senior.")
}
```

## Challenge:
Start by setting up your project on the BhashaX website.
Create a new page and add a title.
Use variables to store user input.
Use the @input function to get user input.
Use if-else statements to display different messages based on the input.
```
@app("Age Checker", "Developer Name", "#f0f0f0", "#333333")

// Display a welcome message
@displayH1("mainHeading", "Age Checker")

// Get user input for name
$name = @displayH2("Please enter your name")

// Get user input for age
$age = parseInt(@input("Please enter your age"))

// Use if-else statements to display a message based on the age
if ($age < 18) {
  @display("Hello, " + $name + "! You are a minor.")
} else if ($age >= 18 && $age < 65) {
  @display("Hello, " + $name + "! You are an adult.")
} else {
  @display("Hello, " + $name + "! You are a senior.")
}
```
