from src.OSMQueries import get_nodes, locations_to_bounding_box


def get_schools_amount(latitude, longitude):

    """
    This method asks for a list of all the elements that have the school tag,
    then parse the response to count each node\way\relation with the <amenity,school> tag.

    :param latitude:
    :param longitude:
    :return: number of schools around latitude, longitude
    """
    schools_in_area = get_nodes(locations_to_bounding_box(latitude, longitude, 0.01), 'school')
    schools = 0
    for key in schools_in_area['osm'].keys():
        if key == 'way' or key == 'node' or key == 'relation':
            element_attributes = schools_in_area['osm'][key]
            if isinstance(element_attributes, list):
                for attribute in element_attributes:
                    schools = count_schools_in_single_element(schools, attribute)
            else:
                schools = count_schools_in_single_element(schools, element_attributes)
    return schools


def count_schools_in_single_element(schools, attribute):
    if 'tag' in attribute:
        if isinstance(attribute['tag'], dict):
            schools = count_if_tag_is_school(attribute['tag'], schools)
        else:
            for tagItem in attribute['tag']:
                schools = count_if_tag_is_school(tagItem, schools)
    return schools


def count_if_tag_is_school(tag_dict, schools):
    if 'amenity' in tag_dict.values() and 'school' in tag_dict.values():
        schools = schools + 1
    return schools
