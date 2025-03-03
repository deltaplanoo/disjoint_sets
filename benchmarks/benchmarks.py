from bench_forest import bench as bench_forest
from bench_list import bench as bench_list
import sqlite3
import matplotlib.pyplot as plt
import os
import numpy as np

def bench_all(n, e, m_max, p):
	bench_list(n, e, m_max, p)
	bench_forest(n, e, m_max, p)

def generate_plot(title="Tempo vs Numero m di operazioni", output_path=None):
    # Connect to the db
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    db_path = os.path.join(project_root, 'DAO', 'benchmark_results.db')
    
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
        
    print(f"Using database at: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Build the query
    query = "SELECT method, n, m, time FROM results"
    
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data found for the given filters.")
        return

    # Extract values
    methods_set = set(row[0] for row in data)  # Unique methods
    colors = plt.colormaps["tab10"]
    method_colors = {method: colors(i) for i, method in enumerate(methods_set)}

    plt.figure(figsize=(10, 6))

    for method in methods_set:
        method_data = [(row[1], row[3]) for row in data if row[0] == method]  # (m, time)
        #method_data.sort()  # Ensure x values are sorted
        n_values, time_values = zip(*method_data)
        
        # Convert to numpy for better handling of log scale
        time_values = np.array(time_values)
        n_values = np.array(n_values)

        plt.plot(n_values, time_values, marker='o', linestyle='-', label=method, color=method_colors[method])

    plt.xlabel("n")
    plt.ylabel("tempo")
    plt.title(title)
    plt.legend()

    # Save or show the plot
    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    else:
        plt.show()


if __name__ == "__main__":
	base = 500
	step = 500

	bench_list([base+step*x for x in range(20)], 0.9)
	generate_plot()
