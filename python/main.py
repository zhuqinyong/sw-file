# 舵机驱动代码 SG90舵机部分
import machine, servo,utime
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=10000)
print(i2c.scan())
s = servo.Servos(i2c, address=0x40)
a=0

# 禁止状态的
#s.position(0,90)
#s.position(4,90)
#s.position(8,90)
#s.position(12,90)

s.position(2,90)
s.position(6,90)
s.position(10,90)
s.position(14,90)

#utime.sleep(1)

#s.position(2,0)
#s.position(6,0)
#s.position(10,0)
#s.position(14,0)

#utime.sleep(1)

# 四足平行状态
s.position(0,120)
s.position(4,60)
s.position(8,60)
s.position(12,120)

# 四足机器人静止动作
#(0,0)(1,90)

# pico-PCA9685

# 3v3 OUT--VCC
# GND--GND
# GPIO0--SDA
# GPIO1--SCL


# PCA 9685 接线
# 0-15为外接舵机
# 外接5V电源
# 黄色 数据
# 红色 5V



