# Recommender for Video Management Platform

A video management platform, similar to YouTube. 

### Run:
Execute ``` python recommendation _system.py <name of dataset> <title of video>```

### Feature implemented:

Refer to ```recommendation_system.py```. The recommender calculates similarity and relevance based on multiple factors: 
- Title of video - done using cosine similarity and TfIdf vectorization
- Views
- Likes
- Dislikes (negative influence)

Therefore, the above parameters are a must in the database. 

A composite score factoring in every feature mentioned above is calculated and the 10 video titles, with the highest score is displayed. This can further be used to refer to the video entry in the database and display thumbnail for the same. 

### Functioning:
An object of class ```recommendation_system``` needs to be instantiated. Following that, the ```iterative_recommender``` method needs to be called after importing the file. The dataset (as a csv) and title of video need to be passed as system arguments. Input passed to the function must be the link of the video that is currently playing. 


### Authors:

- Adithi Satish
- Manah Shetty
- Shriya Shankar