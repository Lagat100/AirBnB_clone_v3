#!/usr/bin/python3
""" Index module """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Return status: OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Retrieves the number of each objects by type """
    classes = {
        "Amenity": storage.count("Amenity"),
        "City": storage.count("City"),
        "Place": storage.count("Place"),
        "Review": storage.count("Review"),
        "State": storage.count("State"),
        "User": storage.count("User")
    }
    return jsonify(classes)
