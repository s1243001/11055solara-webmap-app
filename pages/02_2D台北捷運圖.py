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

    routes_geojson = "https://github.com/s1243001/11055solara-webmap-app/blob/main/routes.geojson"
    stations_geojson = "https://github.com/s1243001/11055solara-webmap-app/blob/main/stations.geojson"
    
    
    m.add_geojson(routes_geojson)
    m.add_geojson(stations_geojson)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
