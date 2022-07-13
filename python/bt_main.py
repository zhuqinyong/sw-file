import _thread,machine,utime

# uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))  # 正常模式
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(16), rx=machine.Pin(17))  # 正常模式
# uart = machine.UART(0, baudrate=38400, tx=machine.Pin(0), rx=machine.Pin(1)) # 正常模式
# uart = machine.UART(0, baudrate=38400, tx=machine.Pin(0), rx=machine.Pin(1)) # AT模式
# uart = machine.UART(0, baudrate=115200, tx=machine.Pin(0), rx=machine.Pin(1)) #

print(uart)
ATNAME = "AT+NAME=AAAA\r\n"
ATROLE = "AT+ROLE=2\r\n"
all_io_L = [0xAA, 0xfc, 0xff, 0xff, 0xe7, 0xf0, 0x00]  # 此指令功能为将所有蓝牙模块核心内OUT引脚设置为高电平
UARTFLAG = False  # 判断蓝牙模块是否初始化完成标志位


def uart_reader_thread():
    global a
    while True:
        if uart.any():
            cmd = uart.readline().decode()
            print(cmd)
        else:
			utime.sleep(0.8)
        


def start_new_thread():
    _thread.start_new_thread(uart_reader_thread, ())


# 配置串口向蓝牙模块写命令
def initUART():
    print(uart)
    start_new_thread()  # 启用一条专门用于读数据的线程
    machine.Pin(25, machine.Pin.OUT).value(0)  # 配置开始前板载LED灭
    utime.sleep(1)
    uart.write(ATNAME)  # 使用AT命令写入组网名
    utime.sleep(1)
    uart.write(ATROLE)
    # uart.write("T+MADDR22\r\n")
    # utime.sleep(1)
    uart.write("AT+ROLE?\r\n")
    utime.sleep(1)
    uart.write("AT+HELP\r\n")
    utime.sleep(1)
    uart.write("AT+RESET\r\n")  # AT命令重启蓝牙模块
    utime.sleep(1)


# uart.write(bytes(all_io_H))  # 拉高电平
# uart.write(bytes(all_io_L))  # 拉低蓝牙模块5个端口的电平
machine.Pin(25, machine.Pin.OUT).value(1)  # 配置完成点亮板载LED

# initUART()  # 初始化串口
# initUART()
start_new_thread()

