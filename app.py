import streamlit as st
import folium
import osmnx as ox

from folium.plugins import Draw
from streamlit_folium import st_folium
from shapely.geometry import shape


st.title("Geo Area Classifier")

st.write(
    "Draw a polygon on the map to analyze the selected region."
)


m = folium.Map(
    location=[28.6139, 77.2090],
    zoom_start=8
)

Draw(
    export=True,
    draw_options={
        "polygon": True,
        "rectangle": True,
        "circle": False,
        "marker": False,
        "polyline": False,
        "circlemarker": False
    },
    edit_options={
        "edit": True,
        "remove": True
    }
).add_to(m)

output = st_folium(
    m,
    width=1000,
    height=600
)

if output["last_active_drawing"]:

    st.success("Polygon Captured!")


    geometry = output["last_active_drawing"]["geometry"]

    polygon=shape(geometry)

    st.subheader("Polygon Statistics")

    st.write("Area (square degrees):")
    st.write(polygon.area)

    st.write("Perimeter:")
    st.write(polygon.length)

    st.write("Bounds:")
    st.write(polygon.bounds)

    if polygon.area > 1:

        st.warning(
            "Large area selected. OSM queries may take time."
        )

    st.subheader("Land Use Analysis")

    try:

        landuse = ox.features_from_polygon(
            polygon,
            {"landuse": True}
        )

        st.write(
            f"Land Use Features Found: {len(landuse)}"
        )

        if "landuse" in landuse.columns:

            counts = (
                landuse["landuse"]
                .value_counts()
            )

            st.write("Raw Counts")

            st.write(counts)

            total = counts.sum()

            percentages = (
                counts / total
            ) * 100

            st.write(
                "Terrain Composition (%)"
            )

            st.write(
                percentages.round(2)
            )

            dominant = percentages.idxmax()

            st.success(
                f"Dominant Terrain: {dominant}"
            )

        else:

            st.warning(
                "No landuse column returned by OSM."
            )

    except Exception:
        st.warning(
            "No land use data found."
    )

    st.subheader("Natural Features Analysis")

    try:

        natural = ox.features_from_polygon(
            polygon,
            {"natural": True}
        )

        st.write(
            f"Natural Features Found: {len(natural)}"
        )

        if "natural" in natural.columns:

            counts = (
                natural["natural"]
                .value_counts()
            )

            st.write("Natural Feature Counts")

            st.write(counts)

            natural_total = counts.sum()
            natural_percentages = (
                counts / natural_total
                ) * 100
            
            st.write(
                "Natural Composition (%)"
                )
            
            st.write(
                natural_percentages.round(2)
                )
            
            dominant_natural = (
                natural_percentages.idxmax()
                )
            
            st.success(
                f"Dominant Natural Feature: {dominant_natural}"
)

        else:

            st.warning(
                "No natural column returned."
            )

    except Exception:

        st.warning(
            "No natural features found in selected area."
        )


    st.subheader("Waterways")

    try:
        waterways = ox.features_from_polygon(
            polygon,
            {"waterway": True}
        )
        st.write(
            f"Waterways Found: {len(waterways)}"
        )
        
        if "waterway" in waterways.columns:
            waterway_counts = (
                 waterways["waterway"]
                 .value_counts()
            )
            
            st.write(
                waterway_counts
            )
            
            waterway_total = waterway_counts.sum()
            
            waterway_percentages = (
                waterway_counts /
                waterway_total
            ) * 100
            
            st.write(
                "Waterway Composition (%)"
                )
            
            st.write(
                waterway_percentages.round(2)
                )
            
            dominant_waterway = (
                waterway_percentages.idxmax()
                )
            
            st.success(
            f"Dominant Waterway: {dominant_waterway}"
        )
            
        else:
            st.warning(
                "No waterway column returned."
                )
            
            
    except Exception:
        st.warning(
            "No waterways found."
            )
else:

    st.info(
        "Draw a polygon to begin analysis."
    )



