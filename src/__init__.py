"""
A simple program to auto. tidy your Downloads folder (it can also run on other folders, 
if desired). Moves loose files; leaves existing folders alone.

Program runs as follows:
    1. Show ASCII header & options
    2. User input/choice
    3. Download folder sort:
        3.1 Checks filepath to Downloads folder via down_path()
        3.2 Creates folders via create_folders()
        3.3 Moves files into folders via move_files() 
    4. Other folder sort:
        4.1 User input
        4.2 Same steps as 3. above
    5. Exit

Should work on Mac/Linux & Windows, but has only been tested on Windows.    
"""

import os
import sys
import shutil
from datetime import datetime
from pathlib import Path
from termcolor import colored


def create_folders(path):
    """
    User determined folder names:
        Iter. thru. folder names & makes new folders if not already existing;
        returns dict. of folder names & their respective filepaths

    N.B. If you're customising this pt., be sure to edit the move_files() func.,
        esp. the if statements
    """

    # '<SUBFOLDER>': os.path.join('<FOLDER>', '<SUBFOLDER>') for folders in folders
    #   where <FOLDER> == the folder containing the subfolder
    #   & <SUBFOLDER> == subfolder name
    # os.path.join() is used instead of an abs./rel. filepath for cross OS compatibility,
    #   but hardcoded filepaths are fine if you prefer.
    folders = {
        "MUSIC": "",
        "VIDEO": "",
        "PICTURES": "",
        "APPS": "",
        "PROGRAMS": os.path.join(path, "APPS"),
        "DOCUMENTS": "",
        "ARCHIVES": "",
        "TV SERIES": "", # N.B. Isn't be auto. sorted
        "SUBTITLES": os.path.join(path, "TV SERIES"),
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
    """Common file extensions & the sorting/moving of files"""

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

    unorg_files = os.listdir(path)  # Loose files in Downloads folder

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

        except shutil.Error as e:
            # If there is a name collision, append no. to filename
            new_filename = os.path.splitext(file)[0]
            suffix = 1
            while True:
                new_filepath = os.path.join(path, f"{new_filename} ({suffix}){ext}")
                if not os.path.exists(new_filepath):
                    break
                suffix += 1
            shutil.move(filepath, new_filepath)
            os.remove(filepath)
        except KeyError as e:
            print(
                "Please check whether dict. key name(s) in folder variable (ln. 42)"
                " & if-statements (ln. 171-190) are matching."
            )
            sys.exit()
        except Exception as e:
            print(f"An error occurred while processing '{file}': {str(e)}")


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
    print(colored(header, "yellow"))


def main():
    # ASCII art header
    header()

    # choice for the preferred folder
    print(f"{colored('[1]', 'blue')} to sort the Downloads folder")
    print(f"{colored('[2]', 'blue')} to sort some other folder")
    print(f"{colored('[3]', 'blue')} to exit")
    print("\n")

    while True:
        choice = input(colored("Choice: ", "blue"))
        if choice in ["1", "2", "3"]:
            # exits the program
            if choice == "3":
                print("\n")
                sys.exit()

            # sorts the alternate folder
            elif choice == "2":
                print("\n")
                while True:
                    path = input(colored("Path of the folder: ", "blue"))
                    if os.path.exists(path):
                        # path for the created folders
                        folderpaths = create_folders(path)
                        move_files(path, folderpaths)
                        break

            # sorts the downloads folder
            else:
                if not down_path():
                    print(
                        "Oops! Looks like your Downloads folder is not at the default location"
                    )
                    while True:
                        path = input(colored("Enter your path manually: ", "blue"))
                        if os.path.exists(path):
                            break
                else:
                    path = down_path()
                    # path for the created folders
                    folderpaths = create_folders(path)
                    move_files(path, folderpaths)
            break


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


if __name__ == "__main__":
    main()
