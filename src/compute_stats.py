#!/usr/bin/env python3
import numpy as np, argparse, csv
p = argparse.ArgumentParser()
p.add_argument("-n", type=int, default=1000, help="grid size")
args = p.parse_args()
field = np.sin(np.linspace(0, 2*np.pi, args.n))  # stand-in for a model field
stats = {"N": args.n, "min": float(field.min()), "max": float(field.max()), "avg": float(field.mean())}
with open("results/summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=stats.keys()); w.writeheader(); w.writerow(stats)
print("Wrote results/summary.csv", stats)

