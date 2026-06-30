```markdown
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/Bale-Bot-0A8EFF?style=for-the-badge&logo=bale" alt="Bale">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/kouroshhamidi92-ship-it/NumberGuessBot?style=social" alt="GitHub stars">
</p>

# 🎯 NumberGuessBot | نابغه‌باز

**یک بازی هوشمند و کامل برای حدس عدد مخفی** که با یک کد، روی ۴ پلتفرم مختلف اجرا می‌شود: **تلگرام** | **بله** | **ویندوز** | **وب/اندروید**

---

## 📖 فهرست مطالب
- [✨ ویژگی‌ها](#-ویژگی‌ها)
- [📸 پیش‌نمایش](#-پیش‌نمایش)
- [🚀 نصب و راه‌اندازی](#-نصب-و-راه‌اندازی)
- [🖥️ نسخه دسکتاپ](#️-نسخه-دسکتاپ)
- [🌐 نسخه وب/اندروید](#-نسخه-وباندروید)
- [☁️ استقرار روی هاست رایگان](#️-استقرار-روی-هاست-رایگان)
- [📁 ساختار پروژه](#-ساختار-پروژه)
- [🤝 مشارکت](#-مشارکت)
- [👨‍💻 توسعه‌دهنده](#-توسعه‌دهنده)
- [💳 حمایت](#-حمایت)

---

## ✨ ویژگی‌ها

- 🎮 **بازی حدس عدد** با راهنمایی بالاتر/پایین‌تر
- 💰 **سیستم سکه** – با هر برد سکه دریافت کنید
- 🏪 **فروشگاه** با ۹ آیتم (تم، راهنما، بوست و...)
- 🏆 **رتبه‌بندی جهانی**
- ⚔️ **دوئل با ربات هوشمند**
- 📈 **مراحل پیشرونده** – سختی بازی افزایش می‌یابد
- ⏱️ **زمان‌سنج** برای هر بازی
- 🎯 **رکورد شخصی**
- ⚙️ **تنظیم بازه اعداد** (۳ حالت آماده + سفارشی)
- 🎨 **طراحی Glassmorphism** (نسخه وب)
- 🔥 **پشتیبانی از PWA** – نصب به عنوان اپ روی موبایل
- 📝 **ثبت‌نام با شماره/ایمیل** (نسخه وب)
- 📦 **بدون نیاز به دیتابیس** – ذخیره‌سازی با JSON
- 🌍 **پشتیبانی از فارسی و انگلیسی**

---

## 📸 پیش‌نمایش

### نسخه تلگرام / بله
```
🎮 به نابغه‌باز خوش آمدی!
💰 سکه: 100
🏆 بهترین: —
📈 مرحله: 1

👇 یکی از گزینه‌ها را انتخاب کن:

[🎮 بازی جدید]  [📊 وضعیت]
[💰 فروشگاه]   [🏆 رتبه‌بندی]
[⚔️ دوئل]     [⚙️ تنظیم بازه]
[📖 راهنما]
```

### نسخه وب / اندروید
- طراحی Glassmorphism با بیش از ۲۰۰ انیمیشن
- ۳۵۰+ ذره شناور در پس‌زمینه
- فروشگاه با ۹ آیتم
- سیستم سکه و رتبه‌بندی
- دوئل با ربات هوشمند
- ثبت‌نام با شماره تلفن یا ایمیل

---

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- پایتون 3.9 یا بالاتر
- کتابخانه `python-telegram-bot`

### مراحل نصب

```bash
# 1. کلون کردن پروژه
git clone https://github.com/kouroshhamidi92-ship-it/NumberGuessBot.git
cd NumberGuessBot

# 2. نصب کتابخانه‌ها
pip install -r requirements.txt

# 3. ساخت فایل .env با توکن ربات
# برای تلگرام:
PLATFORM=telegram
TELEGRAM_BOT_TOKEN=توکن_ربات_خود_را_وارد_کنید

# برای بله:
PLATFORM=bale
BALE_BOT_TOKEN=توکن_ربات_خود_را_وارد_کنید

# 4. اجرای ربات
python bot.py
```

---

## 🖥️ نسخه دسکتاپ

```bash
python desktop_app.py
```

### ساخت فایل exe با PyInstaller
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name="NumberGuessGame" desktop_app.py
```

### ساخت فایل exe با Nuitka (سرعت بالاتر)
```bash
pip install nuitka
python -m nuitka --standalone --enable-plugin=pyqt6 --windows-console-mode=disable --lto=yes --assume-yes-for-downloads --remove-output --output-dir=output --jobs=4 desktop_app.py
```

---

## 🌐 نسخه وب/اندروید

فایل `index.html` را در مرورگر باز کنید.

برای تبدیل به اپلیکیشن اندروید:
- **PWA2APK**
- **WebViewGold**
- **Android Studio** (با WebView)

---

## ☁️ استقرار روی هاست رایگان

### بهترین گزینه‌ها

| سرویس | مزایا | نیاز به کارت |
|-------|-------|-------------|
| [Render](https://render.com) | ✅ بدون کارت بانکی، ۷۵۰ ساعت رایگان در ماه | ❌ |
| [Koyeb](https://koyeb.com) | ✅ بدون کارت بانکی، اتصال به گیت‌هاب | ❌ |
| [PythonAnywhere](https://pythonanywhere.com) | ✅ بدون کارت بانکی، ۲۴/۷ روشن | ❌ |

### استقرار روی Render

1. در [render.com](https://render.com) ثبت‌نام کنید.
2. روی **"New +"** و سپس **"Web Service"** کلیک کنید.
3. مخزن گیت‌هاب خود را انتخاب کنید.
4. تنظیمات زیر را وارد کنید:

| گزینه | مقدار |
|--------|-------|
| **Name** | `numberguessbot` |
| **Environment** | `Python` |
| **Build Command** | `pip install --upgrade pip && pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | `Free` |

5. متغیرهای محیطی را اضافه کنید:

| Key | Value |
|-----|-------|
| `PLATFORM` | `telegram` یا `bale` |
| `TELEGRAM_BOT_TOKEN` | توکن ربات تلگرام |
| `BALE_BOT_TOKEN` | توکن ربات بله |

6. روی **"Create Web Service"** کلیک کنید.

### جلوگیری از خوابیدن (Keep Alive)

از [UptimeRobot](https://uptimerobot.com) استفاده کنید:
1. ثبت‌نام کنید (رایگان).
2. یک مانیتور جدید از نوع `HTTP(s)` بسازید.
3. آدرس: `https://numberguessbot.onrender.com/health`
4. فاصله: `5 Minutes`

---

## 📁 ساختار پروژه

```
NumberGuessBot/
├── bot.py              # کد اصلی ربات
├── game_core.py        # منطق بازی
├── app.py              # اپ Flask برای Render
├── desktop_app.py      # نسخه دسکتاپ PyQt6
├── index.html          # نسخه وب/اندروید
├── requirements.txt    # کتابخانه‌ها
├── .env.example        # نمونه متغیرهای محیطی
├── README.md           # این فایل
├── LICENSE             # مجوز MIT
├── users/              # اطلاعات کاربران (ساخته می‌شود)
└── leaderboard.json    # رتبه‌بندی جهانی (ساخته می‌شود)
```

---

## 🤝 مشارکت

1. مخزن را **Fork** کنید.
2. یک **Branch** جدید بسازید (`git checkout -b feature/your-feature`).
3. تغییرات را **Commit** کنید (`git commit -m 'Add feature'`).
4. **Push** کنید (`git push origin feature/your-feature`).
5. یک **Pull Request** باز کنید.

---

## 👨‍💻 توسعه‌دهنده

**کوروش حمیدی**  
گیت‌هاب: [kouroshhamidi92-ship-it](https://github.com/kouroshhamidi92-ship-it)

---

## 💳 حمایت

اگر از این پروژه خوشتان آمده، می‌توانید از طریق شماره کارت زیر حمایت کنید:

```
5022291532823695 (Shaparak)
```

---

## 📜 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است – برای جزئیات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

---

<p align="center">
  <img src="https://img.shields.io/badge/⭐_اگر_خوشت_آمد_ستاره_فراموش_نشه-FFD700?style=for-the-badge" alt="Star">
</p>

---

**ساخته شده با ❤️ توسط کوروش حمیدی – ایران**
```

---

## 🔥 تفاوت‌های نسخه جدید

| مورد | نسخه قبل | نسخه جدید |
|------|---------|----------|
| **ساختار** |松散 | منظم با فهرست مطالب |
| **ویژگی‌ها** | در یک پاراگراف | در قالب لیست منظم |
| **پیش‌نمایش** | توضیحی | کد باکس شبیه‌سازی شده |
| **نصب** | مختصر | گام‌به‌گام با کدهای دقیق |
| **استقرار** | اشاره‌ای | جدول + راهنمای کامل |
| **جذابیت** | معمولی | ویترینی و حرفه‌ای |

این README کاملاً استاندارد، قابل کپی و بدون مشکل نمایش در گیت‌هاب است.
