# Project: What Makes a Popular Song
Contributors: Gianna Barletta, Sophie Lefebvre, Grace Michael, Preston Reep & Dachuan Zhang

### General Project Goals:
- Analyze similarities between songs to determine what makes a popular song
  - Using Top 40 Streamed Songs of 2020
  - Using Spotify data on each song: Genre, duration (in milliseconds), danceability, etc
- Analyze the relationship between streams and highest billboard position
- Determine which song is the “best” popular song by comparing average length, most repeated words, etc. and seeing which song is closest to these parameters

### Significance:
- The analysis above will help to show what trends in songwriting and production create songs that are most successful streaming-wise
- This project will determine the building blocks for a popular song today
- Based on the analysis of our parameters, we determined which song from the Top 40 Streamed Songs of 2020 most closely represents the “popular song formula”

### General Methodology:
- Analyze similarities between songs to determine what makes a popular song
  - Specific repeated words: Word Cloud
  - Length of lines 
  - Length of choruses 
- Analyze the relationship between streams and highest billboard position
  - Heatmap of billboard positions in relation to above stats
  - Weight the peak positions to scatter-plot vs the number of streams
- Using the above parameters, determine which song best meets the “most popular” criteria - ie median length of lines, choruses, most common words, etc
  - Bell curve plot
- Look at Spotify data on those songs and analyze trends (from Kaggle dataset)
  - Genre, duration (in milliseconds), danceability, etc.


### Data Sources:
We used these sources to build our own csv and txt files
- Top 40 Streamed Songs of 2020: https://www.officialcharts.com/chart-news/the-official-top-40-biggest-songs-of-2020__29264/ 

- Using these songs, find the lyrics on: https://www.musixmatch.com/ 

- Additional song information: https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data.csv
