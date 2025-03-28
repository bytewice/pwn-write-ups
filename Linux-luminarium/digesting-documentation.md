# Searching for Manuals - Write-Up

## 🌟 Overview
**Challenge:** [Searching for Manuals]()  
**Category:** Documentation Digging  
**Description:**  
> [Your task is to locate the specific manpage containing the command that will display the flag. Unlike previous challenges where the command name was intuitive (like `flag` or `print_flag`), this time the command name has been *randomized* - requiring more thorough documentation searching skills.]  

---

## 🔍 Problem Analysis

- What made this challenge tricky or interesting?

To successfully solve this challenge, you'll need to combine fundamental documentation navigation skills with knowledge gained from all previous Pwn College dojo exercises. This builds progressively on the concepts covered in earlier modules.
- ```man -k [apropos]```

HINT 1: man man teaches you advanced usage of the man command itself, and you must use this knowledge to figure out how to search for the hidden manpage that will tell you how to use /challenge/challenge

HINT 2: though the man page is randomly named, you still actually use /challenge/challenge to get the flag!

And I found this problem interesting because it was the first to require a little bit of independency in the search, I was excited when I managed to solve it :D

---

## 🛠️ Solution Steps
### Step 1: Identifying the Target
[How did you approach finding the right manual?]
- Tools used: the command `man -k flag`.
You use it to find out any information about a flag in the many manuals in the system

### Step 2: Locating the Manual
You'll find out a few manual that has a string char attached to it, but there's one that seems a little bit odd: that's the manual whose description is `print the flag!`
- Let's call this manual `flag_manual` to not spoil your experience in finding it.

### Step 3: Reading the Manual
Having the manual in hands, all that's left is to read the manual.
- Use the command: `man flag_manual`
In the description of the manual you can see the following lines:

```
DESCRIPTION
  Output the flag when called with the right arguments.

  --fortune
        read a fortune

  --version
        output version information and exit

  --kdlnxs NUM
        print the flag if NUM is 720
```

### Step 3: Extracting the Answer

So you have all the things you need at hand, all that's left is to extract the flag. You can accomplish it after using the command `/challenge/challenge` with de argument kdlnxs and 720:

- `/chalenge/chalenge --kdlnxs 720` 
