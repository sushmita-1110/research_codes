"""
From Fault Parameters to Moment Tensor

This script computes a 3 x 3 symmetric moment tensor from
fault parameters (strike, dip, and rake) using the Aki & Richards book.
"""

import numpy as np

# Step 1: Define fault parameters
strike, dip, rake = 40, 70, -120  # in degrees

# Conversion from degrees to radians
deg2rad = np.pi / 180
phi = strike * deg2rad   # strike angle in radians
delta = dip * deg2rad    # dip angle in radians
lam = rake * deg2rad     # rake angle in radians

# Step 2: Compute moment tensor components
Mrr = np.sin(2 * lam) * np.sin(delta)**2       # radial-radial
Mtt = -np.sin(lam) * np.sin(2 * delta)        # theta-theta
Mpp = np.sin(lam) * np.sin(2 * delta)         # phi-phi
Mrt = -np.cos(lam) * np.sin(delta)            # radial-theta
Mrp = np.cos(lam) * np.cos(delta)             # radial-phi
Mtp = -np.sin(lam) * np.sin(delta)**2         # theta-phi

# Step 3: Assemble 3×3 symmetric moment tensor
M = np.array([[Mrr, Mrt, Mrp],
              [Mrt, Mtt, Mtp],
              [Mrp, Mtp, Mpp]])

# print matrix
print("3 × 3 symmetric moment tensor:\n", M)