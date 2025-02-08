# Соревнование [CompTech 2025](https://comptech.nsu.ru/)
### Направление - классический ML
1 место на [лидерборде](https://www.codabench.org/competitions/5504/?secret_key=dd48e468-6a08-40e4-9158-16508cb590fd#/results-tab)

![Screenshot from 2025-02-08 14-33-29](https://github.com/user-attachments/assets/869e8d04-95f7-42b4-8b0b-b7d8b34c8a92)

Был проведен анализ данных (количественный, EDA), обработка данных (удаление и замена "странных" значений, генерация фич и др)

Был обучен XGBoost, а также проведено дообучение трансформера; лучший результат - дообучение трансформера distilbert-base-uncased

![Screenshot from 2025-02-08 13-55-14](https://github.com/user-attachments/assets/7e36cb42-9e0c-4182-8a77-f0338b26ba65)

Телеграмм-бот (@komptek_depression_bot) собирает данные и дает вердикт (данные передаются в локально развернутую дообученную модель, подкачанную с [HuggingFace](https://huggingface.co/Gnider/kompt_distil_v1))
Скрипт бота в telegram_bot.py
