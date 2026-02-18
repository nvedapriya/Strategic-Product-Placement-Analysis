import pandas as pd
import numpy as np

# Visualization (optional but useful)
import matplotlib.pyplot as plt

# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Evaluation
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("C:\Users\VEDA PRIYA\OneDrive\Desktop\Product Placement Analysis\Product Positioning.csv")

# Display first rows
df.head()
