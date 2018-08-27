#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_total_feed(api):
  '''
  Return current user feed (posts) and meta-data related to them
  '''
  return api.getTotalSelfUserFeed()
