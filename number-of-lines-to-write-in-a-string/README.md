## Number of Lines to write in a string - Difficulty: Easy

This challenge consisted on write the letters of a given string `S`, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array `widths`, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'. I started by creating a loop through every letter in `S` and checked the width of the letter in the `widths` array using the formula `ord(letter) - 97` to get the index. Then added to a variable called `letterCount`, which if it was higher than `100`, adds `1` to a variable called `lines` and sets the `letterCount` to the current letter width.

## My perfomance

![My performance](https://raw.githubusercontent.com/itspedruu/leetcode-solutions/master/number-of-lines-to-write-in-a-string/success_screenshot.png)