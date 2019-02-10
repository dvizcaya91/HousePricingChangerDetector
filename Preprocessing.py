# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Preprocessing
#
# #### The preprocessing will be carried out using three different approaches in order to compare how easy it is to work with each of them. The three tools will be Pandas, pySpark and Dask.

# ## Data

# The data is located in two different tables of a MySQL DB. One table has the propertoes of the house while the other has the pricing historic, one row each the price of the house changed.

import MySQLdb as mdb
from db_credentials import *

con = mdb.connect(HOST, USER, PWD, DB, charset='utf8')


