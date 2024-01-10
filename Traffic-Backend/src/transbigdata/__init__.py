

__version__ = '0.5.3'
__author__ = 'Qing Yu <yuq@sustech.edu.cn>'

# module level doc-string
__doc__ = """
TransBigData - A Python package develop for transportation spatio-temporal big
data processing, analysis and visualization.
=====================================================================

`TransBigData` is a Python package developed for transportation spatio-temporal
big data processing, analysis and visualization. `TransBigData` provides fast
and concise methods for processing common transportation spatio-temporal big
data such as Taxi GPS data, bicycle sharing data and bus GPS data.
`TransBigData` provides a variety of processing methods for each stage of
transportation spatio-temporal big data analysis. The code with `TransBigData`
is clean, efficient, flexible, and easy to use, allowing complex data tasks to
be achieved withconcise code.


Main Features
-------------

Currently, `TransBigData` mainly provides the following methods:

  - Data Quality: Provides methods to quickly obtain the general information of
  the dataset, including the data amount the time period and the sampling
  interval.
  - Data Preprocess: Provides methods to clean multiple types of data error.
  - Data Gridding: Provides methods to generate multiple types of geographic
  grids (Rectangular grids, Hexagonal grids) in the research area. Provides
  fast algorithms to map GPS data to the generated grids.
  - Data Aggregating: Provides methods to aggregate GPS data and OD data into
  geographic polygon.
  - Data Visualization: Built-in visualization capabilities leverage the
  visualization package keplergl to interactively visualize data on Jupyter
  notebook with simple code.
  - Trajectory Processing: Provides methods to process trajectory data,
  including generating trajectory linestring from GPS points, and trajectory
  densification, etc.
  - Basemap Loading: Provides methods to display Mapbox basemap on matplotlib
  figures
"""

from plotmap import (
    plot_map,
    plotscale,
    set_mapboxtoken,
    set_imgsavepath,
    read_imgsavepath,
    read_mapboxtoken
)
from coordinates import (
    gcj02tobd09,
    bd09togcj02,
    wgs84togcj02,
    gcj02towgs84,
    wgs84tobd09,
    bd09towgs84,
    bd09mctobd09,
    getdistance,
    transform_shape
)
from grids import (
    area_to_grid,
    area_to_params,
    GPS_to_grid,
    grid_to_centre,
    grid_to_polygon,
    grid_to_area,
    grid_to_params,
    grid_params_optimize,
    geohash_encode,
    geohash_decode,
    geohash_togrid
)
from gisprocess import (
    ckdnearest,
    ckdnearest_point,
    ckdnearest_line,
    splitline_with_length,
    merge_polygon,
    polyon_exterior
)
from odprocess import (
    odagg_grid,
    odagg_shape,
    tolinewitharrow
)
from preprocess import (
    clean_outofbounds,
    clean_outofshape,
    dataagg,
    id_reindex_disgap,
    id_reindex
)
from bikedata import (
    bikedata_to_od
)
from taxigps import (
    clean_taxi_status,
    taxigps_to_od,
    taxigps_traj_point
)
from mobilephonedata import (
    mobile_stay_duration,
    mobile_identify_home,
    mobile_identify_work,    
    )
from traj import (
    traj_mapmatch,
    traj_clean_drift,
    traj_clean_redundant,
    traj_slice,
    traj_smooth,
    traj_segment,
    traj_densify,
    traj_sparsify,
    traj_stay_move,
    traj_to_linestring,
    traj_length
)

from utils import (
    dumpjson
)

from quality import (
    sample_duration,
    data_summary
)
from busgps import (
    busgps_arriveinfo,
    busgps_onewaytime
)
from crawler import (
    getadmin,
    getbusdata,
    get_isochrone_amap,
    get_isochrone_mapbox,
)
from metro import (
    split_subwayline,
    metro_network,
    get_path_traveltime,
    get_shortest_path,
    get_k_shortest_paths
)
from visualization import (
    visualization_trip,
    visualization_od,
    visualization_data
)

from activity import (
    entropy,
    entropy_rate,
    ellipse_params,
    ellipse_plot,
    plot_activity
)