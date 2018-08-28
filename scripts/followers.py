#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standardizer import build_user
from logger import log

def get_total_followers(api):
  '''
  Return current user's followers
  '''
  log('Requesting user total followers...')
  api.getTotalSelfFollowers()
  users = api.LastJson['users']

  # Format followers data
  followers = []
  for user in users:
    followers.append(build_user(user))

  return followers
