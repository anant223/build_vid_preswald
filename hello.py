from preswald import text, table, get_df
import pandas as pd
import plotly.express as px


# Add a title
text("# Electric_Vehicle_Population_Data")

# Load and display data
df = pd.read_csv("./data/Electric_Vehicle_Population_Data.csv")


table(df)

# Clean and prepare columns if needed
df.columns = df.columns.str.strip()  # remove whitespace
df.dropna(subset=['Model', 'City', 'Electric Utility', 'Electric Range'], inplace=True)

# Remove extra whitespace
df['Model'] = df['Model'].str.replace(r'\s+', ' ', regex=True)

# Strip leading/trailing whitespace again just in case
df['Model'] = df['Model'].str.strip()

# 1. Total number of vehicles
total_vehicles = len(df)
text(f"Total vehicles : {total_vehicles}")
# 2. Total number of unique makes & models
unique_makes = df['Make'].nunique()
unique_models = df['Model'].nunique()
text(f"Unique Models : {unique_models}")
text(f"Unique Makes : {unique_models}")

# 3. Top 5 car models by count
top_models = df['Model'].value_counts().head(5)
text(f"Top 5 card models by count : {top_models}")

# 4. Average electric range of all vehicles
avg_range = df['Electric Range'].mean()
text(f"Average Electric range : {avg_range}")
# 5. City with the most EVs registered
top_city = df['City'].value_counts().idxmax()
top_city_count = df['City'].value_counts().max()
text(f"City with the most EVs : {top_city} - {top_city_count}")

# 6. Number of TESLA vehicles
tesla_count = len(df[df['Make'].str.upper() == 'TESLA'])
text(f"Number of TESLA : {tesla_count}")

# 7. Number of vehicles eligible under CAFV
eligible_cafv = df[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible']
eligible_count = len(eligible_cafv)
text(f"Eligible Under CAFV : {eligible_cafv}")

# 8. Top 3 Electric Utilities by number of vehicles
top_utilities = df['Electric Utility'].value_counts().head(3)
text(f"Top Utilities : {top_utilities}")




