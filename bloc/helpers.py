from enum import Enum
from math import radians, sin, cos, sqrt, atan2

from enums.DistanceType import DistanceType


def calculate_distance(lat1, lon1, lat2, lon2, distance_type=DistanceType.MILES):
    # Convert coordinates to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])

    # Earth's radius in miles or kilometers
    radius = 3959 if distance_type == DistanceType.MILES else 6371

    # Haversine formula to calculate distance
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c

    print(distance)

    return distance
