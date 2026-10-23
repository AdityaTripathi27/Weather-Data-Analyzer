# 🌦️ Weather Data Analysis Using Python

## 📌 Project Overview

The **Weather Data Analysis** project focuses on analyzing historical weather data using Python and its popular data analysis and visualization libraries. The project explores weather conditions, temperature, visibility, and relationships between numerical weather variables.

Using **Pandas, Matplotlib, and Seaborn**, the dataset is cleaned, processed, analyzed, and visualized to identify patterns and trends in weather conditions throughout the year.

This project is suitable for beginners who want to develop practical skills in Python, data analysis, data cleaning, and data visualization.

## 🎯 Project Objectives

- Load and explore a real-world weather dataset.
- Clean the dataset by handling missing values and duplicate records.
- Convert date and time information into a proper datetime format.
- Generate descriptive statistics for numerical columns.
- Calculate the average values of numerical weather variables.
- Analyze the frequency and percentage of different weather conditions.
- Visualize temperature and visibility trends over time.
- Explore relationships between weather conditions, temperature, and visibility.
- Use a correlation heatmap to understand relationships between numerical variables.

## 🛠️ Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data cleaning, manipulation, and analysis |
| Matplotlib | Creating graphs and charts |
| Seaborn | Statistical data visualization |
| NumPy | Numerical computing and array operations |
| VS Code | Code development and execution |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Weather-Data-Analysis/
│
├── README.md
├── weather_analysis.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Weather Data.csv
│
└── images/
    ├── weather_frequency.png
    ├── temperature_visibility_trend.png
    ├── weather_vs_temperature.png
    ├── weather_vs_visibility.png
    └── correlation_heatmap.png
```

*Note: The folder and image names above are suggested. Update them to match your actual repository. You can omit the dataset from GitHub if you prefer to provide a download link instead.*

## 📊 Dataset Information

The project uses a historical weather dataset named `Weather Data.csv`.

The dataset contains hourly weather observations for the year 2012 and includes the following columns:

| Column Name | Description |
|---|---|
| `Date/Time` | Date and time of the weather observation |
| `Temp_C` | Temperature in degrees Celsius |
| `Dew Point Temp_C` | Dew point temperature in degrees Celsius |
| `Rel Hum_%` | Relative humidity in percentage |
| `Wind Speed_km/h` | Wind speed in kilometres per hour |
| `Visibility_km` | Visibility in kilometres |
| `Press_kPa` | Atmospheric pressure in kilopascals |
| `Weather` | Recorded weather condition |

## 🔍 Data Cleaning and Preprocessing

The following preprocessing steps are performed:

1. **Load the dataset:** Read the CSV file using Pandas.
2. **Convert date and time:** Convert the `Date/Time` column into a datetime format.
3. **Remove duplicates:** Remove duplicate rows to avoid repeated records.
4. **Handle missing values:** Remove rows containing missing values.
5. **Clean column names:** Remove unnecessary spaces from column names.
6. **Clean weather labels:** Remove extra spaces from weather-condition values.
7. **Convert numerical columns:** Ensure relevant columns use numerical data types for analysis.
8. **Inspect the data:** Review dataset information, missing values, duplicate records, and sample rows.

These steps help prepare the data for accurate analysis and visualization.

## 📈 Exploratory Data Analysis (EDA)

### 1. Descriptive Statistics

The `describe()` function is used to calculate statistical measurements such as:

- Mean
- Standard deviation
- Minimum and maximum values
- Quartiles
- Count of observations

The average of each numerical column is also calculated to understand the overall weather characteristics.

### 2. Weather Condition Frequency Analysis

A frequency analysis identifies the most common weather conditions in the dataset.

The project calculates:
- Frequency of each weather condition.
- Percentage contribution of each weather condition.
- Top 10 most frequently recorded weather conditions.

A bar chart is used to compare the most common conditions.

### 3. Temperature Trend Analysis

Daily average temperatures are calculated by grouping hourly observations by date.

A line chart displays:
- Daily average temperature.
- Seven-day rolling average temperature.

The rolling average helps smooth short-term fluctuations and makes broader temperature patterns easier to observe.

### 4. Visibility Trend Analysis

Daily average visibility is calculated and visualized over time.

The graph includes:
- Daily average visibility.
- Seven-day rolling average visibility.

This helps examine changes in visibility throughout the year.

### 5. Weather Condition vs Temperature

A scatter plot compares weather conditions with recorded temperatures.

It helps explore how temperature values vary across different weather categories.

### 6. Weather Condition vs Visibility

A scatter plot compares weather categories with visibility measurements.

It helps explore how visibility varies across recorded weather conditions.

### 7. Correlation Heatmap

A correlation heatmap visualizes the correlation coefficients between numerical weather variables.

The heatmap includes numerical variables such as:

- Temperature
- Dew point temperature
- Relative humidity
- Wind speed
- Visibility
- Atmospheric pressure

Correlation coefficients range from **-1 to +1**:

- **+1:** Perfect positive linear correlation.
- **0:** No linear correlation.
- **-1:** Perfect negative linear correlation.

The heatmap helps identify potentially related variables. However, correlation does not prove causation.

## 💻 Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version
- Visual Studio Code or another Python IDE
- pip package manager

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/Weather-Data-Analysis.git
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository name.

### Step 2: Navigate to the Project Folder

```bash
cd Weather-Data-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, run:

```bash
pip install pandas matplotlib seaborn numpy
```

### Step 4: Configure the Dataset Path

Place the CSV file in the `data` folder and update your Python code to use a relative path:

```python
file_path = "data/Weather Data.csv"
df = pd.read_csv(file_path)
```

Make sure the path matches the actual location and filename of your dataset.

### Step 5: Run the Project

```bash
python weather_analysis.py
```

The program will display data summaries and generate visualizations.

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
pandas
matplotlib
seaborn
numpy
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## 📋 Expected Results

After running the project, you should be able to:

- Understand the structure and quality of the weather dataset.
- Identify the most frequently recorded weather conditions.
- Examine daily and smoothed temperature trends.
- Analyze visibility changes over time.
- Compare temperature and visibility across weather categories.
- Identify correlations between numerical weather variables.

The project produces statistical summaries and multiple visualizations that make the dataset easier to understand.

## 🚀 Future Improvements

Possible enhancements include:

- Add interactive visualizations using Plotly.
- Create a dashboard using Streamlit.
- Perform monthly and seasonal weather comparisons.
- Analyze relationships between humidity, wind speed, and temperature.
- Add a correlation analysis report.
- Build a machine learning model to predict temperature or classify weather conditions.
- Export the analysis results and charts into a PDF report.

## 🎓 Learning Outcomes

Through this project, I practiced:

- Python programming for data analysis.
- Pandas DataFrame operations and data cleaning.
- Handling datetime data and resampling time series.
- Calculating descriptive statistics and percentages.
- Creating bar charts, line charts, and scatter plots.
- Using rolling averages to study trends.
- Building a correlation heatmap with Seaborn.
- Organizing a data analysis project for GitHub.

## 👨‍💻 Author

**Aditya Tripathi**

B.Tech in Artificial Intelligence and Machine Learning

Interested in Python, Data Analysis, Machine Learning, and Artificial Intelligence.

## ⭐ Acknowledgements

Thanks to the dataset provider for making historical weather data available for analysis.

If you find this project useful, feel free to star the repository!
