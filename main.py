from graph import *
from bfs import bfs
from dijkstra import dijkstra
from graph_init import *

character_locations = {
    "Harry Potter": "British Columbia",
    "Hermione Granger": "Ontario",
    "Ron Weasley": "Quebec",
    "Luna Lovegood": "Newfoundland and Labrador",
    "Neville Longbottom": "Saskatchewan",
    "Ginny Weasley": "Nova Scotia"
}

def calculate_paths(algorithm, g):
    results = {}
    destination = "Ottawa"
    
    for character, start in character_locations.items():
        try:
            shp_path, shp_cost = algorithm(g, start, destination, "hops")
            sdp_path, sdp_cost = algorithm(g, start, destination, "distance")
            stp_path, stp_cost = algorithm(g, start, destination, "time")
            fdp_path, fdp_cost = algorithm(g, start, destination, "dementors")
            
            results[character] = {
                "SHP": (shp_cost, shp_path),
                "SDP": (sdp_cost, sdp_path),
                "STP": (stp_cost, stp_path),
                "FDP": (fdp_cost, fdp_path)
            }
        except ValueError as e:
            print(f"Error calculating paths for {character}: {str(e)}")
            continue
    
    return results

def print_results(results):
    """Print results showing both the path and cost with cost type"""
    cost_labels = {
        'SHP': 'Number of hops',
        'SDP': 'Total distance (km)',
        'STP': 'Total time (hours)',
        'FDP': 'Dementors encountered'
    }
    
    for character, paths in results.items():
        print(f"\n{character}:")
        print("-" * (len(character)+1))
        for path_type, (cost, path) in paths.items():
            print(f"{path_type}:")
            print(f"  {cost_labels[path_type]}: {cost}")
            print(f"  Path: {' → '.join(path) if path else 'No path found'}")

def start_Reunion():
    while True:
        print("\nChoose algorithm:")
        print("1: BFS ")
        print("2: Dijkstra")
        print("Type 'exit' to quit")
        
        choice = input("Your choice (1/2): ").strip().lower()
        
        if choice == "exit":
            print("Exiting program")
            break
        elif choice == "1":
            print("\nCalculating all paths using BFS...")
            results = calculate_paths(bfs, g)
            print_results(results)
        elif choice == "2":
            print("\nCalculating all paths using Dijkstra...")
            results = calculate_paths(dijkstra, g)
            print_results(results)
        else:
            print("Invalid input. Please enter 1, 2, or 'exit'")

if __name__ == "__main__":
    start_Reunion()