## Creating the Application ( @app )
The @app function initializes your application. It defines the title, developer details, and the default colors for the background and foreground.

### Parameters:
title (String): The title of the application window.
developer (String): The name of the developer or organization.
backgroundColor (String): Background color in hexadecimal format (e.g., #ffffff for white).
foregroundColor (String): Foreground color in hexadecimal format (e.g., #000000 for black).
### Example:
```
@app(title: "My App", developer: "Developer Name", backgroundColor: "#f0f0f0", foregroundColor: "#333333")
```



## Displaying Images
@image
The @image function adds an image to your application. You can control its dimensions and specify its source.

### Parameters:
1. id (String): A unique identifier for the image.
2. url (String): The URL or path to the image.
3. width (Integer): The width of the image in pixels.
4. height (Integer): The height of the image in pixels.
## Example:
```
@image("logo", url: "https://example.com/logo.png", width: 200, height: 100)
```


## Creating Headings
@displayH1 to @displayH6
These functions create headings with varying levels of importance, from @displayH1 (largest) to @displayH6 (smallest).

### Parameters:
1. id (String): A unique identifier for the heading.
2. text (String): The content of the heading.
### Example:
```
@displayH1("mainHeading", text: "Welcome to BhashaX!")
```


## Interactive Buttons ( @button )
The @button function adds a clickable button to your application. Buttons can trigger specific actions when clicked.

### Parameters:
1. id (String): A unique identifier for the button.
2. label (String): The text displayed on the button.
### Example:
```
@button("submitBtn", "Submit")
```


## Checkbox Inputs ( @checkbox )
The @checkbox function creates a checkbox input element, which allows users to select or deselect an option.

### Parameters:
1. id (String): A unique identifier for the checkbox.
2. label (String): Text displayed next to the checkbox.
### Example:
```
@checkbox("acceptTerms", "I agree to the terms and conditions")
```


## Color Attribute ( @color )
The @color function sets a color for a specific GUI element.

### Parameters:
1. id (String): The identifier of the element.
2. color (String): The color value in hexadecimal format.
### Example:
```
@color("mainHeading", "#ff4500")
```


## Date Input ( @date )
The @date function creates an input field for selecting dates.

### Parameters:
1. id (String): A unique identifier for the date input.
2. label (String): Label text displayed for the input field.
### Example:
```
@date("dob", "Select your birth date")
```


## Date-Time Input ( @datetime_local )
This function creates an input field for selecting both a date and time.

### Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
### Example:
```
@datetime_local("eventTime", "Event Date & Time")
```


## Email Input ( @email )
The @email function generates a text field for email address input.

### Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
### Example:
```
@email("userEmail", "Enter your email")
```


## Number Input ( @number )
This function creates an input field for numeric values.

### Parameters:
1. id (String): A unique identifier for the input field.
2. defaultValue (Number): The prefilled value in the input field.
### Example:
```
@number("quantity", 1)
```


## Telephone Input ( @tel )
The @tel function generates an input field for telephone numbers.

### Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
### Example:
```
@tel("phone", "Enter your phone number")
```


## Password Input ( @password )
This function creates an input field for password input, which obscures the text entered by the user.

### Parameters:
1. id (String): A unique identifier for the input field.
2. defaultValue (String): The prefilled value in the input field.
### Example:
```
@password("userPassword", "")
```


## Dropdown Select Menu ( @select )
The @select function generates a dropdown menu with a list of selectable options.

### Parameters:
1. id (String): A unique identifier for the dropdown menu.
2. options (Array of Strings): An array of strings representing the dropdown options.
### Example:
```
@select("colorPicker", ["Red", "Green", "Blue"])
```


## Radio Button Group ( @radio )
The @radio function creates a group of radio buttons. Users can select one option from the group.

### Parameters:
1. id (String): A unique identifier for the radio button group.
2. options (Array of Strings): An array of strings representing the radio button options.
### Example:
```
@radio("gender", ["Male", "Female", "Other"])
```

