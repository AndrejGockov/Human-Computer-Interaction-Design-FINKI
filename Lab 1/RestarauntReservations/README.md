# Restaurant Reservations

Django апликација за менаџирање на ресторани и резервации

Креирајте Django апликација за менаџирање на ресторани и нивни резервации. Секоја резервација се карактеризира со датум и време, број на гости, посебни барања (текст), ресторан, корисник кој ја направил резервацијата, статус на резервацијата (Потврдена, Во чекање, Откажана) и вкупна проценета цена. За секој ресторан се чуваат: име на ресторанот, адреса, краток опис, кујна (тип на храна), слика и максимален капацитет. За секој тип на кујна се чува: името на кујната, земја на потекло, кратко опишување и дали е моментално во тренд (boolean).

Сите модели треба да се регистрираат во админ панелот.

Во админ панелот треба да биде овозможено филтрирање на резервации според нивниот статус. При додавање на нова резервација, полето за корисник не треба да се пополнува рачно, туку системот автоматски да го зачува корисникот кој е во моментот најавен во системот.

Django application for managing restaurants and reservations

Create a Django application for managing restaurants and their reservations. Each reservation is characterized by a date and time, number of guests, special requests (text), restaurant, the user who made the reservation, reservation status (Confirmed, Pending, Cancelled), and total estimated price. For each restaurant, store: restaurant name, address, short description, cuisine (food type), image, and maximum capacity. For each cuisine type, store: cuisine name, country of origin, short description, and whether it is currently trending (boolean).

All models should be registered in the admin panel.

In the admin panel, filtering of reservations by their status should be enabled. When adding a new reservation, the user field should not be filled manually; instead, the system should automatically save the user who is currently logged into the system.