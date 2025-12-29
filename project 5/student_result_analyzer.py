import pandas as pd
import numpy as np

# Load data
data = {
    "Name": ["Atif", "Wasil", "Ayan", "AMan", "Kazafi"],
    "Maths": [78, 45, 88, 32, 67],
    "Science": [85, 50, 92, 40, 72],
    "English": [74, 48, 90, 38, 65]
}

df = pd.DataFrame(data)

# Calculate average
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Pass / Fail
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

# Grade system
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

print("\n📊 Student Result Analysis\n")
print(df)

# Topper
topper = df.loc[df["Average"].idxmax()]
print("\n🏆 Topper:")
print(topper[["Name", "Average", "Grade"]])
