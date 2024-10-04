import curses
import pandas as pd

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Prompt for file path
    stdscr.addstr(0, 0, "Enter the path of the CSV file: ")
    curses.echo()  # Enable echoing of typed characters
    file_path = stdscr.getstr(0, 34).decode("utf-8")  # Get user input

    # Read CSV file
    try:
        data = pd.read_csv(file_path)
        stdscr.addstr(1, 0, "File uploaded successfully!\n")
        stdscr.addstr(2, 0, "Data preview:\n")
        stdscr.addstr(3, 0, str(data.head()))  # Display first few rows of the data
    except Exception as e:
        stdscr.addstr(1, 0, f"Error: {e}\n")

    stdscr.addstr(4, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()  # Wait for user input

# Run the curses application
curses.wrapper(main)

