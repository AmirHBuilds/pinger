
# 🚀 Pinger - Advanced Network Monitor

A professional, single-file Python script to monitor server availability and latency.
**Multi-threaded, Cross-platform, and Fully Configurable.**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## 🇬🇧 English Documentation

### 📥 1. Download & Install
Run the following command in your terminal to download the script and save it as `pinger.py`.

**Linux / macOS (Terminal):**
```bash
curl -o pinger.py https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py
```

**Windows (PowerShell):**
```powershell
iwr -Uri https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py -OutFile pinger.py
```

### ⚙️ 2. Configuration (Optional)
To add your own servers or change the groups, simply open `pinger.py` with any text editor (like `nano`, `vim`, `notepad`) and edit the `SERVER_GROUPS` section at the top:

```python
SERVER_GROUPS = {
    "1": {
        "name": "My Custom Servers",
        "hosts": ["1.1.1.1", "google.com"]
    }
}
```

### 🚀 3. How to Run
Once downloaded, you can run the script anytime using Python:

*   **Linux / macOS:**
    ```bash
    python3 pinger.py
    ```
*   **Windows:**
    ```bash
    python pinger.py
    ```

---

## 🇮🇷 راهنمای فارسی

### 📥 ۱. دانلود و ذخیره‌سازی
برای دانلود اسکریپت و ذخیره آن در سرور یا کامپیوتر خود، دستور زیر را اجرا کنید. این کار فایل `pinger.py` را دانلود می‌کند تا بتوانید آن را ویرایش کنید.

**لینوکس / مک (ترمینال):**
```bash
curl -o pinger.py https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py
```

**ویندوز (پاورشل):**
```powershell
iwr -Uri https://raw.githubusercontent.com/AmirHBuilds/pinger/refs/heads/main/pinger.py -OutFile pinger.py
```

### ⚙️ ۲. تنظیمات و ویرایش
برای اضافه کردن سرورهای خودتان، فایل `pinger.py` را با هر ویرایشگر متنی (مانند nano یا Notepad) باز کنید و بخش `SERVER_GROUPS` را در بالای فایل تغییر دهید:

```python
SERVER_GROUPS = {
    "1": {
        "name": "سرورهای شخصی من",
        "hosts": ["1.1.1.1", "google.com"]
    }
}
```

### 🚀 ۳. نحوه اجرا
پس از دانلود، می‌توانید هر زمان که بخواهید اسکریپت را با دستور زیر اجرا کنید:

*   **در لینوکس / مک:**
    ```bash
    python3 pinger.py
    ```
*   **در ویندوز:**
    ```bash
    python pinger.py
    ```
