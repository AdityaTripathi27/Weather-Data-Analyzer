
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\hp\Downloads\archive\Weather Data.csv"
df = pd.read_csv(file_path)

print("****\nOriginal Data: ****")

df["Date/Time"] = pd.to_datetime(
    df["Date/Time"], errors="coerce"
)

df = df.drop_duplicates()
df = df.dropna()

df.columns = df.columns.str.strip()
df["Weather"] = df["Weather"].str.strip()

print(df.info())
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df.head())

print(df.describe())

averages = df.mean(numeric_only=True)

print("Average of all numerical columns:")
print(averages)

frequency = df["Weather"].value_counts()

percentage = df["Weather"].value_counts(normalize=True) * 100

result = pd.DataFrame({
    "Frequency": frequency,
    "Percentage": percentage.round(2)
})

print(result)

# Weather frequency graph (Top 10)
plt.figure(figsize=(12, 6))
frequency.head(10).plot(kind="bar")

plt.title("Top 10 Most Frequent Weather Conditions")
plt.xlabel("Weather Condition")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Convert numerical columns to numeric
df["Temp_C"] = pd.to_numeric(df["Temp_C"], errors="coerce")
df["Visibility_km"] = pd.to_numeric(
    df["Visibility_km"], errors="coerce"
)

# Calculate daily averages
daily = (
    df.set_index("Date/Time")
    .resample("D")[["Temp_C", "Visibility_km"]]
    .mean()
)

# Temperature and visibility trend graphs
fig, ax = plt.subplots(2, 1, figsize=(12, 9))

# Temperature trend
ax[0].plot(
    daily.index,
    daily["Temp_C"],
    label="Daily Average Temperature"
)
ax[0].plot(
    daily.index,
    daily["Temp_C"].rolling(7, min_periods=1).mean(),
    label="7-Day Average"
)
ax[0].set_title("Temperature Trend During 2012")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Temperature (°C)")
ax[0].legend()
ax[0].grid(True, alpha=0.3)

# Visibility trend
ax[1].plot(
    daily.index,
    daily["Visibility_km"],
    label="Daily Average Visibility"
)
ax[1].plot(
    daily.index,
    daily["Visibility_km"].rolling(7, min_periods=1).mean(),
    label="7-Day Average"
)
ax[1].set_title("Visibility Trend During 2012")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Visibility (km)")
ax[1].legend()
ax[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# -----------------------------------
# Scatter Plot 1: Weather vs Temperature
# -----------------------------------

plt.figure(figsize=(14, 6))

sns.scatterplot(
    data=df,
    x="Weather",
    y="Temp_C",
    alpha=0.5
)

plt.title("Weather vs Temperature")
plt.xlabel("Weather Condition")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -----------------------------------
# Scatter Plot 2: Weather vs Visibility
# -----------------------------------

plt.figure(figsize=(14, 6))

sns.scatterplot(
    data=df,
    x="Weather",
    y="Visibility_km",
    alpha=0.5
)

plt.title("Weather vs Visibility")
plt.xlabel("Weather Condition")
plt.ylabel("Visibility (km)")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -----------------------------------
# Correlation Heatmap
# -----------------------------------

# Select numerical columns only
correlation = df.select_dtypes(include="number").corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap of Weather Data")
plt.tight_layout()
plt.show()
