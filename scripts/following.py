#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_total_following(api):
  '''
  Return accounts followed by the current user
  '''
  return api.getTotalSelfFollowings()
