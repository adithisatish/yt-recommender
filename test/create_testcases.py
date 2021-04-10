import pandas as pd 
import numpy as np 
import random
import os

path = '/'.join(os.getcwd().split('\\')[:-1]) + "/data/"
# print(path)

data = pd.read_csv(path + "video_details.csv")

# titles = list(data['Video Title'])
# print(titles[random.randrange(0,len(titles)-1)])
copy_data = data.head(8)

copy_data1 = data
copy_data1 = copy_data1.rename(columns={"Likes on Video": "Likes", "Views": "Views on Video"})
no_reco = data[data['Video Title']=='15 Business Books Everyone Should Read']


copy_data.to_csv(path + "test_videos.csv")
copy_data1.to_csv(path + "att_mismatch.csv")
no_reco.to_csv(path + "zero_rec.csv")