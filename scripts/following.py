#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standardizer import build_user
from logger import log

def get_total_following(api):
  '''
  Return accounts followed by the current user
  '''
  log('Requesting user total following...')
  api.getTotalSelfFollowings()
  users = api.LastJson['users']

  # Format following data
  following = []
  for user in users:
    following.append(build_user(user))

  return following
