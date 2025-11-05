import solara
import leafmap.maplibregl as leafmap


def create_map():
    # 設置地圖，並將中心點調整至台北(約121.56, 25.04)
    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[121.56, 25.04],  # 台北市經緯度
        zoom=10,                 # 適合顯示城市範圍的縮放級別
        sidebar_visible=True,
    )

    # 基礎的 GitHub Raw Content URL
    # *** 修正：將 'github.com/...' 改為 'raw.githubusercontent.com/...' 才能正確讀取檔案 ***
    repo_url = "https://raw.githubusercontent.com/s1243001/11055solara-webmap-app/main/"
    
    routes_geojson = repo_url + "routes.geojson"
    stations_geojson = repo_url + "stations.geojson"
    
    # 加入 GeoJSON 圖層
    # leafmap/geopandas 現在可以透過 Raw URL 讀取到正確的 GeoJSON 格式內容
    m.add_geojson(routes_geojson, layer_name="捷運路線")
    m.add_geojson(stations_geojson, layer_name="捷運站點")
    
    return m


@solara.component
def Page():
    # 傳回 Solara 元件
    m = create_map()
    return m.to_solara()
