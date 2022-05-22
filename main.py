from msilib.schema import AppId
import time
from win10toast_click import ToastNotifier 
import os

water = 0
print(f"no water so far :(")
def increment():
    global water
    water = water + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"You have drank {water} glasses of water today.")


#main loop
while True:
    toaster = ToastNotifier()
    toaster.show_toast(title="Drink What Africans Can't Get!",
                       msg=f"You have drank {water} glasses of water today.", 
                       callback_on_click=lambda: increment(), 
                       threaded=True, duration=10, 
                       icon_path="C:\\Users\harsh\\Documents\\Python Projects\\water\\water.ico")
    time.sleep(3600)
