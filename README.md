# Simple Text-Based Note-Taking App

A minimal command-line note-taking application in Python. Notes are saved with timestamps to a local file.

## Features

- Add text notes with automatic timestamping
- View all saved notes
- Simple menu-driven interface
- Notes are stored in `notes.txt` in the script's directory

## Usage

1. **Run the app:**
   ```bash
   python note_taking_app.py
   ```

2. **Menu Options:**
   - `1` - Add a note: Type your note and press Enter. It will be saved with the current date and time.
   - `2` - View notes: Display all notes stored in `notes.txt`.
   - `3` - Quit: Exit the application.

## Example

```
Simple Note-Taking App
----------------------

Options:
1. Add a note
2. View notes
3. Quit
Choose an option (1-3): 1
Enter your note: Finish writing the report
Note saved!
```

## Requirements

- Python 3.x

No third-party packages required.

## License

MIT License
