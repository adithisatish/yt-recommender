# Documentation for the Recommendation System

Refer to ```recommendation_system.py```. The recommender calculates similarity and relevance based on multiple factors: 
- Title of video - done using cosine similarity and TfIdf vectorization
- Views
- Likes
- Dislikes (negative influence)

Therefore, the above parameters are a must in the database. 

A composite score factoring in every feature mentioned above is calculated and the 10 video titles, with the highest score is displayed. This can further be used to refer to the video entry in the database and display thumbnail for the same. 

### Functioning:
As of now, the the ```recommender``` function needs to be called after importing the file. Input passed to the function must be the link of the video that is currently playing. 

### To Do:
Include option for user to give feedback on each recommendation, and incorporate that into the recommender. 