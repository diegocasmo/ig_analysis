#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_total_followers(api):
  '''
  Return current user's followers
  '''
  return api.getTotalSelfFollowers()
