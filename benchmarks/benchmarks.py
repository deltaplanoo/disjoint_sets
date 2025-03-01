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
        method_data = [(row[2], row[3]) for row in data if row[0] == method]  # (m, time)
        method_data.sort()  # Ensure x values are sorted
        m_values, time_values = zip(*method_data)
        
        # Convert to numpy for better handling of log scale
        m_values = np.array(m_values)
        time_values = np.array(time_values)

        plt.plot(m_values, time_values, marker='o', linestyle='-', label=method, color=method_colors[method])

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("m (Scala Logaritmica)")
    plt.ylabel("Tempo (Scala Logaritmica)")
    plt.title(title)
    plt.legend()

    # Set grid only at powers of 10
    ax = plt.gca()
    ax.set_xticks(10**np.arange(np.floor(np.log10(min(m_values))), np.ceil(np.log10(max(m_values))) + 1))
    ax.set_yticks(10**np.arange(np.floor(np.log10(min(time_values))), np.ceil(np.log10(max(time_values))) + 1))
    ax.grid(True, which="major", linestyle="--", linewidth=0.5)

    # Ensure only major ticks appear
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.yaxis.set_minor_locator(plt.NullLocator())

    # Save or show the plot
    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    else:
        plt.show()


if __name__ == "__main__":
	#bench_all(5, 0.2, 1000000, 3)	# nodes, density, m_max, step
	bench_list(5, 0.2, 1000000, 3)
	generate_plot()
