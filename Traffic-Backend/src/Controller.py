# 导入所需的库
import requests
import json
import pandas as pd
import geopandas as gpd
from flask import Flask, request, jsonify
from shapely.geometry import Point, Polygon

# 创建Flask应用
app = Flask(__name__)

# 定义轨迹数据的文件路径
gps_file = "gps_data.csv"

# 定义深圳市地图的文件路径
sz_file = "sz.json"

# 读取轨迹数据
gps_data = pd.read_csv(gps_file, header=None)
gps_data.columns = ["VehicleNum", "Time", "Lng", "Lat", "OpenStatus", "Speed"]

# 读取深圳市地图
sz = gpd.read_file(sz_file)
sz.crs = None

# 定义一个函数，用于将经纬度转换为点对象
def create_point(row):
    return Point(row["Lng"], row["Lat"])

# 为轨迹数据添加点列
gps_data["geometry"] = gps_data.apply(create_point, axis=1)

# 将轨迹数据转换为GeoDataFrame
gps_data = gpd.GeoDataFrame(gps_data, geometry="geometry")

# 定义一个函数，用于判断点是否在深圳市范围内
def in_sz(point):
    return sz.contains(point).any()

# 过滤掉不在深圳市范围内的轨迹数据
gps_data = gps_data[gps_data["geometry"].apply(in_sz)]

# 定义一个路由，用于获取所有轨迹数据
@app.route("/gps", methods=["GET"])
def get_gps():
    # 将轨迹数据转换为JSON格式
    gps_json = gps_data.to_json()
    # 返回JSON响应
    return jsonify(gps_json)

# 定义一个路由，用于获取指定车辆的轨迹数据
@app.route("/gps/<int:vehicle_num>", methods=["GET"])
def get_gps_by_vehicle(vehicle_num):
    # 根据车辆编号筛选轨迹数据
    gps_by_vehicle = gps_data[gps_data["VehicleNum"] == vehicle_num]
    # 将轨迹数据转换为JSON格式
    gps_json = gps_by_vehicle.to_json()
    # 返回JSON响应
    return jsonify(gps_json)

# 定义一个路由，用于创建新的轨迹数据
@app.route("/gps", methods=["POST"])
def create_gps():
    # 获取请求的JSON数据
    gps_json = request.get_json()
    # 将JSON数据转换为DataFrame
    gps_df = pd.DataFrame(gps_json)
    # 为DataFrame添加点列
    gps_df["geometry"] = gps_df.apply(create_point, axis=1)
    # 将DataFrame转换为GeoDataFrame
    gps_gdf = gpd.GeoDataFrame(gps_df, geometry="geometry")
    # 将新的轨迹数据追加到原有的轨迹数据
    global gps_data
    gps_data = gps_data.append(gps_gdf, ignore_index=True)
    # 返回成功的响应
    return jsonify({"message": "GPS data created successfully."})

# 定义一个路由，用于更新指定车辆的轨迹数据
@app.route("/gps/<int:vehicle_num>", methods=["PUT"])
def update_gps_by_vehicle(vehicle_num):
    # 获取请求的JSON数据
    gps_json = request.get_json()
    # 将JSON数据转换为DataFrame
    gps_df = pd.DataFrame(gps_json)
    # 为DataFrame添加点列
    gps_df["geometry"] = gps_df.apply(create_point, axis=1)
    # 将DataFrame转换为GeoDataFrame
    gps_gdf = gpd.GeoDataFrame(gps_df, geometry="geometry")
    # 根据车辆编号删除原有的轨迹数据
    global gps_data
    gps_data = gps_data[gps_data["VehicleNum"] != vehicle_num]
    # 将新的轨迹数据追加到原有的轨迹数据
    gps_data = gps_data.append(gps_gdf, ignore_index=True)
    # 返回成功的响应
    return jsonify({"message": "GPS data updated successfully."})

# 定义一个路由，用于删除指定车辆的轨迹数据
@app.route("/gps/<int:vehicle_num>", methods=["DELETE"])
def delete_gps_by_vehicle(vehicle_num):
    # 根据车辆编号删除原有的轨迹数据
    global gps_data
    gps_data = gps_data[gps_data["VehicleNum"] != vehicle_num]
    # 返回成功的响应
    return jsonify({"message": "GPS data deleted successfully."})


