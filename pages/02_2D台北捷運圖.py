import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[-100, 40],
        zoom=4,
        sidebar_visible=True,
    )

    MRT_geojson = ""
    MRT_style = {
        "layers": [
            {
                "id": "台北MRT",
                "source": "transportation",
                "source-layer": "segment",
                "type": "line",
                "paint": {
                    "line-color": "#ffffff",
                    "line-width": 2,
                },
            },
        ]
    }
    
    m.add_pmtiles(road_pmtiles, style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
