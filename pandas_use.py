import pandas as pd
df1 = pd.DataFrame({
    "Name": ["a", "b", "c"],
    "Roll": [1, 2, 3],
    "Attendance": [90, 85, 88]
})
df2 = pd.DataFrame({
    "Name": ["d", "e"],
    "Roll": [4, 5],
    "Marks": [75, 88]
})
df=pd.merge(df1, df2, on=["Roll", "Name"],how="outer")
print(df)