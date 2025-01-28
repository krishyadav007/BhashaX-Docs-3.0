# Combining Arrays and Loops
Authors: Yuvaansh Kapila
## Overview
* Concepts Taught: Performing advanced operations on arrays.
## Learning plan:
Create an array with the names of 5 colors, add a new color, remove one color, and display all colors using a loop.
$colors = ["Red", "Green", "Blue", "Yellow", "Purple"];
$colors[] = "Orange"; // Adding a new color
unset($colors[1]); // Removing "Green"
foreach ($colors as $color) {
  @display($color);
}
