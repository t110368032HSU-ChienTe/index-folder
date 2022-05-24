data_folder = 'voice1'
csv_folder =  'cad_csv'
save_folder = 'voice1_vad'


import csv
import os
from pydub import AudioSegment

csv_list = os.listdir(csv_folder)
a=-1
for Csv in csv_list:
    path_csv_file = "{}/{}".format(csv_folder, Csv)
    wav_name = Csv.replace("csv","wav")
    wav_path = "{}/{}".format(data_folder, wav_name)
    
    with open(path_csv_file, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for i in rows:
            b = 0
            start_time = float(i[1])
            stop_time  = float(i[2])
            if a == -1:
                a+=1
                continue
            if i in "speech":
                b+=1
                new_wav_path_number = "{}/{}_/{}".format(save_folder,b,wav_name,)
                wav = AudioSegment.from_wav(wav_path)
                wav[1000*start_time:1000*stop_time].export(new_wav_path_number, format="wav") 



