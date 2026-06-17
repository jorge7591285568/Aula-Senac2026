import nidaqmx
import time

with nidaqmx.Task() as task:
    task.do_channels.add_do_chan("Dev1/port0/line1")
    
    value = True
    task.start()
    
    i = 1
    while i < 10:
        print(f"Valor {i}: {value}")
        time.sleep(1)
        i += 1
