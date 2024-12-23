import matplotlib.pyplot as mp

date = ['25/12', '26/12', '27/12']
temp = [8.5, 10.5, 6.8]


mp.plot(date, temp, marker='o')
mp.title("Temperature over Days")

mp.xlabel("Date ------>")

mp.ylabel("Temperature (°C)------->") 
mp.grid(True) 
mp.show()
