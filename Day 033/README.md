# Day 33 – ISS Overhead Notifier 🌌

## Overview

Python program that **notifies you when the ISS is overhead at night**. It uses APIs, datetime handling, and email automation for a real-world Python project.

---

## Features

* Fetches ISS position from the **Open Notify API**.
* Checks **sunrise and sunset times** using the **Sunrise-Sunset API**.
* Determines if the ISS is **near your location (±5°)** and if it’s **night**.
* Sends an **email notification** when conditions are met.
* Runs **continuously every 60 seconds**.

---

## How to Use

1. Install dependencies:

```bash
pip install requests
```

2. Update your coordinates and email credentials in the script.
3. Run:

```bash
python day_33_iss_notifier.py
```

---
![Code_R251g9T46V](https://github.com/user-attachments/assets/9f4f2d92-3fe5-49fb-bce7-45e9656f14b5)



