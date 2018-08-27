#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, pdb
from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
load_dotenv()
from csv_utils import save_as_csv

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

  # Create .csv files of user's data
  dir_name = '{}-{}'.format(api.username, username_id)
  for file_name, data in datasets.items():
    file_path = r'data/{}/{}.csv'.format(dir_name, file_name)
    save_as_csv(data, file_path)
