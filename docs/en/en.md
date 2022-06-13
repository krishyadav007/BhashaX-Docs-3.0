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
### Running a code
1. Click on the green button with "Run", written on it.
2. Output will be visible in the output section.

### Clearing the output
1. Click on the blue button with "Clear" written on it.
2. All the output will get cleared.

## Delete the code
You need to select all the code, and then delete it.

# Tutorials
### Hello world
Lets get started by the very basics. We need the computer to say "Hello world". For this we would need to write
```
@display("Hello world");
```
### Comment
Comments in Python

Thus anything written after `//` will be considered comment for example.
```
@display("Hello world"); // This line will print hello world
```
### String
Text is called in the programming terminology is called as string.

#### How do we write it
To write strings we write whatever text I want inside single `'` or double qoutes `"`.
For example
```
"My name is Allen"

'My name is Ram'
```

### Variables
Variables are like boxes. They store whatever you put in them. You can add or remove whatever you added in it or even delete/destroy that box.

Now there can be as many boxes as possible. How will we diffentiate them? For this at home we add labels to box. Since variables are largely boxes, we need to name them too.

For example
```
$food = "Milk"
```
Here `$food` is the name of variable. Whenever we want to write a name of variable. Then

### Getting input
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
### Operations
There are many opreations which we can do.
#### Arithmetic
##### Addition
```
15 + 10
```

##### Subtraction
```
15 - 10
```

##### Multiplication
```
15 * 10
```

##### Divison
```
15 / 10
```
#### Relational
##### Equal to
It is used to compare 2 values, we use Equal to opreaor. It is denoted by `==` two equal symbols one after other without space. If the value on Left hand side and right hand side are equal, it shall result as true or else it will return false.
```
@display(10 == 10) // Will print True
@display(15 == 10) // Will print False

$number1 = 5*2
@display(number1 == 10) // Will print True
```
##### Is greater
```
15 > 10
```
##### Is lesser
```
15 < 10
```
##### Is not equal
```
15 != 10
```
##### Is greater than or equal to
```
15 >= 10
```
##### Is lesser than or equal to
```
15 <= 10
```

### If-else
Joe is a 4 year old boy. If today it rains, then he will stay inside home and play ludo, or else he will go out side and play cricket. Here based on the environment, Joe decides the outcome of what to do.

Many time when we code, we also need to chose the outcome of what we have to do based on the situation/condition. Thus we use If else.

```
$number_of_chocolates = 20
if( number_of_chocolates == 20 ) {
  @display("You have 20 Chocolates");
}
```
### Loops
Some times when we do things wrong, teacher gives us the punishment to write the same word 10 or 100 times. Imagine now you have to write the same sentence in computer. One way you can do is, copy and paste the same message again and again.
```
EG
```
Or use loops
### Arrays
Consider Array as train. You have engine, and then bogies after the engine. You can keep adding as boggies you want. Then you can also remove some bogies. People can come and go out of a bogie and so on.

Array is a special variable, which can hold more than one value:



### Functions
Function is a block of code designed to perform a particular task.

# Errors

# Sample code
### Calculator
```
$number1 = @input("Please tell the first number1")
$number2 = @input("Please tell the first number2")

$sum = $number1 + $number2

@display(“The sum is : ”)
@display($sum)
// THIS IS BY ME
```
