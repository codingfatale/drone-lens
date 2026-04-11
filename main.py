import argparse
from parsers.csv_parser import parse_csv
from analysis.flight_metrics import calculate_flight_metrics, summarize_flights
from visualization.plots import plot_flight_durations, plot_duration_histogram

def main():
    parser = argparse.ArgumentParser(description="Drone Lens")
    parser.add_argument('--file', type=str,default='data/UAV_Flight_Log.csv', help='Path to the UAV flight log CSV file')
    parser.add_argument('--visualize', action='store_true', help='Whether to generate visualizations')
    args = parser.parse_args()

    
    # Example usage of the CSV parser
    #file_path = 'data/UAV_Flight_Log.csv'  # Replace with your actual file path
    file_path = args.file
    data = parse_csv(file_path)

    if data is not None:
        print("CSV file parsed successfully!")
        print(data.head())  # Display the first 5 rows of the DataFrame
    else:
        print("Failed to parse the CSV file.")

    # Compute flight metrics
    data = calculate_flight_metrics(data)

    # Print summary
    summary = summarize_flights(data)
    print("\nFlight Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Visualizations
    if args.visualize:
        plot_flight_durations(data)
        plot_duration_histogram(data)

if __name__ == "__main__":
    main()