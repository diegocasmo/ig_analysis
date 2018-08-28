#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pdb
import datetime as dt
from collections import Counter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from dotenv import load_dotenv
load_dotenv()

def get_user_dataframes():
  '''
  Read in .csv files of the user's data
  '''
  folder_name = os.getenv('FOLDER_NAME')
  dir_name = r'../data/{}'.format(folder_name)

  followers_df = pd.read_csv('{}/followers.csv'.format(dir_name))
  followers_df = followers_df.replace(np.nan, '', regex=True)

  following_df = pd.read_csv('{}/following.csv'.format(dir_name))
  following_df = following_df.replace(np.nan, '', regex=True)

  feed_df = pd.read_csv('{}/feed.csv'.format(dir_name))
  feed_df = feed_df.replace(np.nan, '', regex=True)

  return (followers_df, following_df, feed_df)

def print_num_of_followers(followers_df):
  '''
  Print the number of followers a user has
  '''
  print('The user has {} followers'.format(len(followers_df)))

def print_no_follow_back_accounts(followers_df, following_df):
  '''
  Print the number of accounts that do not follow the user back, plus their usernames
  '''
  following = following_df['username'].values
  followers = followers_df['username'].values
  no_follow_back = set(following) - set(followers)
  print('{} account(s) do not follow the user back\n'.format(len(no_follow_back)))
  print('The no follow-back accounts are: \n\n{}'.format(', '.join(list(no_follow_back))))

def render_top_n_items_summary(feed_df, sort_by='likes_count', n=5, ascending=False):
  '''
  Render the top-'n' most popular mosts based on 'sort_by'
  '''
  feed_df = feed_df.sort_values(sort_by, ascending=ascending)
  for i in range(n):
    row = feed_df.iloc[i]
    plt.imshow(io.imread(row['thumbnail_url']))
    plt.show()
    print('{} likes'.format(row['likes_count']))
    print(row['text'])

def print_like_count_average(df):
  '''
  Print the 'likes_count' average across the entire data frame
  '''
  like_count_average = df.loc[:, 'likes_count'].mean()
  return 'The average like count is {} per post'.format(int(round(like_count_average)))

def render_top_n_items_statistics(feed_df, sort_by='likes_count', n=5, ascending=False):
  '''
  Render multiple statistics about the top-'n' posts based on the 'sort_by' key
  # TODO: Split into multiple methods
  '''
  feed_df = feed_df.sort_values(sort_by, ascending=ascending)

  days = []
  times = []
  hashtags = []
  words = []
  for i in range(n):
    row = feed_df.iloc[i]
    date = dt.datetime.fromtimestamp(row['taken_at'])
    days.append(date.strftime('%A'))

    times.append(date.strftime('%H:00'))
    for hashtag in get_hashtags(row['text']):
        hashtags.append(hashtag)

    # TODO: Remove stop words
    for word in row['text'].split(' '):
        words.append(word)

  top_days = Counter(days).most_common(3)
  top_times = Counter(times).most_common(3)
  top_hashtags = Counter(hashtags).most_common(3)
  top_words = Counter(words).most_common(3)

  render_pie_chart(top_days, 'What days was the most liked content posted?')
  render_pie_chart(top_times, 'What time were the posts most frequently made? (0:00-24:00)')
  render_pie_chart(top_hashtags, 'What are the most popular hash-tags?')
  render_pie_chart(top_words, 'What words were most frequently used?')

  # Recommend user to create more posts like this if sorted as ascending
  if ascending == False:
    msg = 'It is thus recommended to post on {} around {} o\'clock using the hash-tags \'{}\' and words \'{}\'.'.format(
            ', '.join([x[0] for x in top_days]),
            top_times[0][0],
            ', '.join([x[0] for x in top_hashtags]),
            ', '.join([x[0] for x in top_words]))
    print(msg)

def render_pie_chart(tuple_list, title):
  '''
  Given a list of tuples of the form [(label, size)], render a pie chart with the specified title
  '''
  labels = [x[0] for x in tuple_list]
  sizes = [x[1] for x in tuple_list]

  fig1, ax = plt.subplots()
  ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
  ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
  ax.set(title=title)
  plt.show()

def get_hashtags(text):
  '''
  Return a list of hash-tags found in a text
  '''
  return [x for x in text.split() if x.startswith("#")]
