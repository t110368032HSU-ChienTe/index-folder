data_folder = 'voice1'
csv_folder =  'coice1_index.csv'
save_folder = 'voice1_build'


import csv
import os
import shutil
#open CSV
with open(csv_folder, newline='') as csvfile:

    #read CsV
    rows = csv.reader(csvfile)
    #FOR LOOP
    a=-1
    b=0
    for row in rows:
    #skip the first col
        if a == -1:
            a+=1
            continue
        a+=1
        speaker_name_list = os. listdir(save_folder)
        speaker_name = row[0]
        wav_name = row[1]
        new_path_name_with_file = "{}/{}/{}".format(save_folder, speaker_name, wav_name)
        old_path_name_with_file = "{}/{}".format(data_folder, wav_name)
        if not speaker_name in speaker_name_list:
            b+=1    
        #mk folder for speaker
        os.mkdir("{}/{}".format(save_folder, speaker_name))
        #cp file in speaker folder
        shutil.copyfile(old_path_name_with_file , new_path_name_with_file)
        print ("copy {}} successful". format (wav_name), a)
        print ("wav file have {}}, speaker have {}}".format (a, b))