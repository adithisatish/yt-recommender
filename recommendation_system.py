# Recommender for Video Management Platform

# The recommendation system takes the link of the video as input and returns titles of top 10 most similar videos. This is done as a combination of two methods:
# 
# - Computing similarity based on titles using TfIdf Vectorization
# - Computing a score for each video based on number of views, likes and dislikes
# 
# The latter step is necessary so that there is some standard that the videos recommeded can be held to. 
# 
# The total score is weighted and computed as 0.7 * tfidf score + 0.3 * quality score.
# 
# Note: The quality score is not static and hence cannot be computed only at the very beginning of the system's functioning. It has to be calculated everytime a request is made to the recommendation system.

# ## Importing libraries and accessing data
import pandas as pd 
import numpy as np 
import matplotlib as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# videos.head()

# ## Helper functions

def strip_views(string): # convert the string values to integers
    string = string.split(' ')[0]
    number = int(string.replace(",",""))
    return number

def strip_likes(string): # convert string values to appropriate integers
    temp = string.split(' ')[0]
    try:
        if 'K' in temp:
            temp = temp.replace("K","")
            number = int(float(temp)*1000)
        elif 'M' in temp:
            temp = temp.replace("M","")
            number = int(float(temp)*1000000)
        else:
            number = int(temp)
        return number
   
    except Exception as e:
        print(string)
        print("Error:", e)

def invert_dislikes(number): # This is to account for the decrease in quality when people dislike videos
    if number == 0:
        return number
    return -number

# ## Function to preprocess data

def preprocess(videos):
    # global videos
    try:
        videos = videos.drop(columns=["Comments"]) # dropping comments as inclusion leads to unneccesary complications
        videos = videos.dropna()
        videos = videos[videos['Likes on Video']!='LIKE'] # special case 
        videos['Views'] = videos['Views'].apply(strip_views)
        videos['Likes on Video'] = videos['Likes on Video'].apply(strip_likes)
        videos["Dislikes on Video"] = videos['Dislikes on Video'].apply(strip_likes)
        videos["Dislikes on Video"] = videos['Dislikes on Video'].apply(invert_dislikes)

        return videos
    except Exception as e:
        print("Error:", e)
        return None #exit()

def score_att(view, likes, dislikes): # to score based on quality of video
    return (likes + dislikes)/view

def recommender(link):
    videos = pd.read_csv("video_details.csv")
    videos = preprocess(videos)
    
    index = videos[videos['Video Link']==link].index.values
    # Title Similarity

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(videos['Video Title'])  
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) # cosine similarity used
    title_similarity = list(cosine_sim[index[0]]) 

    # Attribute Similarity - Views, Likes, Dislikes
    
    attributes = ['Views','Likes on Video','Dislikes on Video']
    video_att = videos[attributes]

    score = []

    for index, row in video_att.iterrows():
        score.append(score_att(row['Views'],row['Likes on Video'], row['Dislikes on Video']))
    
    # Combining Title as well as Attribute Similarity - Weighted
    similarity = enumerate([0.7*title_similarity[i] + 0.3*score[i] for i in range(len(score))])

    sim_scores = sorted(similarity, key = lambda x: x[1], reverse=True)[1:11] # Top 10 recommended
    video_titles = [i[0] for i in sim_scores]
    return videos['Video Title'].iloc[video_titles]


if __name__=='__main__':
    dataset = pd.read_csv("video_details.csv")
    recommendations = recommender("https://www.youtube.com/watch?v=imA5NPX4ucU")
    print(recommendations)

