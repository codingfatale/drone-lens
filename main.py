import argparse
from parsers.csv_parser import parse_csv
from parsers.pdf_parser import extract_text_from_pdf, parse_pdf_to_dataframe
from analysis.flight_metrics import calculate_flight_metrics, summarize_flights, add_pdf_duration
from visualization.plots import plot_flight_durations, plot_duration_histogram
from components.cli_menu import interactive_menu
from utils.export import export_data, get_clean_output

def main():
    parser = argparse.ArgumentParser(description="Drone Lens")
    parser.add_argument('--file', type=str,default='data/UAV_Flight_Log.csv', help='Path to the UAV flight log CSV file')
    parser.add_argument("--type", choices=["csv", "pdf"], required=True)
    parser.add_argument('--plot', action='store_true', help='Whether to generate visualizations')
    parser.add_argument('--export', type=str,   help="Export processed data to file (CSV or JSON)")
    args = parser.parse_args()

    # If no args → launch menu
    if not args.file or not args.type:
        user_input = interactive_menu()

        file_path = user_input["file"]
        file_type = user_input["type"]
        plot_flag = user_input["plot"]
        export_path = user_input["export"]
    else:
        file_path = args.file
        file_type = args.type
        plot_flag = args.plot
        export_path = args.export

    if file_type == "csv":
         """
         Parses a CSV file containing UAV flight logs, calculates flight metrics, and prints a summary.
         """
         data = parse_csv(file_path)
         data = calculate_flight_metrics(data)

    elif file_type == "pdf":
        """" 
        Parses a PDF file containing UAV flight logs, extracts flight durations, and prints a summary."""
        text = extract_text_from_pdf(file_path)
        data = parse_pdf_to_dataframe(text)
        data = add_pdf_duration(data)

    if data is not None:
        print(file_type + " file parsed successfully!")
        # print(data.head())  # Display the first 5 rows of the DataFrame
    else:
        print("Failed to parse the " + file_type + " file.")

    # Print summary
    summary = summarize_flights(data)
    print("\nFlight Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Visualizations
    if  plot_flag:
        plot_flight_durations(data)
        plot_duration_histogram(data)

    # Export file if requested
    if export_path:
        clean_df = get_clean_output(data)
        export_data(clean_df, args.export)


if __name__ == "__main__":
    main()