# Test Cases for Recommender

1. Normal execution
    
        Input: python3 recommendation_system.py "video_details.csv" "Anaconda 1 full movie"
        Output: List of Recommendations

2. Relevant recommendation - topic wise
   
        Input: python3 recommendation_system.py "video_details.csv" "15 Business Books Everyone Should Read"
        Output: List of Book related videos

3. Relevant recommendation - text wise
   
        Input: python3 recommendation_system.py "video_details.csv" "Taylor Swift - The Man (Official Video)"
        Output: List of videos including music videos by different artists

4. No input provided
   
        Input: python3 recommendation_system.py
        Output: No video title and/or dataset passed as command line arguments!
        Terminating Program...

5. Wrong dataset provided 
   
        Input: python3 recommendation_system.py "xyz"
        Output: Error! Database of videos not found!
        ---------------------
        Python resulted in error: [Errno 2] File xyz does not exist: 'xyz'
        Terminating Program...
        
6. Video passed as input does not exist in database

        Input: python3 recommendation_system.py "video_details.csv" "adz says hi"
        Output: Error! Video not found!
        Terminating Program...

7. Less than ten recommendations returned

        Input: python3 recommendation_system.py "test_videos.csv" "15 Business Books Everyone Should Read"
        Output: List of 7 recommendations

8. No recommendations returned
   
        Input: python3 recommendation_system.py "zero_rec.csv" "15 Business Books Everyone Should Read"
        Output: Error! No recommendations found!
        Terminating Program...

9.  Failure to preprocess - video atrributes mismatch 
  
        Input: python3 recommendation_system.py "att_mismatch.csv" "15 Business Books Everyone Should Read"
        Output: Error! Preprocessing failed - attribute mismatch!
        Terminating Program...
        
10. 