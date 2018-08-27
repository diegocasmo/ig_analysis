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

  # Create a .csv file of the user's followers
  followers = api.getTotalFollowers(username_id)
  create_csv_file(followers, 'followers')

  # Create a .csv file of the user's following
  following = api.getUserFollowings(username_id)
  create_csv_file(following, 'following')
