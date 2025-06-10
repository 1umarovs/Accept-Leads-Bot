import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = "7069007752:AAGVcziYBJFDG6hNOLYRwXk4X9pzFiUQc3g"
GROUP_CHAT_ID = -1002373701968

bot = telebot.TeleBot(BOT_TOKEN)


devclub_courses = {
    "💻 Kompyuter savodxonligi": "Ushbu kurs kompyuterdan samarali foydalanishni o‘rgatadi.",
    "🎨 Frontend dasturlash": "Frontend kursida HTML, CSS, JavaScript va ReactJS o‘rgatiladi.",
    "🖥 Backend dasturlash": "Backend kursida Python, Django va REST API texnologiyalari o‘rgatiladi.",
    "🌐 Fullstack dasturlash": "Fullstack kursida frontend va backend texnologiyalarining barcha asoslari o‘rgatiladi.",
    "📱 Mobil dasturlash": "Mobil dasturlash kursida Flutter va Dart texnologiyalari o‘rgatiladi."
}


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("📋 Kursga ro‘yxatdan o‘tish", "📞 Administrator bilan bog‘lanish")


user_data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    print(f"Received /start from {message.chat.id}")
    bot.send_message(
        message.chat.id,
        "Salom! 👋 Men DevClub IT Akademiyasi botiman.\n\nBu yerda siz kurslar haqida ma’lumot olishingiz yoki ro‘yxatdan o‘tishingiz mumkin.",
        reply_markup=main_menu
    )

@bot.message_handler(func=lambda message: message.text == "📋 Kursga ro‘yxatdan o‘tish")
def register_course(message):
    print(f"User {message.chat.id} started registration")
    markup = InlineKeyboardMarkup()
    for course in devclub_courses.keys():
        markup.add(InlineKeyboardButton(course, callback_data=f"course_{course}"))
    bot.send_message(message.chat.id, "Kursni tanlang:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
def process_course(call):
    course = call.data.replace("course_", "")
    chat_id = call.message.chat.id
    print(f"User {chat_id} selected course: {course}")

    user_data[chat_id] = {'course': course}

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("7:00 - 12:00", callback_data="7-12"))
    markup.add(InlineKeyboardButton("13:00 - 18:00", callback_data="13-18"))
    bot.send_message(call.message.chat.id, "Qulay vaqtni tanlang:", reply_markup=markup)
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data in ["7-12", "13-18"])
def process_time(call):
    time = call.data
    user_data[call.message.chat.id]['time'] = time
    print(f"User {call.message.chat.id} selected time: {time}")

    bot.send_message(call.message.chat.id, "Iltimos, ismingizni kiriting:")
    bot.register_next_step_handler(call.message, process_name)

def process_name(message):
    name = message.text
    user_data[message.chat.id]['name'] = name 
    print(f"User {message.chat.id} entered name: {name}")
    bot.send_message(message.chat.id, "Yoshingizni kiriting:")
    bot.register_next_step_handler(message, process_age)

def process_age(message):
    age = message.text
    user_data[message.chat.id]['age'] = age 
    print(f"User {message.chat.id} entered age: {age}")
    bot.send_message(message.chat.id, "Telefon raqamingizni kiriting:")
    bot.register_next_step_handler(message, process_phone)

def process_phone(message):
    phone = message.text
    user_data[message.chat.id]['phone'] = phone 
    print(f"User {message.chat.id} entered phone: {phone}")


    name = user_data.get(message.chat.id, {}).get('name', 'Unknown')
    age = user_data.get(message.chat.id, {}).get('age', 'Unknown')
    phone = user_data.get(message.chat.id, {}).get('phone', 'Unknown')
    time = user_data.get(message.chat.id, {}).get('time', 'Unknown')
    course = user_data.get(message.chat.id, {}).get('course', 'Unknown')

    summary = (f"Ma’lumotlaringiz:\n"
               f"👤 Foydalanuvchi: {name}\n"
               f"🎂 Yosh: {age}\n"
               f"📞 Telefon: {phone}\n"
               f"📚 Kurs: {course}\n"
               f"🕓 Vaqt: {time}\n")
    
    bot.send_message(message.chat.id, summary)
    

    bot.send_message(GROUP_CHAT_ID, summary)
    
    bot.send_message(message.chat.id, "🎉 Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz! Tez orada administratorlarimiz siz bilan bog‘lanadi.")

bot.polling(none_stop=True)


@bot.message_handler(func=lambda message: message.text == "📞 Administrator bilan bog‘lanish")
def contact_admin(message):
    print(f"User {message.chat.id} requested admin contact")
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Adminstrator", url="https://t.me/umarovs_17"))
    bot.send_message(message.chat.id, "Qo‘shimcha savollar uchun administrator bilan bog‘laning:\n📞 Telefon: +998 77 000 19 40", reply_markup=markup)

bot.polling(none_stop=True)
