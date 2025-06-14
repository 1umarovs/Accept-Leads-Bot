# 🤖 Accept-Leads-Bot

This is a custom **Telegram bot** developed for **DevClub IT Academy** to automate student registration for various IT courses. The bot interacts with users, collects their details, and sends the information to the group administrators.

---

## 📌 Key Features

- Displays a list of available courses for selection.
- Asks users to choose their preferred time slot.
- Collects name, age, and phone number.
- Sends the collected data to a Telegram group using `GROUP_CHAT_ID`.
- Includes a button to contact the administrator directly.

---

## 🎯 Supported Courses

- 💻 Computer Literacy
- 🎨 Frontend Development (HTML, CSS, JS, React)
- 🖥 Backend Development (Python, Django, REST API)
- 🌐 Fullstack Development
- 📱 Mobile App Development (Flutter, Dart)

---

## 🛠 Technologies Used

- `Python 3`
- `pyTelegramBotAPI` (`telebot`)
- Telegram Bot API

---

## ⚙️ How It Works

1. User sends the `/start` command to begin.
2. Bot shows available courses → user selects time → enters name → age → phone number.
3. Bot gathers all info and sends a formatted summary to a Telegram group.
4. Confirms registration to the user with a success message.

---



## 🧑‍💻 Author

**Muhammadyusuf Umarov**  
📍 Andijan, Uzbekistan  
📬 Telegram: [@umarovs_17](https://t.me/umarovs_17)

---

## 📅 About the Project

- 🛠 Developer: Muhammadyusuf Umarov  
- 📆 Created in: **2024**  
- 🎯 Purpose: Automate course registration and streamline data collection for DevClub

---


## 📦 Getting Started

```bash
git clone https://github.com/1umarovs/Accept-Leads-Bot.git
cd Accept-Leads-Bot
pip install pyTelegramBotAPI
python bot.py
