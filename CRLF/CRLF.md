**CR and LF**


CR и LF это управляющие символы которые можно использовать для обозначения разрыва строки в текстовых файлах.


- CR = Возврат каретки (Carriage Return) (\r, 0x0D в шестнадцатеричной, 13 в десятичной системе счисления) — перемещает курсор в начало строки, не переходя на следующую строку.
- LF = Перевод строки (Line Feed) (\n, 0x0A в шестнадцатеричной, 10 в десятичной системе счисления — перемещает курсор на следующую строку, не возвращаясь в начало строки.)


Преобразуем их в вид для URL:
```
CR — %0d
LF — %0a
```

CR, за которым сразу следует LF (CRLF, \r\n, или 0x0D0A) перемещает курсор на следующую строку и затем перемещает его в начало строки.


Когда пользователь (Браузер) отправляет запрос веб серверу, запрос разделяться на две части.


1. Это HTTP заголовок
2. HTML ответ (Информация с сайта)


Веб сервер использует символы CRLF чтобы понять где идет это разделение на Заголовок и полезную информацию с сайта.


**CRLF-инъекция (CRLF Injection)**
