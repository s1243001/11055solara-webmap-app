import leafmap.maplibregl as leafmap
import solara

def create_map():

    m = leafmap.Map(
        center=[121.53545981563654, 25.0301736102832],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("Satellite", visible=False)
    m.add_overture_3d_buildings(template="simple")
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
