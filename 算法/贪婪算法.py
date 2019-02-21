
def broadcast():
    states_needed = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    stations = {}
    stations["A"] = set(['e', 'g', 'f'])
    stations["B"] = set(['a', 'f', 'c'])
    stations["C"] = set(['g', 'd', 'c'])
    stations["D"] = set(['a', 'e'])
    stations["E"] = set(['b', 'f'])
    stations["F"] = set(['c', 'h'])

    final_stations = set()

    while states_needed:
        best_stations = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_for_station & states_needed
            if len(covered) > len(states_covered):
                best_stations = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_stations)

    return final_stations

if __name__ == '__main__':
    print(broadcast())
