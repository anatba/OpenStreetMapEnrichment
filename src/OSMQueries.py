import requests
from lxml.etree import fromstring
from xmljson import XMLData


def get_nodes(bounding_box, amenity):

    """
    :param bounding_box:
    :param amenity:
    :return: elements which have tag of a specific 'amenity', around the bounding_box
    """
    url = "http://www.overpass-api.de/api/xapi?*[amenity={}][bbox={}]" \
        .format(amenity, ",".join([str(x) for x in bounding_box]))
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Got status code: {response.status_code} from osm request')
        return []

    bf = XMLData(dict_type=dict)

    return bf.data(fromstring(response.content))


def locations_to_bounding_box(latitude, longitude, padding=0.01):
    bounding_box = [None, None, None, None]
    bounding_box[0] = min(bounding_box[0] or longitude, longitude) - padding
    bounding_box[1] = min(bounding_box[1] or latitude, latitude) - padding
    bounding_box[2] = max(bounding_box[2] or longitude, longitude) + padding
    bounding_box[3] = max(bounding_box[3] or latitude, latitude) + padding
    return bounding_box
