import threading
import time

start = time.time() #access the start timestamp
people = 500

def action(num):
    global people
    while people > 0:
        people -= 50
        print("车辆编号：{}, 当前车站人数：{}".format(num,people))
        time.sleep(1) #1 sec sleep

num = 1
vehicle = threading.Thread(target=action, args=(num,)) #instantiate a thread

vehicle.start()
vehicle.join()
end = time.time() #access the end timestamp
duration = end - start
print("Duration time %0.8f" %(duration))



