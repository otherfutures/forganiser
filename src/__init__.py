"""
A simple program to auto. tidy your Downloads folder (it can also run on other folders, 
if desired) by moving loose files into folders it creates; leaves existing folders alone.

Program runs as follows:
    1. Show ASCII header & options
    2. User input/choice
    3. Sort Downloads folder:
        3.1 Checks filepath to Downloads folder via down_path()
        3.2 Creates folders via create_folders()
        3.3 Moves files into folders via move_files() 
    4. Other folder sort:
        4.1 User input
        4.2 Same steps as 3. above
    5. Exit

Should work on Mac/Linux & Windows, but has only been tested on Windows.    
"""
# Native lib.
import os
import sys
import shutil
from pathlib import Path


def main():
    # ASCII art header
    header()

    # Choices for preferred folder
    print(
        "\033[94m[1]\033[0m to sort the Downloads folder\n"
        "\033[94m[2]\033[0m to sort some other folder\n"
        "\033[94m[3]\033[0m to exit\n\n"
    )

    while True:
        choice = input("\033[94mChoice:\033[0m ").strip()  # Blue ANSI
        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue  # Loop back to asking user for input

        if choice == "3":
            print("\n")
            sys.exit()

        # Sort alt. folder
        elif choice == "2":
            print("\n")
            while True:
                path = input("\033[94mPath of the folder: \033[0m ").strip()
                if os.path.exists(path):
                    folderpaths = create_folders(path)
                    move_files(path, folderpaths)
                    break  # Exit loop if folder found

        # Sort the Downloads folder
        else:
            if not down_path():
                print(
                    "Oops! Looks like your Downloads folder is not at the default location"
                )
                while True:
                    path = input("\033[94mPath of the folder:\033[0m ").strip()
                    if os.path.exists(path):
                        break
            else:
                path = down_path()
                folderpaths = create_folders(path)
                move_files(path, folderpaths)

        break  # Exit main loop


def create_folders(path):
    """
    User determined folder names:
        Iter. thru. folder names & makes new folders if not already existing;
        returns dict. of folder names & their respective filepaths

    N.B. If you're customising this pt., be sure to edit the move_files() func.,
        esp. the if statements
    """

    # '<SUBFOLDER>': os.path.join('<FOLDER>', '<SUBFOLDER>') for folders in folders
    #   where <FOLDER> == the folder containing the subfolder (i.e. parent folder)
    #   & <SUBFOLDER> == subfolder name
    # os.path.join() is used instead of an abs./rel. filepath for cross OS compatibility
    #   but abs. path can still be used: i.e. <SUBFOLDER>: abs. path of parent folder
    folders = {
        "MUSIC": "",
        "VIDEOS": "",
        "PICTURES": "",
        "APPS": "",
        "PROGRAMS": os.path.join(path, "APPS"),
        "DOCUMENTS": "",
        "ARCHIVES": "",
        "SUBTITLES": "",
        "EBOOKS": "",
        "COMICS": os.path.join(path, "EBOOKS"),
    }
    folderpaths = {}

    for folder_name, rel_path in folders.items():
        folder_pathname = os.path.join(path, folder_name)

        if rel_path:
            folder_pathname = os.path.join(rel_path, folder_name)

        if not os.path.exists(folder_pathname):
            os.makedirs(folder_pathname)

        folderpaths[folder_name] = folder_pathname

    return folderpaths


def move_files(path, folderpaths):
    """Common file extensions & the sorting/moving of files into folders"""

    music_ext = [".mp3", ".m4a", ".wav", ".wma", ".aac", ".flac", ".alac", ".ogg"]

    videos_ext = [
        ".mp4",
        ".3gp",
        ".webm",
        ".mov",
        ".mpeg",
        ".mpg",
        ".vob",
        ".avi",
        ".mkv",
        ".wmv",
        ".flv",
        ".ogg",
    ]

    pictures_ext = [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".tiff",
        ".psd",
        ".raw",
        ".svg",
        ".webp",
        ".ai",
        ".tif",
        ".bmp",
        ".eps",
        ".cr2",
        ".nef",
        ".orf",
        ".avif",
    ]

    programs_ext = [
        ".py",
        ".java",
        ".c",
        ".cpp",
        ".cs",
        ".js",
        ".rb",
        ".php",
        ".hs",
        ".ml",
        ".mli",
        ".pl",
        ".go",
        ".css",
        ".xml",
        ".json",
        ".csv",
        ".sql",
        ".db",
        ".class",
        ".jar",
        ".dll",
    ]

    documents_ext = [
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".txt",
        ".ppt",
        ".pptx",
        ".html",
        ".htm",
        ".rtf",
        ".odt",
    ]

    applications_ext = [".exe", ".apk", ".deb", ".app", ".msi", ".dmg", ".rpm"]

    archives_ext = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]

    subtitles_ext = [".srt", ".sub", ".ass", ".vtt", ".stl"]

    ebooks_ext = [".epub", ".mobi", ".djv", ".azw", ".azw3", ".prc"]

    comics_ext = [".cbr", ".cbz"]

    unorg_files = os.listdir(path)  # Loose files in Downloads/user input folder

    for file in unorg_files:
        filepath = f"{path}{os.path.sep}{file}"
        ext = os.path.splitext(filepath)[1].lower()

        try:
            if ext in music_ext:
                shutil.move(filepath, folderpaths["MUSIC"])
            elif ext in videos_ext:
                shutil.move(filepath, folderpaths["VIDEOS"])
            elif ext in pictures_ext:
                shutil.move(filepath, folderpaths["PICTURES"])
            elif ext in programs_ext:
                shutil.move(filepath, folderpaths["PROGRAMS"])
            elif ext in documents_ext:
                shutil.move(filepath, folderpaths["DOCUMENTS"])
            elif ext in applications_ext:
                shutil.move(filepath, folderpaths["APPS"])
            elif ext in archives_ext:
                shutil.move(filepath, folderpaths["ARCHIVES"])
            elif ext in subtitles_ext:
                shutil.move(filepath, folderpaths["SUBTITLES"])
            elif ext in ebooks_ext:
                shutil.move(filepath, folderpaths["EBOOKS"])
            elif ext in comics_ext:
                shutil.move(filepath, folderpaths["COMICS"])

        except shutil.Error:
            try:
                # If there is a name collision, append counter no. to filename
                new_filename = os.path.splitext(file)[0]
                suffix = 1  # Init. counter to start at 1
                while True:
                    new_filepath = os.path.join(path, f"{new_filename} ({suffix}){ext}")
                    if not os.path.exists(new_filepath):
                        break
                    suffix += 1
                shutil.move(filepath, new_filepath)
                os.remove(filepath)
            except FileNotFoundError:
                pass
        except KeyError:
            print(
                f"\nPlease check whether dict. key name(s) (ln. 90-99)"
                f" & if-statements (ln. 214-232) are matching"
            )
            sys.exit()
        except FileNotFoundError:
            print(f"FileNotFoundError: Could not find file: '{filepath}'")
        except Exception as e:
            print(f"An error occurred while processing '{file}': {str(e)}")


def down_path():
    """Tries to get the abs. filepath to your Downloads folder"""
    try:
        path = f"{str(Path.home() / 'Downloads')}{os.path.sep}"
        if os.path.exists(path):
            return path
        else:
            return False
    except:
        return False


def header():
    header = """
        ______                             _               
       / ____/___  _________ _____ _____  (_)_______  _____
      / /_  / __ \/ ___/ __ `/ __ `/ __ \/ / ___/ _ \/ ___/
     / __/ / /_/ / /  / /_/ / /_/ / / / / (__  )  __/ /    
    /_/    \____/_/   \__, /\__,_/_/ /_/_/____/\___/_/     
                     /____/                                
                                    
    A nifty tool to sort your messy folders [MIT License]
    """
    print(f"\033[93m{header}\033[0m")  # Yellow ANSI for header


if __name__ == "__main__":
    main()
