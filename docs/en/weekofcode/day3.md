# Calculator
Authors: Yuvaansh Kapila
## Overview
Concepts Taught: Introduction to BhashaX, creating numeric input fields, and basic arithmetic operations.
Project: Create a simple calculator app that allows users to input numbers and perform addition and subtraction.
## Learning plan:
Start by setting up your project on the BhashaX website.
Create a new page and add a title.
Use the @number function to create numeric input fields.
Use the @button function to create buttons for addition and subtraction.
Display the result of the arithmetic operations.
## Code:
```
@app("Calculator App", "Created by Your Name", "#fffcfc", "#FFE6E6")
@displayH3("heading_1", "Please enter number 1")
$number1 = @number("id_number_1", 100)

@displayH3("heading_2", "Please enter number 2")
$number2 = @number("id_number_2", 100)

@displayH3("heading_3", "Please enter number 3")
$number3 = $number1 + $number2

@displayH3("heading_4", "Total: ")
@displayH3("heading_5", $number3)
```

## Challenge:
Making the Calculator Subtract
Start by setting up your project on the BhashaX website.
Create a new page and add a title.
Use the @number function to create numeric input fields.
Use the @button function to create a button for subtraction.
Display the result of the subtraction operation.
@app("Calculator App", "Created by Krish Yadav", "#fffcfc", "#FFE6E6")
@displayH3("heading_1", "Please enter number 1")
$number1 = @number("id_number_1", 100)

@displayH3("heading_2", "Please enter number 2")
$number2 = @number("id_number_2", 100)

@displayH3("heading_3", "Please enter number 3")
$number3 = $number1 - $number2

@displayH3("heading_4", "Total: ")
@displayH3("heading_5", $number3)
