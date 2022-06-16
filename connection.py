import subprocess,bluetooth,pyautogui
# Setting up connection
passkey="1234"
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# Pass your host ip and port as argument
sock.connect(("PS:YO:UR:HO:ST:IP",1))



# Core Code
while 1:
    x=sock.recv(1024)
    print(x)
    x=x.decode()
    if x=="w":
        pyautogui.keyUp("a")
        pyautogui.keyUp("s")
        pyautogui.keyUp("d")
        pyautogui.keyDown("w")
    elif x=="a":
        pyautogui.keyUp("w")
        pyautogui.keyUp("s")
        pyautogui.keyUp("d")
        pyautogui.keyDown("a")
    elif x=="s":
        pyautogui.keyUp("a")
        pyautogui.keyUp("w")
        pyautogui.keyUp("d")
        pyautogui.keyDown("s")
    elif x=="d":
        pyautogui.keyUp("a")
        pyautogui.keyUp("s")
        pyautogui.keyUp("w")
        pyautogui.keyDown("d")
    elif x=="q":
        pyautogui.keyUp("d")
        pyautogui.keyUp("s")
        pyautogui.keyDown("w")
        pyautogui.keyDown("a")
    elif x=="e":
        pyautogui.keyUp("a")
        pyautogui.keyUp("s")
        pyautogui.keyDown("w")
        pyautogui.keyDown("d")
    elif x=="z":
        pyautogui.keyUp("d")
        pyautogui.keyUp("w")
        pyautogui.keyDown("s")
        pyautogui.keyDown("a")
    elif x=="c":
        pyautogui.keyUp("a")
        pyautogui.keyUp("w")
        pyautogui.keyDown("d")
        pyautogui.keyDown("s")        
