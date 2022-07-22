# Welcome to BhashaJS in English 

# Usage

## How to register
### On laptop 
1. Click on register present on the top left corner of the website.
2. It will open a new page with a form in it.
3. Fill your real full name in the first blank.
4. Fill email address in the second blank. If you don't have your own email address or are underage put your parents email address.
5. Put password for your account.
6. Re type the same password from the step to confirm the creation of account.
7. Then click on the blue colored "Register" button.

### On mobile
1. Click on hamburger/ menu icon present on the top left corner of the website.
2. It will open a list of text, click on register.
3. It will open a new page with a form in it.
4. Fill your real full name in the first blank.
5. Fill email address in the second blank. If you don't have your own email address or are underage put your parents email address.
6. Put password for your account.
7. Re type the same password from the step to confirm the creation of account.
8. Then click on the blue colored "Register" button.

## How to login
# Interface
## Running a code
1. Click on the green button with "Run", written on it.
2. Output will be visible in the output section.

## Clearing the output
1. Click on the blue button with "Clear" written on it.
2. All the output will get cleared.

## Delete the code
You need to select all the code, and then delete it.

# Tutorials
## Hello world
Lets get started by the very basics. We need the computer to say "Hello world". For this we would need to write
```
@display("Hello world");
```
## Comment
Comments in BhashaX

Thus anything written after `//` will be considered comment for example.
```
@display("Hello world"); // This line will print hello world
```
Comments are useful to have explanatory information for the code.

## String
Text is called in the programming terminology is called as string.

### How do we write it
To write strings we write whatever text I want inside single `'` or double qoutes `"`.
For example
```
"My name is Allen"

'My name is Ram'
```

## Variables
Variables are like boxes. They store whatever you put in them. You can add or remove whatever you added in it or even delete/destroy that box.

Now there can be as many boxes as possible. How will we diffentiate them? For this at home we add labels to box. Since variables are largely boxes, we need to name them too.

For example :-
```
$food = "Milk"
```
Here `$food` is the name of variable. Whenever we want to write a name of variable. 

## Getting input
To get the input from user we use 
```
@input("Please tell your input")
```

If you want to store the value of input in some variable then you can do so by

```
$input = @input("Please tell your input")
$name = @input("Please tell your name")
```

But wait how will computer distguish whether the input you want to pass is `"4"` or `4`, i.e is it a text or a number. All the input you pass to computer by defualt is considered as number. We need to change them

## Operations
There are many opreations which we can do.
### Arithmetic
#### Addition
```
15 + 10
```

#### Subtraction
```
15 - 10
```

#### Multiplication
```
15 * 10
```

#### Divison
```
15 / 10
```

#### Modulus
Modulus is finding the remainder of the division.
```
15 % 10  // This will give you the remainder of the division, 15 / 10 has remainder of 5.
```
### Relational
#### Equal to
It is used to compare 2 values, we use Equal to opreaor. It is denoted by `==` two equal symbols one after other without space. If the value on Left hand side and right hand side are equal, it shall result as true or else it will return false.
```
@display(10 == 10) // Will print True
@display(15 == 10) // Will print False

$number1 = 5*2
@display(number1 == 10) // Will print True
```
#### Is greater
Is greater than symbol is if anything is greater than something or not.
```
15 > 10
```
#### Is lesser
Is lesser than symbol is if anything is lesser than something or not.
```
15 < 10
```
#### Is not equal
Checks if the value on left hand side is not equal to the value on right hand side.
```
15 != 10
```
#### Is greater than or equal to
The Is greater than or equal to symbol is if anything is greater than or equal to something or not.
```
15 >= 10
```
#### Is lesser than or equal to
The Is lesser than or equal to symbol is if anything is lesser than or equal to something or not.
```
15 <= 10
```
### Assignment Operator
The assignment operators are used to assign variables a value or result of an expression.
```
// Syntax:
$variable_name = "value";
$my_number = 3.14159;
```
`=` is one of the assingment operators.
#### Shorthand assignment operators
Say for example to add `1` to `$my_number` we can use the following
```
$my_number = $my_number + 1;
```
here we are refrencing `$my_number` 2 times, this can be made shorter by using the shorthand assignment operators.
```
$my_number += 1;
```
the `+=`, `-=`, `*=`, `/=`, `%=` are all shorthand assignment operators.

### Increment/Decrement Operators
Increment and decrement operators are used to increment or decrement the value of a variable, by 1 unit.

Example :-
```
$my_number++;
```

<!-- Add Logical, Bitwise operators -->

### If-else
Joe is a 4 year old boy. If today it rains, then he will stay inside home and play ludo, or else he will go out side and play cricket. Here based on the environment, Joe decides the outcome of what to do.

Many time when we code, we also need to chose the outcome of what we have to do based on the situation/condition. Thus we use If else.

```
$number_of_chocolates = 20
if( number_of_chocolates == 20 ) {
  @display("You have 20 Chocolates");
}
else {
  @display("You have 20 Chocolates");
}
```

The else block is optional, it can be omitted if we don't want to write anything in else block.

#### Multiple conditions
If we want to check multiple conditions, we can use the `else if` ladder. The Else if ladder is used to check multiple conditions.
For example you wanted to check if the number of chocolates is less than 10, if it is less than 10, then you want to say "You have less than 10 chocolates, we need more chocolate!", otherwise you want to check if you have less than 50 chocolate, then you want to say "You have enough chocolates", otherwise you want to say "You have more than 50 chocolates, that's a lot of chocolate! dont forget to share".

```js
$number_of_chocolates = parseInt(@input("Please tell the number of chocolates"));
// the parseInt function is used to convert the string to integer.

if ($number_of_chocolates < 10) {
  @display("You have less than 10 chocolates, we need more chocolate!");
}
else if ($number_of_chocolates < 50) {
  @display("You have enough chocolates");
}
else {
  @display("You have more than 50 chocolates, that's a lot of chocolate! dont forget to share");
}
```
First the `$number_of_chocolates < 10` will be checked, if it is true, then the `@display("You have less than 10 chocolates, we need more chocolate!")` will be executed. If it is false, then the `$number_of_chocolates < 50` will be checked, if it is true, then the `@display("You have enough chocolates")` will be executed. If it is false, then the `@display("You have more than 50 chocolates, that's a lot of chocolate! dont forget to share")` will be executed.

### Loops
Some times when we do things wrong, teacher gives us the punishment to write the same word 10 or 100 times. Imagine now you have to write the same sentence in computer. One way you can do is, copy and paste the same message again and again.
```
EG
```
Or use loops
### Arrays
Consider Array as train. You have engine, and then bogies after the engine. You can keep adding as boggies you want. Then you can also remove some bogies. People can come and go out of a bogie and so on.

Array is a special variable, which can hold more than one value:

```
arr = [0,0,0,"heesh"]
```

### Functions
Function is a block of code designed to perform a particular task.

# Errors

# Sample code
## Calculator
```js
$number1 = parseInt(@input("Please tell the first number1"));
$number2 = parseInt(@input("Please tell the first number2"));

$sum = $number1 + $number2;

@display(“The sum is : ”);
@display($sum);
// THIS IS BY ME
```
