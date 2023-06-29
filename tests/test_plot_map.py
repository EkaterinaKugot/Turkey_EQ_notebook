import pytest
import h5py
import os

from dateutil import tz
from datetime import (datetime, timedelta)
from turkey_eq.turkey import *

_UTC = tz.gettz('UTC')

times = [datetime(2023, 2, 6, 10, 25)]
times = [t.replace(tzinfo=t.tzinfo or _UTC) for t in times]

C_LIMITS ={
    'ROTI': [-0,0.5,'TECu/min'],
    '2-10 minute TEC variations': [-0.2,0.2,'TECu'],
    '10-20 minute TEC variations': [-0.4,0.4,'TECu'],
    '20-60 minute TEC variations': [-0.6,0.6,'TECu'],
    'tec': [0,50,'TECu/min'],
    'tec_adjusted': [0,50,'TECu'],
}

EPICENTERS = {'10:24': {'lat': 38.016,
                        'lon': 37.206,
                        'time': datetime(2023, 2, 6, 10, 24, 50)}
             }


def test_file():
    answers = [True, True, False]
    data = retrieve_data_multiple_source({'tests/dtec_2_10_10_24.h5': 'ROTI'}, 'ROTI', times)
    data = {'ROTI': data}

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), sort=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS, test_mod=True)
    except:
        answers[0] = False

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), sort=False, use_alpha=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS, savefig='tests/text.jpg')
    except:
        answers[1] = False

    try:
        plot_map(times, data, 'ROTI', (25, 50), (25, 50), ncols=2, sort=True, markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS, test_mod=True)
    except:
        answers[2] = True

    os.remove('tests/text.jpg')

    for answer in answers:
        assert answer
