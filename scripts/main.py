#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, pdb
from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
load_dotenv()
from create_csv import create_csv_file

if __name__ == '__main__':
  # Get user API
  api = InstagramAPI(os.getenv('IG_USERNAME'), os.getenv('IG_PASSWORD'))
  api.login()
  username_id = api.username_id

  # Get user's data
  datasets = {
    'followers': api.getTotalFollowers(username_id),
    'following': api.getUserFollowings(username_id),
    'feed': api.getTotalUserFeed(username_id)
  }

  # Create a .csv file of user's data
  for file_name, data in datasets.items():
    create_csv_file(data, file_name)
