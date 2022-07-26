# all imports

import pandas as pd
import time
import datetime

lines = []
with open('lyrics.txt') as f:
    lines = f.readlines()

# set up dataframe
df = pd.DataFrame(columns=['timeStamp', 'lyrics'])
print(df)


# increment to line
count = 0
for line in lines:
    count += 1
    #print(f'line {count}: {line}')
    timeStamp = line[line.find("[")+1:line.find("]")]
    lyrics = line[10:]
    df.loc[len(df.index)] = [timeStamp, lyrics]
    # store in data frame
