import flask
from flask import request
from src.Enrichment import get_schools_amount

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/enrich', methods=['POST'])
def enrich_schools_amount():

    """
    This method returns the number of schools around(*) the Latitude,Longitude in input, according to the OSM API.
    (*) around - please note that padding is 0.01
    """

    if request.is_json:
        content = request.get_json()
        for data_row in content['data']:
            data_row.update({'Schools': get_schools_amount(data_row['Latitude'], data_row['Longitude'])})
        return content
    else:
        return "415 Unsupported"


if __name__ == '__main__':
    app.run()
