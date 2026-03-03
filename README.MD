# 🚀 Pinger Pro - Advanced Network Monitor

A professional, single-file Python script to monitor server availability and latency. 
**No installation required. No external libraries.** Just run and ping.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## 🇬🇧 English Documentation

### ⚡ Quick Start (One-Line Command)
You can run the script directly from your terminal without downloading the file manually.

**Linux / macOS (Terminal):**
```bash
curl -sL https://raw.githubusercontent.com/AmirHBuilds/pinger/main/pinger.py | python3
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/AmirHBuilds/pinger/main/pinger.py | python
```

---

### 📥 Manual Usage (Copy & Paste)
If you prefer to save the script or edit the server list:

1.  **Download:**
    *   Copy the code from [pinger.py](https://github.com/AmirHBuilds/pinger/blob/main/pinger.py).
    *   Paste it into a file named `pinger.py` on your server or computer.

2.  **Run:**
    Open your terminal/command prompt in the folder where you saved the file.

    *   **Windows:**
        ```bash
        python pinger.py
        ```
    *   **Linux / macOS:**
        ```bash
        python3 pinger.py
        ```

### ⚙️ Configuration
To add your own servers, open `pinger.py` with any text editor (Notepad, nano, vim) and edit the `SERVER_GROUPS` dictionary at the top of the file:

```python
SERVER_GROUPS = {
    "1": {
        "name": "My Custom Servers",
        "hosts": ["1.1.1.1", "google.com"]
    }
}
```

---

## 🇮🇷 راهنمای فارسی

### ⚡ اجرای سریع (بدون نیاز به دانلود)
شما می‌توانید بدون دانلود کردن فایل، تنها با یک دستور اسکریپت را مستقیماً از گیت‌هاب اجرا کنید.

**لینوکس / مک (Terminal):**
```bash
curl -sL https://raw.githubusercontent.com/AmirHBuilds/pinger/main/pinger.py | python3
```

**ویندوز (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/AmirHBuilds/pinger/main/pinger.py | python
```

---

### 📥 روش دستی (کپی و اجرا)
اگر می‌خواهید فایل را ذخیره کنید یا لیست سرورها را تغییر دهید:

۱. **دانلود:**
   *   کد را از [اینجا (pinger.py)](https://github.com/AmirHBuilds/pinger/blob/main/pinger.py) کپی کنید.
   *   آن را در فایلی به نام `pinger.py` در سرور یا کامپیوتر خود ذخیره کنید.

۲. **اجرا:**
   ترمینال یا CMD را در پوشه‌ای که فایل را ذخیره کردید باز کنید.

   *   **در ویندوز:**
       ```bash
       python pinger.py
       ```
   *   **در لینوکس / مک:**
       ```bash
       python3 pinger.py
       ```

### ⚙️ تنظیمات شخصی
برای تغییر لیست سرورها، فایل `pinger.py` را با هر ویرایشگر متنی باز کنید و بخش `SERVER_GROUPS` را در بالای کد ویرایش کنید.
