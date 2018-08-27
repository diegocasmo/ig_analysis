#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def create_csv_file(data, file_name = 'data'):
  '''
  Create .csv file from the passed data
  TODO: Create user folder within the data folder (username or user_id?)
  '''
  # Create .csv file
  file_path = r'data/{}.csv'.format(file_name)
  output = csv.writer(open(file_path, 'w'))

  # Append data to .csv file
  output.writerow(data[0].keys()) # Header row
  for row in data:
    output.writerow(row.values()) # Values row
