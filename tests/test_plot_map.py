import pytest
import h5py
import os

from dateutil import tz
from datetime import (datetime, timedelta)
from turkey_eq.turkey import *

_UTC = tz.gettz('UTC')

times = [datetime(2023, 2, 6, 10, 25), datetime(2023, 2, 6, 10, 40), datetime(2023, 2, 6, 10, 45, 0)]
times = [t.replace(tzinfo=t.tzinfo or _UTC) for t in times]


def test_file():
    answers = [True, True, False]
    data = retrieve_data_multiple_source({'tests/dtec_2_10_10_24.h5': 'ROTI'}, 'ROTI', times)
    data = {'ROTI': data}

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), sort=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS)
    except:
        answers[0] = False

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), sort=False, use_alpha=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS, savefig='tests/text.jpg')
    except:
        answers[1] = False

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), ncols=1, sort=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS)
    except:
        answers[2] = True

    os.remove('tests/text.jpg')

    for answer in answers:
        assert answer
