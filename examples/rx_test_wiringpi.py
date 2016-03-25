
import time

try:
    from libwiringpi.wiringpi import *
except ImportError:
    import sys
    sys.path.append('..')
    from libwiringpi.wiringpi import *


PIN_IRQ = 6
PIN_SDN = 5


global ItStatus1, ItStatus2
irq_flag = 0
g_u8SendFrame = 0


def si443x_readRegister(regAddr):
    data_buffer = bytes([regAddr, 0xFF])
    wiringPiSPIDataRW(0, data_buffer, 2)
    return data_buffer[1]


def si443x_writeRegister(regAddr, value):
    data_buffer = bytes([regAddr | 0x80, value])
    wiringPiSPIDataRW(0, data_buffer, 2)

    
def pin_irq_isr_handle():
    global irq_flag, ItStatus1, ItStatus2
    
    irq_flag = 1
    
    ItStatus1 = si443x_readRegister(0x03)
    ItStatus2 = si443x_readRegister(0x04)
    print('isr handle %02X - %02X' %(ItStatus1, ItStatus2))

    if (ItStatus1 & 0x01) == 0x01:
        si443x_writeRegister(0x08, 0x02)
        si443x_writeRegister(0x08, 0x00)
        print("CRC Error interrupt occured!!!\n")
        irq_flag = 0

    if (ItStatus1 & 0x02) == 0x02:
        payload = [0] * 10
        
        print("Recv low event detect for pin irq\n")
        si443x_writeRegister(0x07, 0x01)			
        length = si443x_readRegister(0x4B)
        if length <= 10:
            for temp8 in range(length):
                payload[temp8] = si443x_readRegister(0x7F)

            print("Recv data ok\n")
            for temp8 in range(length):
                print("payload[%d]:0x%x  " % (temp8, payload[temp8]))
                if temp8 != 0:
                    payload[0] ^= payload[temp8]
                
            print("\nRecv Data XOR value:0x%x\n"% payload[0])
            print("\n\n")

        si443x_writeRegister(0x08, 0x02)					
        si443x_writeRegister(0x08, 0x00)				
        si443x_writeRegister(0x07, 0x05)			

        irq_flag = 0


def rasp_gpio_init():
    global PIN_IRQ, PIN_SDN
    wiringPiSetup()
    pinMode(PIN_IRQ, INPUT)
    pullUpDnControl(PIN_IRQ, PUD_UP)
    wiringPiISR(PIN_IRQ, INT_EDGE_FALLING, pin_irq_isr_handle)
    pinMode(PIN_SDN, OUTPUT)


def si443x_sendData():
    global irq_flag, ItStatus1, ItStatus2, g_u8SendFrame 
    
    si443x_writeRegister(0x07, 0x01)			

    print("Send data beginning......\n")
	
    g_u8SendFrame += 1			 																				
    if g_u8SendFrame > 255:
        g_u8SendFrame = 0
    si443x_writeRegister(0x3E, 8)			
    si443x_writeRegister(0x7F, 0x42)
    si443x_writeRegister(0x7F, 0x55)
    si443x_writeRegister(0x7F, 0x54)
    si443x_writeRegister(0x7F, 0x54)
    si443x_writeRegister(0x7F, 0x4F)
    si443x_writeRegister(0x7F, 0x4E)
    si443x_writeRegister(0x7F, g_u8SendFrame)
    si443x_writeRegister(0x7F, 0x0D)		

    si443x_writeRegister(0x05, 0x04)	
    si443x_writeRegister(0x06, 0x00)
    ItStatus1 = si443x_readRegister(0x03)	
    ItStatus2 = si443x_readRegister(0x04)

    si443x_writeRegister(0x07, 0x09)

    while irq_flag == 0:
        pass
    irq_flag = 0

    print("low event detect for pin irq-send interrupt\n")
    
    ItStatus1 = si443x_readRegister(0x03)
    ItStatus2 = si443x_readRegister(0x04)


    time.sleep(0.01)  

    print("Send data ended!\n")
			
    si443x_writeRegister(0x05, 0x03)	
    si443x_writeRegister(0x06, 0x00) 
    ItStatus1 = si443x_readRegister(0x03)
    ItStatus2 = si443x_readRegister(0x04) 
    si443x_writeRegister(0x07, 0x05)	   


def si443x_sendTest():
    global irq_flag, ItStatus1, ItStatus2, PIN_SDL
    
    print("Initialize the si443x ISM chip.\n")

    digitalWrite(PIN_SDN, LOW)
    time.sleep(0.15)
    ItStatus1 = si443x_readRegister(0x03)	
    ItStatus2 = si443x_readRegister(0x04)	
 
    si443x_writeRegister(0x07, 0x80)

    while irq_flag == 0:
        pass
    irq_flag = 0

    print("low event detect for pin irq-1\n")
    ItStatus1 = si443x_readRegister(0x03)			
    ItStatus2 = si443x_readRegister(0x04)		

#    while irq_flag == 0:
#        pass
#    irq_flag = 0
#
#    print("low event detect for pin irq-2\n")
#	  
#    ItStatus1 = si443x_readRegister(0x03)			
#    ItStatus2 = si443x_readRegister(0x04)			

    si443x_writeRegister(0x75, 0x53)		
    si443x_writeRegister(0x76, 0x64)		
    si443x_writeRegister(0x77, 0x00)

    si443x_writeRegister(0x2a, 0x14)
    si443x_writeRegister(0x6E, 0x09)		
    si443x_writeRegister(0x6F, 0xd5)		
    si443x_writeRegister(0x70, 0x2C)
    
    si443x_writeRegister(0x72, 0x38)	

    si443x_writeRegister(0x1C, 0x1b)	
    si443x_writeRegister(0x21, 0xc0)						
    si443x_writeRegister(0x22, 0x13)					
    si443x_writeRegister(0x23, 0xa9)				
    si443x_writeRegister(0x24, 0x00)			
    si443x_writeRegister(0x25, 0x03)		
    si443x_writeRegister(0x1D, 0x40)	
    si443x_writeRegister(0x1E, 0x0A)
    si443x_writeRegister(0x2A, 0x14)
					
    si443x_writeRegister(0x34, 0x0A)		
    si443x_writeRegister(0x35, 0x2A)	

    si443x_writeRegister(0x33, 0x02)
	
    si443x_writeRegister(0x36, 0x2D)
    si443x_writeRegister(0x37, 0xD4)

    si443x_writeRegister(0x30, 0x8D)
    si443x_writeRegister(0x32, 0x00)
    si443x_writeRegister(0x71, 0x63)
								
    si443x_writeRegister(0x0C, 0x15)
    si443x_writeRegister(0x0b, 0x12)

    si443x_writeRegister(0x09, 0xD7)
    si443x_writeRegister(0x69, 0x60)
	 
    si443x_writeRegister(0x6d, 0x1e)
    si443x_writeRegister(0x07, 0x05)
    si443x_writeRegister(0x05, 0x03)
    si443x_writeRegister(0x06, 0x00)

    ItStatus1 = si443x_readRegister(0x03)
    ItStatus2 = si443x_readRegister(0x04)
    	    
    si443x_writeRegister(0x07, 0x05)		
    si443x_writeRegister(0x0d, 0xf4)

    while True:
        print("Loop wait...!!!\n")
        
        #si443x_sendData()
        
        if irq_flag == 1:
            irq_flag = 0

        time.sleep(5)



if __name__ == '__main__':
    import faulthandler
    faulthandler.enable(open('si443xtest_fault.log', 'a'))
    wiringPiSPISetup(0, 500000)
    rasp_gpio_init()
    si443x_sendTest()
    

    
