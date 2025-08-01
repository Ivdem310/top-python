"""
file 10
socket
user datagram protocol
протокол без установления соединения (нет состояния)
скорость и низкие накладные расходы
допустимы потери, но важна скорость доставки
серверу приходится определять, от кого пришло сообщение
широковещательные и мультикаст-сообщения
MTU maximum transmission unit
RTT - round trip time - время от отправки до получения
"""
"""
отличия от tcp на уровне кода
нет listen accept connect
sendto и recvfrom вместо send recv
"""
import socket

socket.settimeout(5)

"""
broadcast - всем в локалке
multicast - на группу
"""
socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#255.255.255.255

"""
методы
SOCK_DGRAM - UDP
recvfrom(1024) - получить сообщение
sendto - отправить сообщение
settimeout - установить таймаут. socket.timeout исключение

методы которых нет
listen
accept
connect
send
recv
"""

# задание 
"""
надежная отправка сообщений по UDP
udp server:
    принимает сообщения от клиента
    в сообщении UID (номер пакета)
    сервер хранит список уже полученных идентификаторов
    если UID уже получен, то игнорируем
    если новое
        печать
        отправить OK при корректности или ERROR (содержит слово ошибка) при ошибке

udp client:
    отправляет серверу 1 или более сообщений с UID например (1:Привет, ...)
    ожидает ответа
    если нет за 3 сек - повтор
    максимум 3 попытки
    если есть ответ, то измеряем и выводим время задержки
    если прислали ERROR - выводим ошибку
"""