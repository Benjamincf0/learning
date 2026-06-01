import pandas as pd
import pickle

from google.maps import routing_v2
from google.maps.routing_v2 import (
    ComputeRoutesRequest,
    Waypoint,
    Location,
    RouteTravelMode,
    RoutingPreference,
    Units,
)

from google.type import latlng_pb2
from dotenv import load_dotenv 
import os
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
from typing import Any
Point2D = tuple[float, float]
Polyline = Any

# BIXI_CSV_PATH = "./DonneesOuvertes2025_010203040506070809101112.csv"
BIXI_FEATHER_PATH = "./bixidata.feather"

load_dotenv()
GOOGLEMAPS_API_KEY = os.getenv("GOOGLEMAPS_API_KEY")

START_COLS = ['STARTSTATIONLATITUDE', 'STARTSTATIONLONGITUDE']
END_COLS = ['ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE']

# Helper to get directions
def make_waypoint(lat: float, lng: float) -> Waypoint:
    return Waypoint(
        location=Location(
            lat_lng=latlng_pb2.LatLng(latitude=lat, longitude=lng)
        )
    )

def get_route(start: Point2D, end: Point2D):
    # API key passed via header metadata + client option
    client = routing_v2.RoutesClient(
        client_options={"api_key": GOOGLEMAPS_API_KEY}
    )

    request = ComputeRoutesRequest(
        origin=make_waypoint(*start),
        destination=make_waypoint(*end),
        travel_mode=RouteTravelMode.BICYCLE,
        # routing_preference=RoutingPreference.TRAFFIC_AWARE,
        compute_alternative_routes=False,
        language_code="en-US",
        units=Units.METRIC,
    )

    # Field mask REQUIRED -> pass as gRPC metadata
    field_mask = (
        "routes.duration,"
        "routes.distance_meters,"
        "routes.polyline.encoded_polyline"
    )

    response = client.compute_routes(
        request=request,
        metadata=[("x-goog-fieldmask", field_mask)],
    )

    # for route in response.routes:
    #     print("distance_m:", route.distance_meters)
    #     print("duration:", route.duration.seconds, "s")
    #     print("polyline:", route.polyline.encoded_polyline)

    return response
