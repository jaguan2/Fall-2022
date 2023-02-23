#Jason Guan
#U9893-2926
#Program intended to calculate wind-chill temperature when inputted temp and windspeed

Temp = int(input('Enter the temperature in Fahrenheit:'))
while Temp < -58 or Temp > 41:
    Temp=int(input('Temperature must be between -58F and 41F \nPlease re-enter the temperature in Fahrenheit:'))
windSpeed = int(input('Enter the wind speed miles per hour:'))
while windSpeed <= 2:
    windSpeed =int(input('Speed must be greater than or equal to 2 \nPlease re-enter the wind speed miles per hour:'))
    
                
windChillSpeed = 35.74 + (0.6215 * Temp) - (35.75 * windSpeed ** 0.16) + (0.4275 * Temp * (windSpeed ** 0.16)) 
windChillSpeed = float(windChillSpeed)

print(f'The wind chill index is {windChillSpeed:.1f}')
