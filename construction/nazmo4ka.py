#Sky-Sharks код для приёма сигнала
#21.02.2025


import serial
import time

com_port = 'COM4'
baud_rate = 9600  
timeout = 1
#channel_command = "10 A1\n"       


try:

    #set(channel_command.encode('ascii'))
    #print(f"Команда '{channel_command.strip()}' отправлена.")

    ser = serial.Serial(com_port, baud_rate, timeout=timeout,)
    print(f"Порт {com_port} вскрыт.")
except serial.SerialException as e:
    print(f"Ошибка открытия порта {com_port}: {e}")
    exit()


try:
    while True:
        if ser.in_waiting > 0:
            
            hex_data = ser.read(ser.in_waiting).hex()
            time.sleep(0)
            ascii_data = bytes.fromhex(hex_data).decode('ascii', errors='ignore')
            print(f"ASCII: {ascii_data}")

except KeyboardInterrupt:
    print("Остановка работы.")

finally:
    ser.close()
    print(f"Порт {com_port} закрыт.")

















 

