"""
Impact Analysis Module
"""

import pandas as pd


def analyze_results(pressure, flow):

    # Average pressure at each node
    avg_pressure = pressure.mean()

    # Average flow in each pipe
    avg_flow = flow.mean()

    # Remove reservoir from calculations
    if "Reservoir" in avg_pressure.index:
        pressure_only = avg_pressure.drop("Reservoir")
    else:
        pressure_only = avg_pressure

    min_node = pressure_only.idxmin()
    max_node = pressure_only.idxmax()

    min_pressure = pressure_only.min()
    max_pressure = pressure_only.max()

    network_average = pressure_only.mean()

    average_flow = avg_flow.mean()

    # Simple severity classification
    if min_pressure < 45:
        severity = "HIGH"
    elif min_pressure < 50:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    affected = pressure_only[pressure_only < network_average].index.tolist()

    print("\n" + "=" * 40)
    print("DIGITAL TWIN IMPACT ANALYSIS")
    print("=" * 40)

    print(f"Average Network Pressure : {network_average:.2f} m")
    print(f"Minimum Pressure         : {min_pressure:.2f} m ({min_node})")
    print(f"Maximum Pressure         : {max_pressure:.2f} m ({max_node})")
    print(f"Average Pipe Flow        : {average_flow:.4f} m³/s")
    print(f"Leak Severity            : {severity}")
    print(f"Affected Junctions       : {', '.join(affected)}")

    print("=" * 40)

    return {
        "average_pressure": network_average,
        "minimum_pressure": min_pressure,
        "maximum_pressure": max_pressure,
        "severity": severity,
        "affected_nodes": affected,
        "average_flow": average_flow,
    }

