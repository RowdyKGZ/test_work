Я хотел создать отдельный файл для парсинга и подключать его в models.py как метод для класса TagetUrl,
а Timeshift хотел сделать в views.py что-то вроде if datetime.date.now > TageUrl.time_work
и что бы вызывался метод для парсинга и записывал в БД а потом выводить их в отдельной Views