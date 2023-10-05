import math
from math import log

def hundeAlder_til_menneskeAlder(hundeAlder):
    menneskealder = 16 * log(hundeAlder) + 31
    print(menneskealder)

hundeAlder_til_menneskeAlder(10)


def inkluder_moms(pris, moms=0.25):
    pris_med_moms = pris + (pris*moms)
    print(pris_med_moms)

pris_uten_moms = 100
inkluder_moms(pris_uten_moms)