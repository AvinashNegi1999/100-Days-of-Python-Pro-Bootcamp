# Day 27 – Tkinter & Python Functions

## What I Learned

* Creating windows and labels using **Tkinter**
* Using **buttons**, **entry widgets**, and configuring widget options
* Exploring Tkinter widgets like **Radiobuttons**, **Scales**, and **Checkbuttons**
* Layout managers: `.pack()`, `.place()`, and `.grid()`
* Python function features: setting default values, using `*args` and `**kwargs`

## Summary

Practiced building GUI programs with Tkinter and deepened understanding of flexible function arguments to write cleaner, more versatile code.

## Code Snippet: \*args and \*\*kwargs

```python
def greet(*names, **info):
    for name in names:
        print(f"Hello, {name}!")
    for key, value in info.items():
        print(f"{key}: {value}")

greet("Alice", "Bob", age=25, city="New York")
```

*Output:*

```
Hello, Alice!
Hello, Bob!
age: 25
city: New York
```
---


![Code_bsAe8KZre0](https://github.com/user-attachments/assets/a1e94a69-e242-4291-b4f1-569ce84f9578)
