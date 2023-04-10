def add_time(start, duration, weekday=''):

  new_time = ''
  n_day = 0
  
  # Split the string so you have hours and Timezone separatly
  current_time = start.split(' ')

  # Split the hours and the duration
  time = current_time[0].split(':')
  duration_split = duration.split(':')

  # Convert the time and duration_split to int
  time = [int(i) for i in time]
  duration_split = [int(i) for i in duration_split]

  # Covert time[1] from 12h format to 24
  if current_time[1] == 'PM':
    time[0] = time[0] + 12

  # Calculate the hour and minute and save the difference in days
  time[0] = time[0] + (time[1] + duration_split[1]) // 60
  time[1] = (time[1] + duration_split[1]) % 60
  n_day = (time[0] + duration_split[0]) // 24
  time[0] = (time[0] + duration_split[0]) % 24

  # Translate time[0] to PM or AM
  # Transform time[0] 24 hors format intro 12 hours format
  if time[0] > 12:
    current_time[1] = 'PM'
    time[0] = time[0] % 12
  elif time[0] < 12:
    current_time[1] = 'AM'
  else:
    current_time[1] = 'PM'

  # time[0] = 0 case
  if time[0] == 0:
    time[0] = 12

  # Covert time back to str
  time = [str(x) for x in time]

  # Convert the minutes that are less than 10 to 0x format
  if int(time[1]) // 10 == 0:
    time[1] = '0'+ time[1]
  
  # Calculate the weekdays
  if weekday == '':
    if n_day == 0:
      new_time = str(':'.join(time) + ' ' + current_time[1])
    elif n_day == 1:
      new_time = str(':'.join(time) + ' ' + current_time[1] + ' (next day)')
    else:
      new_time = str(':'.join(time) + ' ' + current_time[1] + ' (' + str(n_day) + ' days later)')
  else:
    weekday = weekday.lower().capitalize()
    days_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    new_weekday = days_of_week[(weekdays[weekday] + n_day) % 7]
    if n_day == 0:
      new_time = str(':'.join(time) + ' ' + current_time[1] + ', ' + new_weekday)
    elif n_day == 1:
      new_time = str(':'.join(time) + ' ' + current_time[1] + ', ' + new_weekday +' (next day)')
    else:
      new_time = str(':'.join(time) + ' ' + current_time[1] + ', ' + new_weekday +' (' + str(n_day) + ' days later)')
  
  
  return new_time