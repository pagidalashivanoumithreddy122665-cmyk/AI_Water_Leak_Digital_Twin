import wntr
import config

# Load network without leak
wn = wntr.network.WaterNetworkModel(config.NETWORK_FILE)

# Run normal simulation
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim()

# Extract pressure
pressure = results.node["pressure"]

# Save baseline pressure
pressure.to_csv("baseline_pressure.csv")

print("Baseline created successfully!")
print(pressure.head())