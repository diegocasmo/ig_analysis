#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

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

def build_post(post = {}):
  '''
  Build a post dictionary using a standard notation
  '''
  return {
    'id': post['id'],
    'pk': post['pk'],
    'media_type': post['media_type'],
    'thumbnail_url': post['image_versions2']['candidates'][0]['url'],
    'text': post['caption']['text'],
    'taken_at': post['taken_at'],
    'likers': [],
    'likes_count': 0,
    'comments': [],
    'comments_count': 0
  }

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
