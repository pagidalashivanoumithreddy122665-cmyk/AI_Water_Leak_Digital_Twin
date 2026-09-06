"""
Configuration for the AI-Based Digital Twin
"""

NETWORK_FILE = "network.inp"

SIMULATION_DURATION = 24 * 3600      # seconds

TIME_STEP = 3600                     # 1 hour

RESULT_FOLDER = "results"

LEAK_SIZES = {
    "Small": 0.2,
    "Medium": 0.50,
    "Large": 0.90
}

DEMAND_LEVELS = {
    "Low": 0.8,
    "Medium": 1.0,
    "High": 1.2
}
