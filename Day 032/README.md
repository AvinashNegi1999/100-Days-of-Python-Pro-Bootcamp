# 🎉 Birthday Wisher

A Python script that automatically sends personalized birthday emails using Gmail + App Password.



## 📌 Features
- Reads birthdays from `birthdays.csv`
- Picks a random template from `letter_templates/`
- Replaces `[NAME]` with recipient’s name
- Sends email via Gmail SMTP

---

![Code_oJWFgvMg8k](https://github.com/user-attachments/assets/b0378b06-b455-4117-bf68-146e4bbf5e01)

---

## 📂 Usage
1. Add birthdays to `birthdays.csv`:
   ```csv
   name,email,year,month,day
   John Doe,john@example.com,1995,8,19
````

2. Add templates in `letter_templates/`:

   ```
   letter_1.txt
   letter_2.txt
   letter_3.txt
   ```

3. Run:

   ```bash
   python main.py
   ```

---

## ⚠️ Note

Use a **Gmail App Password**, not your normal Gmail password.


