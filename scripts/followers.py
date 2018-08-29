#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standardizer import build_user
from logger import log
from request import do_paginated_request

def get_total_followers(api):
  '''
  Return current user's followers
  '''
  log('Requesting user total followers...')

  followers = []
  users = do_paginated_request(api, api.getUserFollowers, 'users')
  for user in users:
    followers.extend([build_user(user)])

  return followers
