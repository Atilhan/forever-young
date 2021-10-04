for a in range (0,25):
    if a in range (0,13):
        print ('Het is', a ,'AM')
    if a in range (12,25):
        print ('Het is ', a , 'PM')
# for variable a heeft een lijst van 0 tot 25, 
# daarbij krijgt het een if, (als) a tot 12 komt vanaf 0 tot 12, dan krijgt het een AM 
# als het vanaf 12 verder gaat tot en met 24 (25) dan krijgt het een PM 


print('----------------')


import time
while True:
    from datetime import datetime
    now = datetime.now()  
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
    time.sleep(30)



#importtime krijgt een function waarmee je secondes kunt aangeven
#met de function datetime kan je aangeven welke tijden je wilt zien , uren, secondes , dagen.
#om de 30 seconde krijg je de datum te zien.
#%s string | %d int | %f float
#https://stackoverflow.com/questions/37515587/run-a-basic-digital-clock-in-the-python-shell)


