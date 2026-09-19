# Geo Area Classifier

An interactive Streamlit and Folium application for analyzing a user-selected geographic region using OpenStreetMap data.

## Features

- Interactive map centered on the Delhi region
- Draw polygons or rectangles directly on the map
- Calculate selected polygon area, perimeter, and bounds
- Retrieve OpenStreetMap land-use features with OSMnx
- Analyze natural features within the selected area
- Analyze waterways within the selected area
- Calculate category distributions
- Identify dominant land-use, natural-feature, and waterway categories

## How It Works

1. Open the application.
2. Draw a polygon or rectangle on the interactive map.
3. The application captures the selected geometry.
4. Shapely is used to analyze the geometry.
5. OSMnx queries OpenStreetMap features within the selected region.
6. The application summarizes the returned features and reports dominant categories.

## Run Locally

```bash
git clone <YOUR_REPOSITORY_URL>
cd geo-area-classifier

python -m venv .venv
pip install -r requirements.txt

streamlit run app.py
```

## Technologies

Python · Streamlit · Folium · Streamlit-Folium · OSMnx · GeoPandas ecosystem · Shapely · OpenStreetMap

## Notes

OSM feature availability depends on the selected region and OpenStreetMap coverage. Large polygons can result in slower OSM queries.
