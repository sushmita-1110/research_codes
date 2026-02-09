"""
CMT Solution: Seismic Moment, Moment Magnitude, and Beachball Plot

This script computes the seismic moment (M0), moment magnitude (Mw),
and plots a beachball diagram from moment tensor components.
"""

import numpy as np
import matplotlib.pyplot as plt
from obspy.imaging.beachball import beachball


def compute_seismic_moment(mrr, mtt, mpp, mrt, mrp, mtp):
    """
    Compute seismic moment (M0) from moment tensor components.
    Seismic moment in dyne·cm
    """
    return (1 / np.sqrt(2)) * np.sqrt(
        mrr**2 + mtt**2 + mpp**2 + 2 * (mrt**2 + mrp**2 + mtp**2)
    )


def compute_moment_magnitude(m0):
    """
    Compute moment magnitude (Mw) from seismic moment.
    """
    return (2 / 3) * (np.log10(m0) - 16.1)


def cmtsolution_plot(mrr, mtt, mpp, mrt, mrp, mtp):
    """
    Compute Mw and plot beachball diagram for a CMT solution.
    """
    # Compute seismic moment and magnitude
    m0 = compute_seismic_moment(mrr, mtt, mpp, mrt, mrp, mtp)
    mw = compute_moment_magnitude(m0)

    # Print results
    print(f"Seismic Moment (M0): {m0:.3e} dyne·cm")
    print(f"Moment Magnitude (Mw): {mw:.2f}")

    # Plot beachball diagram
    moment_tensor = [mrr, mtt, mpp, mrt, mrp, mtp]
    beachball(moment_tensor, linewidth=2, facecolor="k", bgcolor="w")
    plt.show()


# example: CMT solution values
Mrr = -0.002e23
Mtt = -0.064e23
Mpp = 0.066e23
Mrt = -0.090e23
Mrp = -0.002e23
Mtp = -0.188e23

# plot beachball
cmtsolution_plot(Mrr, Mtt, Mpp, Mrt, Mrp, Mtp)