"""
Exercise Description
    Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
argument for this parameter will be the number of seconds to be translated into the number of hours,
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don't show it: the
function should return '10m' rather than '0h 10m 0s'. The only exception is that
getHoursMinutesSeconds(0) should return '0s'.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
"""
def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return f"{totalSeconds}s"
    
    ans = []
    data =""
    hours = int(int(totalSeconds/60)/60)
    if (hours != 0 ):
        totalSeconds -= (hours * 60 * 60) 
        ans.append(f'{hours}h')
        
    min = int(totalSeconds/60)
    if (min != 0 ):
        totalSeconds -= (min * 60)
        ans.append(f'{min}m')
    
    if totalSeconds != 0:
        ans.append(f'{totalSeconds}s')
    for i in range(len(ans)):
        if ans[i] in ["0h","0m","0s"]:
            continue
        else:
            if i == 3 or i == 0:
                data += f'{ans[i]}'
            else:
                data += f' {ans[i]}'
    return(data)
    

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'

# this version give ny chatgpt is 100 times better thanmine

def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"
    
    ans = []
    hours = totalSeconds // 3600
    if hours:
        ans.append(f"{hours}h")
    totalSeconds %= 3600

    minutes = totalSeconds // 60
    if minutes:
        ans.append(f"{minutes}m")
    totalSeconds %= 60

    if totalSeconds:
        ans.append(f"{totalSeconds}s")

    return ' '.join(ans)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'

# and here is the authors version

def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s':
    if totalSeconds == 0:
        return '0s'

    # Set hours to 0, then add an hour for every 3600 seconds removed from
    # totalSeconds until totalSeconds is less than 3600:
    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600

    # Set minutes to 0, then add a minute for every 60 seconds removed from
    # totalSeconds until totalSeconds is less than 60:
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60

    # Set seconds to the remaining totalSeconds value:
    seconds = totalSeconds

    # Create an hms list that contains the string hour/minute/second amounts:
    hms = []
    # If there are one or more hours, add the amount with an 'h' suffix:
    if hours > 0:
        hms.append(str(hours) + 'h')
    # If there are one or more minutes, add the amount with an 'm' suffix:
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    # If there are one or more seconds, add the amount with an 's' suffix:
    if seconds > 0:
        hms.append(str(seconds) + 's')

    # Join the hour/minute/second strings with a space in between them:
    return ' '.join(hms)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'