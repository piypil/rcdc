* XSS - Cross-Site Scripting
* Межсайтовый скриптинг

В основе XSS атаки лежит внедрение зловредного скрипта или сценария в веб приложение, которое на стороне клиента выполняет зловредные действия в браузере пользователя.

XSS атаки классифицируются по 3 основным признакам:
- Хранимые (Stored) XSS (код перед выполнением храниться в базе данных)
- Отраженные (Reflected) XSS (код не храниться в базе данных, а отражается от сервера)
- DOM-Based XSS (код одновременно храниться и выполняется в браузере)

Что может злоумышленник `->`
1. Злоумышленник может попытаться получить креды ("credentials") пользователя и войти в его аккаунт.
2. Злоумышленник может перенаправить пользователя на поддельную страницу и украсть cookies.
3. Многое другое

Как можно внедрить код ? Код можно внедрить через поля ввода `->` форма ввода комментария, форма логина и пароля, форма заполнения информации о твоей бывшей (или …). `(o-_-o)`
