import datetime
import winsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%H:%M %p"))
    
    altime = altime[11:-3]
    
    
    Mireal = altime[3:5]
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break

