time = int(input('Введите время в секундах:'))
hour = int(time/3600)
minute = int((time - hour * 3600)/60)
sec = time - hour * 3600 - minute * 60
print(int(hour),':',minute,':',sec)
