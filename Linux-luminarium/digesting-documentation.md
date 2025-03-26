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
- ```man -k flag```

HINT 1: man man teaches you advanced usage of the man command itself, and you must use this knowledge to figure out how to search for the hidden manpage that will tell you how to use /challenge/challenge

HINT 2: though the man page is randomly named, you still actually use /challenge/challenge to get the flag!

And I found this problem interesting because it was the first to require a little bit of independency in the search, I was excited when I managed to solve it :D

---

## 🛠️ Solution Steps
### Step 1: Identifying the Target
[How did you approach finding the right manual?]
- Tools used (e.g., `man`, `apropos`, Google, etc.).
- Keywords or commands you tried.

### Step 2: Locating the Manual
[Describe the process of narrowing down the documentation.]
- Did you find multiple candidates? How did you filter them?
- Was there a specific section or flag mentioned in the challenge?

### Step 3: Extracting the Answer
[How did you extract the solution from the manual?]
- Example:  
  ```bash
  man <command> | grep "<keyword>"