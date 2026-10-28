"""Datasheet-only prediction of the rotating field amplitudes, compared with the TLE493D measurements.
Run:  python3 predict.py     (needs numpy only)"""
import csv, os
import numpy as np
from field_model import field

BR = 1.32            # T, K&J D48DIA (N42) datasheet, Br max 13,200 G
D, L = 6.35, 12.70   # mm, K&J D48DIA

here = os.path.dirname(__file__)
print("dist  Br_pred  Br_meas   err    Bt_pred  Bt_meas   err")
for row in csv.DictReader(open(os.path.join(here, "..", "data", "measured_summary.csv"))):
    d = float(row["distance_mm"])
    br = BR * field(1, 0, 0, -d, R=D / 2, L=L, theta=0.0)[2] * 1e3
    bt = -BR * field(1, 0, 0, -d, R=D / 2, L=L, theta=np.pi / 2)[1] * 1e3
    mb, mt = float(row["Br_major_mT"]), float(row["Bt_minor_mT"])
    print(f"{d:4.0f}  {br:7.2f}  {mb:7.2f}  {100*(br/mb-1):+5.1f}%  {bt:7.2f}  {mt:7.2f}  {100*(bt/mt-1):+5.1f}%")
