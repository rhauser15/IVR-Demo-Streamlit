import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

#Plotting map data
map_data = pd.DataFrame(
    np.random.randn(100, 2) * [37,95] + [0, 0],
    columns=['lat', 'lon'])

gaus_data = pd.DataFrame(
    np.random.randn(10000000),
    columns=['lat'])
