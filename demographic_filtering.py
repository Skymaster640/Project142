import pandas as pd
import numpy as np

df = pd.read_csv("articles.csv")

def find_total_events(df1_row):
  total_likes = df[(df["contentId"] == df1_row["contentId"]) & (df["eventType"] == "LIKE")].shape[0]
  total_views = df[(df["contentId"] == df1_row["contentId"]) & (df["eventType"] == "VIEW")].shape[0]
  total_bookmarks = df[(df["contentId"] == df1_row["contentId"]) & (df["eventType"] == "BOOKMARK")].shape[0]
  total_follows = df[(df["contentId"] == df1_row["contentId"]) & (df["eventType"] == "FOLLOW")].shape[0]
  total_comments = df[(df["contentId"] == df1_row["contentId"]) & (df["eventType"] == "COMMENT CREATED")].shape[0]
  return total_likes + total_views + total_bookmarks + total_follows + total_comments

df["total_events"] = df.apply(find_total_events, axis=1)

df.head()

df = df.sort_values(['total_events'],ascending=[False])

output = df