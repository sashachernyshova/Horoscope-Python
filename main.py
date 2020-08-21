import telebot;
bot = telebot.TeleBot('1253833567:AAGiWnXTpDTtnnuqLC8_X83Un0ebLrDvoGs');
import random


dict_zodiacs = {1: 'Aries', 2:'Taurus', 3:"Gemini", 4:"Cancer", 5: "Leo", 6: "Virgo", 7: "Libra", 8: "Scorpio",
                9: "Sagittarius", 10: "Capricorn", 11: "Aquarius", 12: "Pisces"}


first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello, I am going to predict your horoscope")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "write 'Hello'")
    else:
        bot.send_message(message.from_user.id, "I do not understand. Write /help.")

    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in dict_zodiacs.keys():
    # key_aries = telebot.types.InlineKeyboardButton(text='Aries', callback_data='zodiac')
        keyboard.add(telebot.types.InlineKeyboardButton(text=str(dict_zodiacs[i]), callback_data='zodiac'))
    bot.send_message(message.from_user.id, text='Choose your sign', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
  if call.data == "zodiac":
    msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
    bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
