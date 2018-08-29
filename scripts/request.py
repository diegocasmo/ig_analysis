#!/usr/bin/env python
# -*- coding: utf-8 -*-

def do_paginated_request(api, method, json_key):
  '''
  TODO: Document
  '''
  arr = []
  next_max_id = True
  while next_max_id:
    if next_max_id is True:
      next_max_id = ''

    method(api.username_id, maxid=next_max_id)
    arr.extend(api.LastJson.get(json_key, []))
    next_max_id = api.LastJson.get('next_max_id', '')

  return arr
