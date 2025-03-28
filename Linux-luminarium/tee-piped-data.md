# Piped Data with tee - Write-Up

## 🌟 Overview
**Challenge:** Piped Data with tee  
**Category:** Command Line Piping  
**Description:**  
> This challenge teaches how to intercept and debug data flowing through pipes using the `tee` command. You need to examine the output of `/challenge/pwn` before it gets piped to `/challenge/college` to understand what input the program expects.

---

## 🔍 Problem Analysis
The challenge demonstrates a common debugging scenario:
1. When piping commands (`cmd1 | cmd2`), the intermediate output isn't visible
2. This makes troubleshooting failed pipes difficult
3. `tee` acts like a "T-splitter" to duplicate the stream

Key aspects:
- Need to intercept data between two programs
- Must preserve the original pipe functionality
- Requires understanding of `tee`'s dual purpose (file and stdout)

---

## 🛠️ Solution Steps
### Step 1: Initial Attempt (Problem Observation)
The first approach involved executing the direct pipe command:
```bash
/challenge/pwn | /challenge/college
```
- The terminal processed the command but returned an error without meaningful output
- This indicated the need for intermediate inspection of the data flow

### Step 2: Debugging with tee

Following the challenge's implicit suggestion, we implemented the `tee` command for pipeline debugging:  `/challenge/pwn | tee tmp-output | /challenge/college`

- The command appeared to execute without visible changes.
- The true purpose was to capture intermediate output for analysis.

### Step 3: Reading the debugging file

The critical investigation phase involved examining the captured data: `cat tmp-out`

- The file revealed hidden requirements for successful execution

- Specifically, it indicated the need for a particular argument format (let´s say `--secret bigsecret232` to not completely spoil your experience in the challenge)

- This discovery was crucial for progressing toward the solution

### Step 4: Finding the flag

With the required parameters identified, the final solution took form: `/challenge/pwn --secret bigsecret232 | /challenge/pwn`

Happy hacking! 💻🔐  
*— [belcx/bytewice]*

