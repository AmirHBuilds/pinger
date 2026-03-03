# 🚀 Pinger - Advanced Network Monitor

A professional, single-file Python script to monitor server availability and latency.
**Multi-threaded, Cross-platform, and Fully Configurable.**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## 🇬🇧 English Documentation

### 📥 Option 1: Command Line Download (Recommended)
Run the following command in your terminal to download the script and save it as `pinger.py`.

**Linux / macOS (Terminal):**
```bash
curl -o pinger.py https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py
```

**Windows (PowerShell):**
```powershell
iwr -Uri https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py -OutFile pinger.py
```

### 📋 Option 2: Manual Copy & Paste
If you prefer, you can manually create the file on your server:
1.  Open the code here: [pinger.py on GitHub](https://github.com/AmirHBuilds/pinger/blob/main/pinger.py).
2.  Copy the code.
3.  Create a new file on your server named `pinger.py` and paste the code inside.

### ⚙️ Configuration
To add your own servers or groups, open `pinger.py` with any text editor (like `nano`, `vim`, or `Notepad`) and edit the `SERVER_GROUPS` dictionary at the top of the file:

```python
SERVER_GROUPS = {
    "1": {
        "name": "My Custom Servers",
        "hosts": [
            "1.1.1.1",
            "google.com",
            "myserver.local"
        ]
    }
}
```

### 🚀 How to Run
Once downloaded and configured, run the script:

**Linux / macOS:**
```bash
python3 pinger.py
```

**Windows:**
```bash
python pinger.py
```

---

## 🇮🇷 راهنمای فارسی

### 📥 روش اول: دانلود با دستور (پیشنهادی)
برای دانلود اسکریپت و ذخیره آن به نام `pinger.py` در سرور یا کامپیوتر خود، دستور زیر را اجرا کنید:

**لینوکس / مک (ترمینال):**
```bash
curl -o pinger.py https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py
```

**ویندوز (پاورشل):**
```powershell
iwr -Uri https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py -OutFile pinger.py
```

### 📋 روش دوم: کپی دستی
اگر مایل هستید، می‌توانید فایل را به صورت دستی ایجاد کنید:
۱. کدها را از [اینجا (pinger.py)](https://github.com/AmirHBuilds/pinger/blob/main/pinger.py) کپی کنید.
۲. یک فایل جدید به نام `pinger.py` در سرور خود بسازید و کدها را در آن قرار دهید.

### ⚙️ تنظیمات و شخصی‌سازی
برای تغییر لیست سرورها، فایل `pinger.py` را با ویرایشگر متن باز کنید و بخش `SERVER_GROUPS` را در بالای فایل ویرایش کنید:

```python
SERVER_GROUPS = {
    "1": {
        "name": "سرورهای شخصی من",
        "hosts": [
            "1.1.1.1",
            "google.com",
            "myserver.local"
        ]
    }
}
```

### 🚀 نحوه اجرا
پس از دانلود و تنظیم، اسکریپت را اجرا کنید:

**لینوکس / مک:**
```bash
python3 pinger.py
```

**ویندوز:**
```bash
python pinger.py
```
