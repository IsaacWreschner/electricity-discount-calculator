
# 🔌 Electricity Discount Calculator | מחשבון הנחה חשמל

This simple application helps you calculate how much electricity discount you can get by selecting the correct time range and days where the discount applies.

---

## 📋 What It Does

- You choose the **type**: `DAILY` (every day) or `WEEKLY` (specific days).
- You select the **start hour** and **end hour** (e.g., 23 to 6).
- You choose the **discount percentage** (e.g., 10%).
- You upload the **CSV file** with hourly electricity consumption data.
- The app will calculate:
  - How much of your total usage falls in the selected range.
  - How much of a discount you would get in total.

---

## 🧰 How to Run This App (For Beginners)

### Step 1: Install Python

1. After cloning this repository, go to: https://www.python.org/downloads/
2. Click **Download Python** (choose the latest version).
3. During installation, **make sure to check the box "Add Python to PATH"**.
4. Finish the installation.

### Step 2: Install Required Packages

Open a terminal (Command Prompt) and run:
```bash
pip install pandas
```

### Step 3: Run the App

Open a terminal (Command Prompt) on the directory and run:
```bash
python electricity_discount.py
```

A window will open where you can enter your values and upload your file.

---

## 📁 CSV File Format and Source

**Where do I get the CSV file?**

> You can download your hourly electricity usage CSV file directly from the **Israel Electric Company (IEC / חברת החשמל)** website — *only if you have a smart meter (מונה חכם)*.

- Go to: https://www.iec.co.il
- Log in with your user account (or create one).
- Go to **"My Account" → "Smart Meter" (מונה חכם)**.
- Download the **hourly usage report** as a CSV file.

The CSV file should look like this:
```
Date, Time, Consumption
28/01/2025, 00:00, 1.23
28/01/2025, 01:00, 1.45
...
```

> ⚠️ Make sure the file contains **hourly data** in three columns: `Date`, `Time`, and `Consumption`.

---

## 🌍 Hebrew Instructions | הוראות בעברית

### 🧭 מה התוכנה עושה?

- בחרו אם ההנחה תקפה כל יום (`DAILY`) או רק בימים מסוימים (`WEEKLY`).
- הזינו שעת התחלה ושעת סיום (למשל 23 עד 6).
- הזינו את גובה ההנחה באחוזים (למשל 10%).
- העלו את קובץ צריכת החשמל (CSV).
- התוצאה תראה:
  - כמה מהצריכה שלכם הייתה בטווח ההנחה.
  - וכמה כסף תחסכו מההנחה הכוללת.

### 🖥️ איך מריצים את התוכנה?

#### שלב 1: התקנת פייתון

1. לאחר העתקת הקוד למחשב שלכם, כנסו לכתובת: https://www.python.org/downloads/
2. לחצו על **Download Python**.
3. סמנו את האפשרות **"Add Python to PATH"** במהלך ההתקנה.
4. השלימו את ההתקנה.

#### שלב 2: התקנת חבילות נדרשות

פתחו חלון פקודה והקלידו:
```bash
pip install pandas
```

#### שלב 3: הרצת התוכנה

פתחו חלון פקודה באותה תקייה והריצו כך:
```bash
python electricity_discount.py
```

ייפתח חלון בו תוכלו למלא את הנתונים ולקבל תוצאה.

---

### 📁 פורמט קובץ ה-CSV ומאיפה משיגים אותו

**מאיפה משיגים את קובץ הנתונים?**

> הקובץ ניתן להורדה מאתר **חברת החשמל**, רק אם יש לכם **מונה חכם**.

- היכנסו לאתר: https://www.iec.co.il  
- התחברו לחשבון שלכם (או צרו חשבון).
- עברו ל: **"החשבון שלי" → "מונה חכם"**.
- הורידו את **דו"ח צריכה לפי שעות** בפורמט CSV.

הקובץ צריך להיראות כך:
```
תאריך, שעה, צריכה
28/01/2025, 00:00, 1.23
28/01/2025, 01:00, 1.45
...
```

> ⚠️ שימו לב: הקובץ חייב להכיל נתונים **שעתיים** עם שלוש עמודות בלבד: `תאריך`, `שעה`, `צריכה`.

---

### 📞 Need Help?

Contact your provider or a tech-savvy friend if you have trouble opening CSV files or installing Python.
