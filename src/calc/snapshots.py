#!/usr/bin/python3

import numpy as np
import json
from collections import OrderedDict
import argparse

TOTAL_HYDRAS = 1000000

# Input
raw_files = ['../data/snapshots_raw/before_91067.dat',
             '../data/snapshots_raw/before_91201.dat',
             '../data/snapshots_raw/before_91340.dat',
             '../data/snapshots_raw/before_91486.dat',
             '../data/snapshots_raw/before_91618.dat',
             '../data/snapshots_raw/before_91756.dat',
             '../data/snapshots_raw/before_91895.dat',
             '../data/snapshots_raw/before_92026.dat',
             '../data/snapshots_raw/before_92181.dat',
             '../data/snapshots_raw/before_92331.dat',
             '../data/snapshots_raw/before_92477.dat',
             '../data/snapshots_raw/before_92612.dat',
             '../data/snapshots_raw/before_92746.dat']

# Output
balances_chonological_file = '../data/processed/all_balances_chronological.json'
balances_summed_file = '../data/processed/all_balances_summed.json'
HYD_awarded_file = '../data/processed/HYD_awarded.json'

print("Processing raw snapshots...")

nSnaps = len(raw_files)

# Read all snapshots and make a list for each address, containing the balances
snapshots= {}
for i in range(nSnaps):
    rawData = np.asarray( np.genfromtxt(raw_files[i], skip_header=6, dtype=None, encoding=None) )
    for x in rawData:
        address = x[2]#.decode("utf-8")
        if not address in snapshots:
            snapshots[ address ] = np.zeros(nSnaps).tolist()
        snapshots[ address ][i] = x[0]


# Throw out all addresses that do not have any balance and sort the balances by amount
print("Removing timelocked addresses and addresses with zero balance...")
balances_chronological = {}
balances_summed = {}
total = 0
for key, value in snapshots.items():
    if max(value) > 0 and key.startswith('p'): # exclude time locked tokens
        balances_chronological[ key ] = value
        balances_summed[ key ] = sum(value)
        total += sum(value)


print("{} standard addresses had non-zero balance during the snapshots, with a total amount of {} IOP*days".format( len(balances_chronological), total ) )



hyd_per_iop = TOTAL_HYDRAS/total

print("Each IOP will receive {} HYD for each snapshot, or each IOP held for all snapshots will receive {} HYD".format(hyd_per_iop, hyd_per_iop*nSnaps) )

HYD_awarded = {}
total_HYD = 0
for addr, coins in balances_summed.items():
    HYD_awarded[ addr ] = "{:.12f}".format(hyd_per_iop * coins)
    total_HYD += hyd_per_iop * coins

print(total_HYD)

print("Writing chronological balances to JSON... {}".format(balances_chonological_file))
with open(balances_chonological_file, 'w') as outfile:
    json.dump(balances_chronological, outfile, indent=2)

print("Writing summed balances to JSON... {}".format(balances_summed_file))
with open(balances_summed_file, 'w') as outfile:
    json.dump(balances_summed, outfile, indent=2)


print("Writing awarded HYD to JSON... {}".format(HYD_awarded_file))
with open(HYD_awarded_file, 'w') as outfile:
    json.dump(HYD_awarded, outfile, indent=2)