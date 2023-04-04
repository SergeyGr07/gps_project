import serial

# Указываем имя COM-порта и скорость передачи данных
ser = serial.Serial('COM4', 9600)

# Отправляем сообщение в COM-порт
ser.write(b'Hello, world!')

# Закрываем соединение
ser.close()
