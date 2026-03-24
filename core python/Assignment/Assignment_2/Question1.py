# Convert the time entered in hh,min and sec into seconds. 

hours = int(input('Enter the hours:'))
minutes = int(input('Enter the minutes:'))
seconds = int(input('Enter the seconds:'))

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print(f'Total time in seconds is: {total_seconds}')