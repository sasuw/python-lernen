# Getting Started with Python and Thonny

*A beginner-friendly guide for a young programmer (and an adult helping them)*

**Goal:** Install everything you need, write your first Python programs, and build a small game.

**You'll need:** A Windows 10 or 11 PC, an internet connection for installation, and about 45–60 minutes for your first session. No programming experience is needed.

> **For the adult:** This guide assumes a typical Windows PC with an Intel or AMD processor. If the PC has an ARM/Snapdragon processor, choose the ARM installer instead. macOS and Linux options are listed at the end. Let the learner do the typing and make the decisions whenever possible.

## 1. Install Thonny (and Python)

Python is the language you'll learn. **Thonny** is the program in which you'll write and run Python code. Conveniently, the normal Windows Thonny installer already includes Python, so **you do not need to install Python separately**.

1. Open a web browser and visit **<https://thonny.org/>**.
2. Under **Official downloads for Windows**, choose the installer for **Intel or AMD computers** (the usual type of PC). The download should be an `.exe` file.
3. Open the downloaded file. If Windows asks whether to allow it to run, check that it is the installer downloaded from the official Thonny website before proceeding.
4. Follow the setup instructions. Installing **for the current user / me only** is normally fine. Keep the default options unless there's a reason to change them.
5. Open **Thonny** from the Start menu.

**Check:** Thonny opens, with a place to type code and a **Shell** pane underneath. You are ready!

**If you don't see the same screen:** Thonny's exact appearance can vary slightly between versions. You can open the Shell with **View → Shell**.

## 2. Know your way around

Thonny has two important areas:

| Area | What it is for |
| --- | --- |
| **Editor** (usually top) | Write a program and save it as a `.py` file. |
| **Shell** (usually bottom) | See what a program prints, answer its questions, and try quick Python commands. |

Useful shortcuts:

| What you want to do | Shortcut |
| --- | --- |
| New program | `Ctrl+N` |
| Save your program | `Ctrl+S` |
| Run the current program | `F5` (or the green Run button) |
| Run step by step | `Ctrl+F5` |
| Go to the next big step while debugging | `F6` |

First, experiment in the **Shell**. Type each of these after the `>>>` prompt and press Enter:

```python
2 + 3
10 * 5
"hello" + " world"
```

Try changing the numbers and words. The Shell is a great place to experiment.

## 3. Your first program: Say hello!

Click in the **Editor** (not the Shell) and type:

```python
print("Hello, world!")
print("I am learning Python!")
```

1. Press **Ctrl+S** to save.
2. Create a folder such as `Documents/Python-Projects` and save the file as **`hello.py`**.
3. Press **F5** to run it.
4. Look at the Shell. It should show:

```text
Hello, world!
I am learning Python!
```

**Try it:** Change the messages, add another `print()` line, or print a calculation like `print(7 * 8)`.

### What just happened?

- `print(...)` tells Python to display something.
- Words in quotation marks are called **strings**.
- Parentheses `(...)` tell Python what to give to `print`.
- Python executes these statements from top to bottom.

## 4. Make the program interactive

Create a new file (**Ctrl+N**) and type:

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

Save it as **`greeting.py`** and press **F5**. Type your name in the **Shell**, then press Enter.

Here you have learned two new ideas:

- A **variable**, such as `name`, remembers a value.
- `input(...)` asks the person using the program to type something.

**Challenges:**

1. Ask for the person's favorite game and display it in a sentence.
2. Ask two questions and use both answers in your message.
3. Change the program to say hello three times.

### Numbers behave differently from text

Try this in a new file:

```python
age_text = input("How old are you? ")
age = int(age_text)
print("Next year you will be", age + 1)
```

`input()` gives you text. `int(...)` converts text such as `13` into a whole number so that Python can do arithmetic with it. If you type something that isn't a number, you'll get an error—that's normal, and you'll learn to handle it later.

## 5. Your first game: Guess the secret number

Create **`guessing_game.py`** and enter this program:

```python
import random

secret = random.randint(1, 20)
guess = 0
attempts = 0

print("I am thinking of a number between 1 and 20.")

while guess != secret:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You needed", attempts, "guesses.")
```

Save, press **F5**, and play!

**New ideas in this game:**

- `import random` adds a built-in tool for choosing random numbers.
- `random.randint(1, 20)` chooses a whole number from 1 through 20.
- `while` repeats code until a condition is no longer true.
- `if`, `elif`, and `else` let your program make decisions.
- `==` means *is equal to*; `!=` means *is not equal to*.
- The indented lines (spaces at the start) belong to the loop or decision above them. **Indentation matters in Python.**

**Upgrade your game (one change at a time):**

1. Make the secret number range from 1 to 100.
2. Give the player a maximum of 7 guesses.
3. Award a score based on the number of guesses.
4. Let the player play another round without restarting the program.

> Tip: It's okay if you can't solve every challenge immediately. Make a guess, change the code, run it, and observe what happens.

## 6. Bonus: Draw with Python

Want something more visual? Python has a built-in drawing module called **turtle**. Create **`drawing.py`**:

```python
import turtle

pen = turtle.Turtle()
pen.speed(3)

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
```

Run it to draw a square in a new window.

**Experiments:**

- Change `range(4)` to `range(3)` and change the turn to `120` degrees.
- Try `pen.circle(60)` after the loop.
- Change the pen color using `pen.color("blue")`.
- See what happens when you change the distance or speed.

This introduces a **for loop**, which repeats something a specified number of times.

## 7. How to figure out what went wrong

Every programmer gets errors. The aim isn't to avoid all mistakes; it's to learn how to investigate them.

1. **Read the last line of the error message** in the Shell. It often names the problem.
2. Check the **line number** mentioned in the message.
3. Look for missing quotation marks, brackets, colons (`:`), or indentation.
4. Change **one thing at a time** and run the program again.
5. If you're stuck, explain what you expected and what actually happened to the person helping you.

Some common errors:

| Error | What to check |
| --- | --- |
| `SyntaxError` | A typo, missing quote, bracket, or colon. |
| `IndentationError` | Spaces at the beginning of a line. |
| `NameError` | A misspelled variable name or a variable not yet created. |
| `ValueError` from `int(...)` | You entered something that couldn't be converted into a number. |

### See how Python thinks, step by step

In Thonny, choose **View → Variables**. Then open one of your programs and press **Ctrl+F5** instead of F5. Use **F6** to move forward one step at a time. Watch the variables change. This is called **debugging**, and it's a very useful skill.

## 8. What to do next

You don't need to learn everything at once. Here is a possible progression for the next few sessions:

| Session | Project | Concepts |
| --- | --- | --- |
| 1 | Hello, greeting, guessing game | `print`, `input`, variables, conditions, loops |
| 2 | Rock–paper–scissors | Randomness, `if`, comparing values |
| 3 | Quiz with a score | Repetition, counters, strings |
| 4 | Drawing patterns with turtle | `for` loops, geometry |
| 5 | Text adventure with different choices | Functions, branching, organizing code |
| 6 | Your own idea | Combine what you've learned |

Useful free resources:

- [Thonny official website](https://thonny.org/) — downloads and help
- [Python's official beginner tutorial](https://docs.python.org/3/tutorial/) — good as a reference, but not necessary to read from start to finish
- [Python turtle documentation](https://docs.python.org/3/library/turtle.html) — drawing commands and examples
- [Invent Your Own Computer Games with Python](https://inventwithpython.com/invent4thed/) — beginner-friendly game projects, freely readable online

## 9. For the adult helping

You don't have to deliver a formal course. A productive first session is simply installing Thonny, getting something to run, and finishing one small project.

- **Let him drive.** He types, chooses changes, and presses Run. You guide when needed.
- **Ask questions instead of immediately fixing mistakes.** For example: “What does this error message tell us?”
- **Explain the smallest concept needed right now.** You can save classes, type annotations, package management, Git, and architecture for later.
- **Make changes visible.** Predict what will happen before pressing F5, then compare the result.
- **Finish with a win.** Save the program, ask him what he wants to improve next time, and stop before it becomes frustrating.

A good initial rhythm is **30–45 minutes at a time**, with lots of experimentation and few lectures.

## 10. Installation troubleshooting and other operating systems

**Windows installer:** If the installer doesn't run, confirm it came from [thonny.org](https://thonny.org/), check whether Windows security or account permissions are blocking it, and ask the adult for help. Don't disable Windows security protections just to install a program.

**Python not found / wrong interpreter:** Thonny's bottom-right corner shows the Python interpreter. If necessary, select the Python installation bundled with Thonny. The normal installer should configure this automatically.

**Program seems stuck:** If it contains `input(...)`, look at the Shell; the program may be waiting for you to type a response and press Enter. For other cases, use Thonny's Stop button.

**macOS:** Visit [thonny.org](https://thonny.org/) and use the installer for Intel Macs or Apple Silicon (M-series), as appropriate. Python is included in the official macOS installer.

**Linux:** Visit [thonny.org](https://thonny.org/) for the current Linux installation choices. Linux installations may use an existing system Python instead of a bundled copy.

---

### First-session checklist

- [ ] Thonny is installed and opens successfully.
- [ ] I can type `2 + 3` in the Shell and see `5`.
- [ ] I saved and ran `hello.py`.
- [ ] I made a program ask for my name.
- [ ] I played my guessing game.
- [ ] I changed at least one program to do something new.

**Congratulations—you've started programming.** The best next project is one that *you* want to build.

---

*Prepared October 2026. Installation instructions were checked against the official Thonny website, which currently offers Thonny 5.0.0 with Python 3.14 for Windows 10/11. Download labels may change with future releases.*
