# Project2
Веб-приложение для управления базой данных бонусных карт

Краткая визуализация выполненных требований:
1. Список полей: серия карты, номер карты, дата выпуска карты, дата окончания активности карты, дата использования, сумма, статус карты (не активирована/активирована/просрочена).
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541007537717269/image.png?width=1092&height=683)
Функционал приложения
2.1. список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541007537717269/image.png?width=1092&height=683)
2.2. поиск по этим же полям
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541008208789574/image.png?width=1089&height=681)
2.3. просмотр профиля карты с историей покупок по ней
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541008582099014/image.png?width=1089&height=681)
2.4. активация/деактивация карты/удаление карты
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541007537717269/image.png?width=1089&height=681)
2.5. Реализовать генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц". После истечения срока активности карты, у карты проставляется статус "просрочена".
![alt text](https://media.discordapp.net/attachments/726847131582857238/1050541007856476230/image.png?width=1092&height=683)

В файле settings.py указывается частота "проверки" статуса карт.