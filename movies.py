import pandas as pd

ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')

ratings['timestamp'] = pd.to_datetime(ratings['timestamp'],unit='s')
ratings['hour'] = ratings.timestamp.dt.hour

tags['timestamp'] = pd.to_datetime(tags['timestamp'],unit='s')
tags['hour'] = tags.timestamp.dt.hour

rating_counts = ratings[['userId', 'rating']].groupby('userId').count()
tag_counts = tags[['userId', 'tag']].groupby('userId').count()


users = rating_counts.join(tag_counts, on='userId')

users.plot.scatter(x='rating',y='tag')
