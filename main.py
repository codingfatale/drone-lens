import argparse
from parsers.csv_parser import parse_csv
from parsers.pdf_parser import extract_text_from_pdf, parse_pdf_to_dataframe
from analysis.flight_metrics import calculate_flight_metrics, summarize_flights, add_pdf_duration
from visualization.plots import plot_flight_durations, plot_duration_histogram

def main():
    parser = argparse.ArgumentParser(description="Drone Lens")
    parser.add_argument('--file', type=str,default='data/UAV_Flight_Log.csv', help='Path to the UAV flight log CSV file')
    parser.add_argument("--type", choices=["csv", "pdf"], required=True)
    parser.add_argument('--visualize', action='store_true', help='Whether to generate visualizations')
    parser.add_argument( '--export', type=str, help="Path to export output file (e.g., output.csv)")
    args = parser.parse_args()

   
    file_path = args.file 
    # Example usage of the CSV parser

    if args.type == "csv":
         """
         Parses a CSV file containing UAV flight logs, calculates flight metrics, and prints a summary.
         """
         data = parse_csv(file_path)
         data = calculate_flight_metrics(data)

    elif args.type == "pdf":
        """" 
        Parses a PDF file containing UAV flight logs, extracts flight durations, and prints a summary."""
        text = extract_text_from_pdf(file_path)
        data = parse_pdf_to_dataframe(text)
        data = add_pdf_duration(data)

    if data is not None:
        print(args.type + " file parsed successfully!")
        # print(data.head())  # Display the first 5 rows of the DataFrame
    else:
        print("Failed to parse the " + args.type + " file.")

    # Print summary
    summary = summarize_flights(data)
    print("\nFlight Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Visualizations
    if args.visualize:
        plot_flight_durations(data)
        plot_duration_histogram(data)

    # Export file if requested
    if args.export:
        data.to_csv(args.export, index=False)
        print(f"Data exported to {args.export}")


if __name__ == "__main__":
    main()