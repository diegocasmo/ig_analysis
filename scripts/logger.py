#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def log(msg):
  '''
  Print output if the verbose option is true
  '''
  if os.getenv('IS_VERBOSE') == 'True':
    print(msg)
