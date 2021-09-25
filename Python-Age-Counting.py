"""
Python Age Counting
In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER. Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.

Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2

"""



import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# print(len(r.json()['data']))

response_data = r.json()['data'].split(",")

count = 0
for data in response_data:
  split_data = data.split("=")
  if split_data[0].strip() == "age" and int(split_data[1]) >= 50:
    count += 1

print(count)
