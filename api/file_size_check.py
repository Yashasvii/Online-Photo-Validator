import os.path
from .models import Config


def check_image(path):
    size = os.path.getsize(path) / 1000.00

    tolerance = 10.00

    config = Config.objects.all()[0]
    min_size = config.min_size - tolerance
    max_size = config.max_size + tolerance

    # Check if the size of the file is greater than 1MB or not
    if min_size <= size <= max_size:
        return True
    return False
