#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standardizer import build_user
from logger import log
from request import do_paginated_request

def get_total_following(api):
  '''
  Return accounts followed by the current user
  '''
  log('Requesting user total following...')

  following = []
  users = do_paginated_request(api, api.getUserFollowings, 'users')
  for user in users:
    following.extend([build_user(user)])

  return following
