import unittest
from flask import json
from unittest.mock import patch
from src.EnrichOSMApi import app
from test.Samples import five_ways_with_school_xml, two_nodes_of_school_xml, rel_xml, four_nodes_nine_ways_one_rel_xml, \
    empty_xml


def test_post(expected_schools):
    response = app.test_client().post(
        '/api/enrich',
        data=json.dumps({
            "data": [
                {
                    "Latitude": 0.0,
                    "Longitude": 0.0
                }
            ]
        }
        ),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['data'][0]['Schools'] == expected_schools


class MyTestCase(unittest.TestCase):

    @patch('src.OSMQueries.requests.get')
    def test_ways_schools(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = five_ways_with_school_xml
        test_post(5)

    @patch('src.OSMQueries.requests.get')
    def test_nodes_schools(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = two_nodes_of_school_xml
        test_post(2)

    @patch('src.OSMQueries.requests.get')
    def test_relation_schools(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = rel_xml
        test_post(1)

    @patch('src.OSMQueries.requests.get')
    def test_nodes_ways_rel_schools(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = four_nodes_nine_ways_one_rel_xml
        test_post(14)

    @patch('src.OSMQueries.requests.get')
    def test_no_schools(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = empty_xml
        test_post(0)


if __name__ == '__main__':
    unittest.main()
