# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import pandas as pd
import json
from pprint import pprint


# %%
# Testing api and json call to store data
# API Reference https://api.collegefootballdata.com/api/docs/?url=/api-docs.json#/
url = 'https://api.collegefootballdata.com/'
test_url = 'https://api.collegefootballdata.com/records?year=2020&team=texas%20a%26m&conference=sec'


# %%
test_get = requests.get(test_url).json()


# %%
pprint(test_get)


# %%
second_test = url + ''


