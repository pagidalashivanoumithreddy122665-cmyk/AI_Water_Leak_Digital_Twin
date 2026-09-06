"""
Digital Twin Simulator
AI-Based Digital Twin for Water Leak Impact & Response Optimisation
"""

import wntr
import config
from scenario import LeakScenario
from analysis import analyze_results


def run_simulation():

    scenario = LeakScenario()


    wn = wntr.network.WaterNetworkModel(
        config.NETWORK_FILE
    )


    # Demand multiplier

    wn.options.hydraulic.demand_multiplier = config.DEMAND_LEVELS[
        scenario.demand
    ]


    # Leak location

    junction = wn.get_node(
        scenario.junction
    )


    # Apply leak

    junction.add_leak(
        wn,
        area=config.LEAK_SIZES[scenario.leak_size],
        start_time=scenario.start_hour * 3600,
        end_time=(scenario.start_hour + scenario.duration) * 3600
    )


    sim = wntr.sim.EpanetSimulator(wn)


    results = sim.run_sim()


    pressure = results.node["pressure"]

    flow = results.link["flowrate"]


    return scenario, pressure, flow



def display_results(
        scenario,
        pressure,
        flow
):

    print()

    scenario.display()


    print("\nAverage Pressure")
    print(pressure.mean())


    print("\nAverage Flow")
    print(flow.mean())


    analyze_results(
        pressure,
        flow
    )



if __name__ == "__main__":

    scenario, pressure, flow = run_simulation()

    display_results(
        scenario,
        pressure,
        flow
    )
