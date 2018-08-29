#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_user(user = {}):
  '''
  Build a user dictionary using a standard notation
  '''
  return {
    'pk': user['pk'],
    'username': user['username'],
    'full_name': user['full_name'],
    'is_private': user['is_private']
  }

def build_post(item = {}):
  '''
  Build a post dictionary using a standard notation
  '''
  try:

    post = {
      'id': item['id'],
      'pk': item['pk'],
      'media_type': item['media_type'],
      'text': item['caption']['text'] if 'caption' in item and item['caption'] != None else '',
      'taken_at': item['taken_at'],
      'likers': [],
      'likes_count': 0,
      'comments': [],
      'comments_count': 0
    }

    if item['media_type'] == 8:
      post['thumbnail_url'] = item['carousel_media'][0]['image_versions2']['candidates'][0]['url']
    else:
      post['thumbnail_url'] = item['image_versions2']['candidates'][0]['url']

    return post
  except Exception as e:
    print('\n\n')
    print(item)
    print(str(e))
    print('\n\n')

def build_comment(comment = {}):
  '''
  Build a comment dictionary using a standard notation
  '''
  # Merge comment attributes with its user attributes
  return {
    **build_user(comment['user']),
    ** {
      'text': comment['text'],
      'created_at': comment['created_at']
    }
  }
