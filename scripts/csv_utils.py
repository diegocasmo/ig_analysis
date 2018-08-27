#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, os

def save_as_csv(data, file_path):
  '''
  Create .csv file from data
  '''
  try:
    create_csv(file_path)
    write_to_csv(data, file_path)
    print('Successfully created \'{}\''.format(file_path))
  except Exception as e:
    print('Unable to create CSV file \'{}\': {}'.format(file_path, str(e)))

def write_to_csv(data, file_path):
  '''
  Write data to a .csv file
  '''
  output = csv.writer(open(file_path, 'w'))
  output.writerow(data[0].keys()) # Header row
  for row in data:
    output.writerow(row.values()) # Values row

def create_csv(file_path):
  '''
  Create .csv file in the specified file path
  '''
  if not os.path.exists(os.path.dirname(file_path)):
    try:
      os.makedirs(os.path.dirname(file_path))
    except OSError as exc: # Guard against race condition
      if exc.errno != errno.EEXIST:
        raise
