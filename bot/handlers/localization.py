import re
from typing import Dict, Any

from db import User


def remove_emojis(text: str) -> str:
    """Remove emojis from the text.

    Args:
        text (str): Text to remove emojis from.

    Returns:
        str: Text without emojis.
    """
    lines = text.split('\n')
    cleaned_lines = [re.sub(r'\s*\[:\w+-?\w*\]\s*', ' ', line).strip() for line in lines]
    return '\n'.join(cleaned_lines)


def start_message(username: str | None) -> str:
    if username is None: username = "пользователь"
    return f"👋 <b>Привет, {username}!\n\n" \
           "🔸 Я помогу тебе следить за проектами на бирже Kwork и откликаться на них быстрее остальных!\n" \
           "🔸 Это увеличит шансы на то, что заказчик выберет именно тебя!\n\n" \
           "🚀 Чтобы начать, перейди в раздел «Профиль» и включи отслеживание проектов.\n" \
           "🔎 Также советуем ознакомиться с инструкцией перед использованием бота в разделе «💬 Помощь» —> «📜 Инструкция».</b>"
           
           
def no_sub() -> str:
    return "<b>⚠️ Для использования бота необходимо подписаться на наш канал!</b>"


def project_info(data: Dict[str, Any]) -> str:
    username = data['wantUserGetProfileUrl'].split('/')[-1]
    profile_url = f"https://kwork.ru/user/{username}"
    projects_url = f"https://kwork.ru/projects/list/{username}"
    
    cleaned_name = remove_emojis(data['name'])
    cleaned_description = remove_emojis(data['description'])
    
    return f"<blockquote><b>{cleaned_name}</b>\n\n" \
           f"{cleaned_description.replace('\n', '\n\n')}</blockquote>\n\n" \
           f"Желаемый бюджет: до {int(float(data['priceLimit']))} ₽\n" \
           f"Допустимый: до {int(float(data['possiblePriceLimit']))} ₽\n\n" \
           f"Покупатель: <a href='{profile_url}'>{username}</a>\n" \
           f"Размещено проектов на бирже: {data['user']['data']['wants_count']}   " \
           f"<a href='{projects_url}'>Смотреть открытые ({data['getWantsActiveCount']})</a>\n" \
           f"Нанято: {data['user']['data']['wants_hired_percent']}%\n\n" \
           f"Осталось: {data['timeLeft']}\n" \
           f"Предложений: {data['kwork_count']}"
           
           
def user_profile(user: User, username: str) -> str:
    username = username if username else "Пользователь"
    return f"👤 <b>{username}:</b>\n\n" \
           f"🏷 <b>ID:</b> <code>{user.id}</code>"
    
            
def enter_kwork_login() -> str:
    return "<b>📲 Войди в свой аккаунт Kwork, чтобы бот мог отслеживать проекты по твоим любимым категориям.</b>"


def error_login() -> str:
    return "<b>⚠️ Произошла ошибка при входе в Kwork. Введи логин и пароль еще раз.</b>"


def projects_tracking_enabled() -> str:
    return "🔔 Отслеживание проектов включено"


def projects_tracking_disabled() -> str:
    return "🔕 Отслеживание проектов выключено"


def temp_message(seconds: int) -> str:
    return f"<b>✅ Авторизация прошла успешно!</b>\n\n<i>Сообщение будет удалено через {seconds} секунд...</i>"


def help_sections() -> str:  
    return "Выбери раздел:"


def manual() -> str:
    return "<b>1.</b> На сайте kwork.ru в разделе «Биржа» выбери любимые рубрики, по ним бот будет отслеживать проекты.\n\n" \
           "<i>(❗️Важно: в настройках аккаунта Kwork должно быть выбрано «Я продавец»)</i>\n\n" \
           "<b>2.</b> Зайди в свой аккаунт Kwork через бота, введя команду /start или нажав на кнопки «Профиль» -> «Включить отслеживание проектов».\n\n" \
           "<b>3.</b> После включения отслеживания бот будет отправлять тебе проекты по выбранным рубрикам сразу после их размещения на бирже.\n\n" \
           "<i>(❗️Важно: при первом нажатии на кнопку «Открыть проект» или «Предложить услугу», необходимо зайти в свой аккаунт Kwork в открывшемся приложении)</i>"


def support() -> str:
    return "❗️Перед обращением в поддержку, проверь, нет ли ответа на твой вопрос в разделе «📜 Инструкция».\n\n" \
           "☎️ Контакт: <span class='tg-spoiler'>@kurochki_n</span>"