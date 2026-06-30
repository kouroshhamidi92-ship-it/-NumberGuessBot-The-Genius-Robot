```markdown
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/Bale-Bot-0A8EFF?style=for-the-badge&logo=bale" alt="Bale">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Platform-Web%20%7C%20Desktop%20%7C%20Android-orange?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/github/stars/kouroshhamidi92-ship-it/NumberGuessBot?style=social" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/kouroshhamidi92-ship-it/NumberGuessBot?style=social" alt="GitHub forks">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=32&duration=3000&pause=500&color=F79D22&center=true&vCenter=true&random=false&width=700&lines=🎯+NumberGuessBot+%7C+نابغه‌باز;🤖+Smart+Number+Guessing+Game;💎+Coin+System+%2B+Shop;⚔️+Duels+with+AI+Bot;📱+Telegram+%7C+Bale+%7C+Web+%7C+Desktop" alt="Typing SVG">
</p>

---

## 📌 What is NumberGuessBot?

**NumberGuessBot** is a complete, cross-platform number guessing game with a **coin system**, **in-app shop**, **AI bot duels**, and **global leaderboards**. The same codebase runs on **4 platforms**:

| Platform | Description | Status |
|----------|-------------|--------|
| 🤖 **Telegram** | Bot with inline keyboards & professional menu | ✅ Complete |
| 💬 **Bale** | Bot with inline keyboards (same code with BASE_URL) | ✅ Complete |
| 🖥️ **Desktop** | PyQt6 GUI application with high performance | ✅ Complete |
| 🌐 **Web/Android** | HTML version with PWA support & 200+ animations | ✅ Complete |

---

## ✨ 30+ Amazing Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | 🎮 **Number Guessing Game** | Guess the secret number with higher/lower hints |
| 2 | 💰 **Coin System** | Earn coins per win and spend in the shop |
| 3 | 🏪 **Shop** | 9 items including themes, hints, coins, etc. |
| 4 | 🏆 **Global Leaderboard** | Store and display top players worldwide |
| 5 | ⚔️ **AI Bot Duels** | Battle against a smart AI bot |
| 6 | 📈 **Progressive Levels** | Difficulty increases automatically with each win |
| 7 | ⏱️ **Timer** | Track time spent on each game |
| 8 | 🎯 **Personal Best** | Store each user's best performance |
| 9 | ⚙️ **Dynamic Range Settings** | 3 presets + custom range |
| 10 | 📱 **Cross-Platform** | Works on Telegram, Bale, Windows, Android |
| 11 | 🔒 **Local Storage** | JSON file storage – no database required |
| 12 | 🎨 **Glassmorphism UI** | Modern, sleek inline keyboards |
| 13 | 🧠 **AI-Powered Hints** | Smart messages based on distance from target |
| 14 | 📊 **Advanced Statistics** | Attempts, time, level, best score |
| 15 | 🎨 **200+ Animations** | GSAP-powered animations (web version) |
| 16 | 🔥 **PWA Support** | Install as native app on mobile |
| 17 | 📝 **Phone/Email Auth** | Local authentication (web version) |
| 18 | 🎯 **Daily Challenges** | (Coming soon) |
| 19 | 🌍 **Multilingual** | Full Persian support |
| 20 | 🚀 **High Performance** | Optimized for speed and efficiency |
| 21 | 🔄 **Render Deployment** | Free 24/7 hosting support |
| 22 | 📦 **No Database Required** | Uses JSON for data storage |
| 23 | 🛡️ **Error Handling** | Robust exception management |
| 24 | 📱 **Mobile Responsive** | Works on all screen sizes |
| 25 | 🎵 **Sound Effects** | (Coming soon) |
| 26 | 🌓 **Dark/Light Themes** | (Coming soon) |
| 27 | 📊 **Admin Dashboard** | (Coming soon) |
| 28 | 👥 **Multiplayer Online** | (Coming soon) |
| 29 | 📈 **Progress Reports** | Performance graphs |
| 30 | 🏅 **Medals & Achievements** | (Coming soon) |

---

## 📸 Preview

### Telegram/Bale Version

```
🎮 Welcome to NumberGuessBot!
💰 Coins: 100
🏆 Best: —
📈 Level: 1

👇 Choose an option:

[🎮 New Game]  [📊 Status]
[💰 Shop]     [🏆 Leaderboard]
[⚔️ Duel]     [⚙️ Set Range]
[📖 Help]
```

### Web/Android Version

- **Glassmorphism** design with **350+ floating particles**
- **200+ animations** powered by GSAP
- **9-item shop** with coin system
- **AI bot duels** with smart logic
- **Local authentication** with phone/email
- **PWA-ready** – install as native app

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- `python-telegram-bot` library

### 1. Clone the Repository
```bash
git clone https://github.com/kouroshhamidi92-ship-it/NumberGuessBot.git
cd NumberGuessBot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your Bot Tokens

#### For Telegram:
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow the instructions
3. Copy your bot token

#### For Bale:
1. Message [@BotFather](https://bale.ai/botfather) on Bale
2. Send `/newbot` and follow the instructions
3. Copy your bot token

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
# Choose platform: telegram or bale
PLATFORM=telegram

# Telegram bot token (if using Telegram)
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

# Bale bot token (if using Bale)
BALE_BOT_TOKEN=YOUR_BALE_BOT_TOKEN
```

### 5. Run the Bot

#### Windows:
```bash
python bot.py
```

#### Linux/Mac:
```bash
python3 bot.py
```

---

## 🖥️ Desktop Version (PyQt6)

### Run:
```bash
python desktop_app.py
```

### Build with Nuitka (High Speed):
```bash
python -m nuitka --standalone --enable-plugin=pyqt6 --windows-console-mode=disable --lto=yes --assume-yes-for-downloads --remove-output --output-dir=output --jobs=4 desktop_app.py
```

### Build with PyInstaller (Simpler):
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name="NumberGuessGame" desktop_app.py
```

---

## 🌐 Web/Android Version

Open `index.html` in your browser or on your phone.

### Web Version Features:
- ✅ **Glassmorphism design** with 200+ animations
- ✅ **Local authentication** with phone/email
- ✅ **Coin system & shop** with 9 items
- ✅ **Local leaderboard** (stored in localStorage)
- ✅ **AI bot duels** with smart logic
- ✅ **Progressive levels** with increasing difficulty
- ✅ **Timer** during gameplay
- ✅ **350+ floating particles** in background
- ✅ **GSAP-powered animations**
- ✅ **PWA-ready** – install as native app

### Convert to Android App:
- Use **PWA2APK** or **WebViewGold**
- Build with **Android Studio** using WebView

---

## ☁️ Free Hosting Deployment

### Best Free Options:

| Service | Advantages | Card Required |
|---------|------------|---------------|
| [Render](https://render.com) | ✅ No credit card, 750 hours/month free | ❌ |
| [Koyeb](https://koyeb.com) | ✅ No credit card, GitHub integration | ❌ |
| [PythonAnywhere](https://pythonanywhere.com) | ✅ No credit card, 24/7 uptime | ❌ |
| [Oracle Cloud](https://oracle.com/cloud/free) | ✅ Always free VM, 24GB RAM | ✅ |

### Deploy on Render:

1. Sign up at [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Enter these settings:

| Setting | Value |
|---------|-------|
| **Name** | `numberguessbot` |
| **Environment** | `Python` |
| **Build Command** | `pip install --upgrade pip && pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | `Free` |

5. Add environment variables:

| Key | Value |
|-----|-------|
| `PLATFORM` | `telegram` or `bale` |
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token |
| `BALE_BOT_TOKEN` | Your Bale bot token |

6. Click **"Create Web Service"**

### Prevent Sleep (Keep Alive):

Use [UptimeRobot](https://uptimerobot.com):
1. Sign up (free)
2. Create a new monitor (Type: `HTTP(s)`)
3. Set URL: `https://numberguessbot.onrender.com/health`
4. Set Interval: `5 Minutes`

---

## 📁 Project Structure

```
NumberGuessBot/
├── bot.py              # Main bot code (Telegram & Bale)
├── game_core.py        # Game core logic
├── app.py              # Flask app for Render
├── desktop_app.py      # PyQt6 desktop version
├── index.html          # Web/Android version
├── requirements.txt    # Python dependencies
├── .env.example        # Sample environment variables
├── .gitignore          # Ignored files
├── README.md          # This file
├── LICENSE            # MIT License
├── users/             # User data (auto-generated)
└── leaderboard.json   # Global leaderboard (auto-generated)
```

---

## 🛠️ Technologies Used

| Technology | Description |
|------------|-------------|
| **Python 3.9+** | Core programming language |
| **python-telegram-bot** | Main bot framework |
| **PyQt6** | Desktop GUI framework |
| **Flask** | Web server for Render |
| **Gunicorn** | WSGI HTTP server |
| **HTML/CSS/JS** | Web version |
| **GSAP** | Advanced animations |
| **JSON** | Data storage |
| **Git** | Version control |
| **Render** | Cloud hosting |

---

## 🤝 How to Contribute

1. **Fork** this repository
2. Create a new **branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

---

## 👨‍💻 Developer

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/kouroshhamidi92-ship-it">
        <img src="https://avatars.githubusercontent.com/u/your-avatar" width="120px;" alt="Avatar"/><br />
        <sub><b>Kourosh Hamidi</b></sub>
      </a>
      <br />
      <a href="https://github.com/kouroshhamidi92-ship-it/NumberGuessBot/commits?author=kouroshhamidi92-ship-it" title="Code">💻</a>
      <a href="#design-kouroshhamidi92-ship-it" title="Design">🎨</a>
      <a href="https://github.com/kouroshhamidi92-ship-it/NumberGuessBot/commits?author=kouroshhamidi92-ship-it" title="Documentation">📖</a>
    </td>
  </tr>
</table>

---

## 💳 Support the Project

If you enjoy this project and want to support its development:

```
5022291532823695 (Shaparak)
```

<p align="center">
  <img src="https://img.shields.io/badge/💳_Support_Card-5022291532823695-FFD700?style=for-the-badge" alt="Support Card">
</p>

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## ⭐ Why Star This Project?

| Reason | Description |
|--------|-------------|
| 🚀 **Complete & Multi-Platform** | One codebase, 4 platforms |
| 💡 **Educational** | Great resource for learning bot development |
| 🆓 **Free & Open Source** | 100% free to use and modify |
| 🔥 **Modern Stack** | Uses latest Python, PyQt6, GSAP |
| 🌍 **Global** | Works on Telegram and Bale |
| 💎 **High Quality** | Clean, documented, optimized code |
| 🤝 **Contributable** | Open to PRs and new ideas |

---

## 🔗 Useful Links

- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [Render Documentation](https://render.com/docs)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [GSAP Documentation](https://greensock.com/docs/)

---

## 🎯 Summary

**NumberGuessBot** is a fully-featured, professional, cross-platform number guessing game that runs on **4 platforms** using a single codebase. It's perfect for learning bot development, building cross-platform applications, or just having fun!

<p align="center">
  <img src="https://img.shields.io/badge/⭐_If_you_like_this_project,_please_star_it!-FFD700?style=for-the-badge" alt="Star">
</p>

---

**Built with ❤️ by Kourosh Hamidi in Iran**

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| v7.0.0 | 2024-06-04 | Final release with all features |
| v6.0.0 | 2024-05-28 | Added duels & shop |
| v5.0.0 | 2024-05-27 | Added web version |
| v4.0.0 | 2024-05-26 | Added Bale support |
| v3.0.0 | 2024-05-25 | Added leaderboard |
| v2.0.0 | 2024-05-24 | Added coins & shop |
| v1.0.0 | 2024-05-23 | Initial release |

---

<p align="center">
  <a href="#-numberguessbot--نابغهباز">
    <img src="https://img.shields.io/badge/🔝_Back_to_Top-2E86AB?style=for-the-badge" alt="Back to top">
  </a>
</p>
```
