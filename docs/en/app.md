# 1. Creating the Application (@app)
The @app function initializes your application. It defines the title, developer details, and the default colors for the background and foreground.

Parameters:
1. title (String): The title of the application window.
2. Subtitle (String): Any other details which you want to tell.
3. backgroundColor (String): Background color in hexadecimal format (e.g., #ffffff for white).
4. foregroundColor (String): Foreground color in hexadecimal format (e.g., #000000 for black).
Example:
```
@app(title: "My App", developer: "Developer Name", backgroundColor: "#f0f0f0", foregroundColor: "#333333")
```
# 2. Displaying Images (@image)
The @image function adds an image to your application. You can control its dimensions and specify its source.

Parameters:
1. id (String): A unique identifier for the image.
2. url (String): The URL or path to the image.
3. width (Integer): The width of the image in pixels.
4. height (Integer): The height of the image in pixels.
Example:
```
@image(id: "logo", url: "https://example.com/logo.png", width: 200, height: 100)
```
# 3. Creating Headings
@displayH1 to @displayH6
These functions create headings with varying levels of importance, from @displayH1 (largest) to @displayH6 (smallest).

Parameters:
1. id (String): A unique identifier for the heading.
2. text (String): The content of the heading.
Example:
````
@displayH1(id: "mainHeading", text: "Welcome to BhashaX!")
```
# 4. Interactive Buttons
@button
The @button function adds a clickable button to your application. Buttons can trigger specific actions when clicked.

Parameters:
1. id (String): A unique identifier for the button.
2. label (String): The text displayed on the button.
Example:
````
@button(id: "submitBtn", label: "Submit")
```
# 5. Checkbox Inputs
@checkbox
The @checkbox function creates a checkbox input element, which allows users to select or deselect an option.

Parameters:
1. id (String): A unique identifier for the checkbox.
2. label (String): Text displayed next to the checkbox.
Example:
````
@checkbox(id: "acceptTerms", label: "I agree to the terms and conditions")
```
# 6. Color Attribute (@color)
The @color function sets a color for a specific GUI element.

Parameters:
1. id (String): The identifier of the element.
2. color (String): The color value in hexadecimal format.
Example:
````
@color(id: "mainHeading", color: "#ff4500")
```
# 7. Date Input
@date
The @date function creates an input field for selecting dates.

Parameters:
1. id (String): A unique identifier for the date input.
2. label (String): Label text displayed for the input field.
Example:
````
@date(id: "dob", label: "Select your birth date")
```
# 8. Date-Time Input
@datetime_local
This function creates an input field for selecting both a date and time.

Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
Example:
````
@datetime_local(id: "eventTime", label: "Event Date & Time")
```
# 9. Email Input (@email)
The @email function generates a text field for email address input.

Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
Example:
````
@email(id: "userEmail", label: "Enter your email")
```
# 10. Number Input (@number)
This function creates an input field for numeric values.

Parameters:
1. id (String): A unique identifier for the input field.
2. defaultValue (Number): The prefilled value in the input field.
Example:
````
@number(id: "quantity", defaultValue: 1)
```
# 11. Telephone Input ( @tel )
The @tel function generates an input field for telephone numbers.

Parameters:
1. id (String): A unique identifier for the input field.
2. label (String): Label text displayed for the input field.
Example:
````
@tel(id: "phone", label: "Enter your phone number")
```
# 12. Password Input ( @password )
This function creates an input field for password input, which obscures the text entered by the user.

Parameters:
1. id (String): A unique identifier for the input field.
2. defaultValue (String): The prefilled value in the input field.
Example:
````
@password(id: "userPassword", defaultValue: "")
```
# 13. Dropdown Select Menu ( @select )
The @select function generates a dropdown menu with a list of selectable options.

Parameters:
1. id (String): A unique identifier for the dropdown menu.
2. options (Array of Strings): An array of strings representing the dropdown options.
Example:
````
@select(id: "colorPicker", options: ["Red", "Green", "Blue"])
```
14. Radio Button Group ( @radio )
The @radio function creates a group of radio buttons. Users can select one option from the group.

Parameters:
1. id (String): A unique identifier for the radio button group.
2. options (Array of Strings): An array of strings representing the radio button options.
Example:
````
@radio(id: "gender", options: ["Male", "Female", "Other"])
```
