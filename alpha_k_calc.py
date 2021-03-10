#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from sklearn.linear_model import LinearRegression



model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)
print('slope:', model.coef_)
