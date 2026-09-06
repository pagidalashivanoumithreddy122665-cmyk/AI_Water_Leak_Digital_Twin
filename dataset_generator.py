"""
AI-Based Digital Twin
Improved Dataset Generator with Pressure Loss Features
"""

import pandas as pd
from simulator import run_simulation


NUM_SCENARIOS = 2000

dataset = []


print("=" * 50)
print("GENERATING IMPROVED DATASET")
print("=" * 50)


# -----------------------------------------
# Create baseline (no leak)
# -----------------------------------------

print("\nCreating baseline network...")

from simulator import wntr, config

wn = wntr.network.WaterNetworkModel(config.NETWORK_FILE)

sim = wntr.sim.EpanetSimulator(wn)

baseline_result = sim.run_sim()

baseline_pressure = baseline_result.node["pressure"]
baseline_flow = baseline_result.link["flowrate"]


print("Baseline created successfully")


# -----------------------------------------
# Generate leak scenarios
# -----------------------------------------

for i in range(NUM_SCENARIOS):

    print(f"Scenario {i+1}/{NUM_SCENARIOS}")


    scenario, pressure, flow = run_simulation()


    row = {

        "Scenario": i + 1,

        "Leak_Junction": scenario.junction,

        "Leak_Size": scenario.leak_size,

        "Demand": scenario.demand,

        "Start_Hour": scenario.start_hour,

        "Duration": scenario.duration,

        # numerical leak location feature
        "Leak_Node_Number": int(
            scenario.junction.replace("J","")
        ),

        "Leak_Large":
            1 if scenario.leak_size=="Large" else 0,

        "Leak_Medium":
            1 if scenario.leak_size=="Medium" else 0,

        "Leak_Small":
            1 if scenario.leak_size=="Small" else 0

    }


    # -------------------------------------
    # Pressure Loss Features
    # -------------------------------------

    for junction in pressure.columns:


        if junction == "Reservoir":
            continue


        leak_pressure = pressure[junction].values


        normal = baseline_pressure[junction].values


        loss = normal - leak_pressure



        row[f"{junction}_AvgPressure"] = (
            leak_pressure.mean()
        )


        row[f"{junction}_MinPressure"] = (
            leak_pressure.min()
        )


        row[f"{junction}_MaxPressure"] = (
            leak_pressure.max()
        )


        row[f"{junction}_PressureLossAvg"] = (
            loss.mean()
        )


        row[f"{junction}_PressureLossMax"] = (
            loss.max()
        )


        row[f"{junction}_PressureLossStd"] = (
            loss.std()
        )


    # -------------------------------------
    # Flow Features
    # -------------------------------------

    for pipe in flow.columns:

        values = flow[pipe].values


        row[f"{pipe}_AvgFlow"] = (
            values.mean()
        )


        row[f"{pipe}_MaxFlow"] = (
            values.max()
        )


    dataset.append(row)



# -----------------------------------------
# Save dataset
# -----------------------------------------

df = pd.DataFrame(dataset)


df.to_csv(
    "dataset.csv",
    index=False
)


print("\n" + "="*50)
print("DATASET COMPLETE")
print("="*50)


print(df.head())


print("\nShape:", df.shape)


print("Saved: dataset.csv")
