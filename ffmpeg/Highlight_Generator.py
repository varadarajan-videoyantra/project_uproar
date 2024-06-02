# import csv
import re
import subprocess
import shlex
import pandas as pd

df = pd.read_csv('../prediction.csv')
df = df[['Audio ID', 'Finalprediction']]
newdf = df.query('Finalprediction == 1')
# print(newdf)
val_list = newdf["Audio ID"].tolist()
fval_list = []

for x in val_list:
    fval_list.append(re.findall(r'\d+', x))
segment_list = []
filter_list = []
for x in fval_list:
    segment_list.append("-i Video_Segments/AV_Segment_" + x[0] + ".mp4")
for i in range(len(segment_list)):
    filter_list.append("[" + str(i) + ":" + "0" + "]" " [" + str(i) + ":" + "1" + "]")
command = " ffmpeg " + str(segment_list) + " -filter_complex " + "\"" + str(filter_list) + " concat=n=" + str(
    len(segment_list)) + ":v=1:a=1 [v] [a]" + "\"" + " -map " + "\"" + "[v]" + "\"" + " -map " + "\"" + "[a]" + "\"" + " highlights.mp4"
command = command.replace("['","").replace("']","").replace("'","").replace(",","")
print(command)
subprocess.run(shlex.split(command))

