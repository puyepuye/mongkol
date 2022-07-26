import datetime
import time
timeStampString = '00:15.15'
after_Dot = (timeStampString[6:])
x = time.strptime(timeStampString.split('.')[0], '%M:%S')
seconds = datetime.timedelta(
    hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
milliseconds = (seconds*1000) + (int(after_Dot)*10)

#df.iloc[i]['timeStamp'] = seconds
print(milliseconds)
