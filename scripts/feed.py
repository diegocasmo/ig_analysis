#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standardizer import build_post, build_user, build_comment
from logger import log

def get_total_feed(api):
  '''
  Return current user feed (posts) and meta-data related to them
  '''
  log('Requesting user feed...')
  api.getTotalSelfUserFeed()
  items = api.LastJson['items']

  # Format feed data
  feed = []
  for item in items:
    post = build_post(item)
    post['likers'] = get_media_likers(api, post['id'])
    post['comments'] = get_media_comments(api, post['id'])
    feed.append(post)

  return feed

def get_media_likers(api, media_id):
  '''
  Return a media's likes
  '''
  log('Requesting media {} likers...'.format(media_id))
  api.getMediaLikers(media_id)
  likers = api.LastJson['users']
  return [build_user(x) for x in likers]

def get_media_comments(api, media_id):
  '''
  Return a media's comments
  '''
  log('Requesting media {} comments...'.format(media_id))
  api.getMediaComments(media_id)
  comments = api.LastJson['comments']
  return [build_comment(x) for x in comments]
