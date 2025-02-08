# Соревнование [CompTech 2025](https://comptech.nsu.ru/)
### Направление - классический ML
1 место на [лидерборде](https://www.codabench.org/competitions/5504/?secret_key=dd48e468-6a08-40e4-9158-16508cb590fd#/results-tab)

![Screenshot from 2025-02-08 14-33-29](https://github.com/user-attachments/assets/869e8d04-95f7-42b4-8b0b-b7d8b34c8a92)

Анализ данных (количественный, EDA), обработка данных (удаление и замена "странных" значений, генерация фич)

Дообучение трансформера; лучший результат - distilbert-base-uncased

Чат-бот собирает данные и дает вердикт (данные передаются в локально развернутую дообученную модель, подкачанную с [HuggingFace](https://huggingface.co/Gnider/kompt_distil_v1))
Скрипт бота в telegram_bot.py
