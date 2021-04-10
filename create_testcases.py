import pandas as pd 
import numpy as np 

data = pd.read_csv("video_details.csv")
copy_data = data.head(8)

copy_data1 = data
copy_data1 = copy_data1.rename(columns={"Likes on Video": "Likes", "Views": "Views on Video"})
no_reco = data[data['Video Title']=='15 Business Books Everyone Should Read']


copy_data.to_csv("test_videos.csv")
copy_data1.to_csv("att_mismatch.csv")
no_reco.to_csv("zero_rec.csv")