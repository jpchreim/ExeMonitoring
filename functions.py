import wmi
def checkStatus():
    #Initalizing the wmi 
    f = wmi.WMI()
    running_Status = False
    print("Let's start checking")
    #Loop through all process
    #We would be using the WMI.Win32_Process function in order to get the list of running processes on the system
    for process in f.Win32_Process():
        if "JAVA.exe" in process.Name:
            running_Status = True
    print("Current ", running_Status)