from bench_forest import bench as bench_forest
from bench_list import bench as bench_list
import sqlite3
import matplotlib.pyplot as plt
import os
import numpy as np
import math

def bench_all(n, e, m_max, p):
	bench_list(n, e, m_max, p)
	bench_forest(n, e, m_max, p)

def generate_plot(title="no name", output_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    db_path = os.path.join(project_root, 'DAO', 'benchmark_results.db')
    
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
        
    print(f"Using database at: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
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

    plt.figure(figsize=(5,4))

    for method in methods_set:
        method_data = [(row[1], row[3]) for row in data if row[0] == method]  # (m, time)
        #method_data.sort()  # Ensure x values are sorted
        n_values, time_values = zip(*method_data)

        
        time_values = np.array(time_values)
        n_values = np.array(n_values)

        plt.plot(n_values, time_values, marker='o', linestyle='-', label=method, color=method_colors[method])

    plt.xlabel("n")
    plt.ylabel("Tempo")
    plt.title(title)
    plt.legend()

    # Save or show the plot
    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    else:
        plt.show()

def generate_plot_ref():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    db_path = os.path.join(project_root, 'DAO', 'benchmark_results.db')
    
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
        
    print(f"Using database at: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT method, n, m, time FROM results"
    
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    # Unpack the data into lists
    methods = [row[0] for row in data]
    n_values = [row[1] for row in data]
    m_values = [row[2] for row in data]
    time_values = [row[3] for row in data]
    calculated_values = [math.pow(n,2) for m, n in zip(m_values, n_values)]
  
    max_time = max(time_values)
    max_calc = max(calculated_values)

    calculated_values = (np.array(calculated_values) * np.array(time_values)) / max_calc

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, time_values, marker='o', linestyle='-', color='b', label='m vs Time')
    plt.plot(n_values, calculated_values, marker='x', linestyle='--', color='r', label='n^2')

    plt.xlabel('n')
    plt.ylabel('Tempo (s)')
    plt.title('Foresta')

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    base = 500
    step = 500
    #bench_forest([base+step*x for x in range(10)], 0.9)
    bench_list([base+step*x for x in range(10)], 0.9)
    generate_plot("Lista Concatenata", "linked.png")
