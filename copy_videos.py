import pandas as pd 
import numpy as np 

data = pd.read_csv("video_details.csv")
copy_data = data.head(8)

copy_data.to_csv("test_videos.csv")
print(copy_data['Video Title'].head(8))