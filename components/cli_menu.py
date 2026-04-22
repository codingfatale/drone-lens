def interactive_menu():
    print("\n=== Drone Flight Log Analyzer ===")
    print("1. Analyze CSV file")
    print("2. Analyze PDF file")
    print("3. Exit")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        file_path = input("Enter CSV file path: ")
        plot = input("Show plots? (y/n): ").lower() == "y"
        export = input("Export summary? (leave blank or enter filename): ")

        return {
            "type": "csv",
            "file": file_path,
            "plot": plot,
            "export": export if export else None
        }

    elif choice == "2":
        file_path = input("Enter PDF file path: ")
        plot = input("Show plots? (y/n): ").lower() == "y"
        export = input("Export summary? (leave blank or enter filename): ")

        return {
            "type": "pdf",
            "file": file_path,
            "plot": plot,
            "export": export if export else None
        }

    elif choice == "3":
        print("Exiting...")
        exit()

    else:
        print("Invalid option.")
        return interactive_menu()