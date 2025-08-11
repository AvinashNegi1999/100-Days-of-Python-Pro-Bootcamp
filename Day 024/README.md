# Day 24 – Files, Directories & Paths

## 📚 Concepts
- Open, read, and write files with `with` keyword.
- Relative vs Absolute file paths.
- Save high score in Snake Game.

## 🐍 Snake Game Update
- Added persistent high score stored in `data.txt`.
- Reads score on start, updates if player beats record.

```python
with open("C:/Users/avina/.../data.txt") as file:
    high_score = int(file.read())

with open("C:/Users/avina/.../data.txt", "w") as file:
    file.write(f"{new_high_score}")
```
![Code_vu3jk871jP](https://github.com/user-attachments/assets/a323713d-c9fe-4f1d-9b8e-b1a0722870ee)

