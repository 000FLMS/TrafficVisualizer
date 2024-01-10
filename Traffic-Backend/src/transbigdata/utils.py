

import numpy as np

def dumpjson(data, path):
    '''
    Input the json data and save it as a file. This method is suitable for
    sovling the problem that numpy cannot be compatiable with json package.

    Parameters
    -------
    data : json
        The json data to be saved
    path : str
        The storage path

    '''
    import json

    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)  # pragma: no cover
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return super(NpEncoder, self).default(obj)  # pragma: no cover
    f = open(path, mode='w')
    json.dump(data, f, cls=NpEncoder)
    f.close()