import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load dataset
data = pd.read_csv("traffic_accidents.csv")

# Convert date/time columns
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data['Hour'] = pd.to_datetime(data['Time'], errors='coerce').dt.hour

# Drop rows with missing location
data = data.dropna(subset=['Latitude', 'Longitude'])

# ---------------------------
# 1. Weather vs Accidents
plt.figure(figsize=(8,5))
sns.countplot(x='Weather', data=data, order=data['Weather'].value_counts().index)
plt.title("Accidents by Weather Condition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------
# 2. Road Condition vs Accidents
plt.figure(figsize=(8,5))
sns.countplot(x='Road_Condition', data=data, order=data['Road_Condition'].value_counts().index)
plt.title("Accidents by Road Condition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------
# 3. Time of Day Pattern
plt.figure(figsize=(10,5))
sns.histplot(data['Hour'], bins=24, kde=True)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# ---------------------------
# 4. Accident Hotspots Map using Folium
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=3,
        color='red',
        fill=True,
        fill_opacity=0.6
    ).add_to(m)

m.save("accident_hotspots_map.html")
print("✅ Accident hotspot map saved as 'accident_hotspots_map.html'")
