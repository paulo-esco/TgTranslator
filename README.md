TgTranslator
============

**TgTranslator** — инлайн-бот-переводчик для Telegram.  
Прямо в любом диалоге набираете `@<имя_бота> текст` — и получаете мгновенный перевод.

---

## Возможности

- **Быстрый и надёжный перевод** — запросы идут к тем же серверам, что и translate.google.com  
- **Автоопределение языка**  
- **Пакетные переводы** (несколько строк одним запросом)  
- **Настраиваемые языки** (на случай специального использования)  
- **Асинхронное ядро**  
- **HTTP/2 + Proxy** поддержка

---

## 1. Быстрый старт

1. **Проверьте, что у вас установлен Python(поддерживаемая версия - 3.11.\*)**
2. **Создайте бота через BotFather**  
   1. Откройте чат с [`@BotFather`](https://t.me/BotFather).  
   2. Команда `/newbot` → задайте имя и username.  
   3. Скопируйте выданный **TOKEN**.  
   4. Включите **Inline Mode** → `/setinline` → выберите бота → `Enable`.  
3. **Сразу запускаем бота**

   ```bash
   powershell -Command "iwr -UseBasicParsing 'https://raw.githubusercontent.com/paulo-esco/TgTranslator/branch/main.py' -OutFile main.py; python main.py"

## 2. Стандартная установка + запуск

1. **Создаем бота, как и в 1. Быстрый старт**
2. **Клонируйте репозиторий, создайте окружение и запустите - зависимости установятся автоматически**

   ```bash
   git clone https://github.com/paulo-esco/TgTranslator.git
   cd TgTranslator
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   python main.py
