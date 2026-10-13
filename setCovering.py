def main(states_needed, final_stations):
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states # find the item that shows up in both sets
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations



if __name__ == "__main__":
    states_needed = set(['mt', 'wa', 'or', 'id','nv','ut', 'ca', 'az']) # A set can't have duplicates
    stations = {}
    final_stations = set()


    stations["Kone"] = set(["id", "nv", "ut"])
    stations["Ktwo"] = set(["wa", "id", "mt"])
    stations["Kthree"] = set(["or", "nv", "ca"])
    stations["Kfour"] = set(["nv", "ut"])
    stations["Kfive"] = set(["ca", "az"])

    print(main(states_needed, final_stations))

