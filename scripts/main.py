#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json, pdb

from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
load_dotenv()

from csv_utils import save_as_csv
from followers import get_total_followers
from following import get_total_following
from feed import get_total_feed

if __name__ == '__main__':
  # Get user API
  api = InstagramAPI(os.getenv('IG_USERNAME'), os.getenv('IG_PASSWORD'))
  api.login()

  # Get user's data
  datasets = {
    'followers': get_total_followers(api),
    'following': get_total_following(api),
    'feed': get_total_feed(api)
  }

  # Create .csv files of user's data
  dir_name = '{}-{}'.format(api.username, api.username_id)
  for file_name, data in datasets.items():
    file_path = r'data/{}/{}.csv'.format(dir_name, file_name)
    save_as_csv(data, file_path)
