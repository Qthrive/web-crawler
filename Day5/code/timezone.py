import time

local_timezone = time.tzname

print('本地时区名称:',local_timezone)

offset = -time.timezone if(time.localtime().tm_isdst == 0) else -time.altzone
print('本地时区偏移量：(s)',offset)