import os
import shutil
from datetime import datetime


def move_files(path, music, loose_videos, pictures, programs, documents, applications, archives, subtitles, ebooks):

    music_ext = [
        ".mp3",
        ".m4a",
        ".wav",
        ".wma",
        ".aac",
        ".flac",
        ".alac",
        ".ogg"
    ]

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
        ".ogg"
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
        ".avif"
    ]

    programs_ext = [
        ".py", 
        ".java", 
        ".c", 
        ".cpp", 
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
        ".csv"
        ".sql", 
        ".class", 
        ".jar", 
        ".dll"
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
        ".odt"
    ]

    applications_ext = [
        ".exe",
        ".apk",
        ".deb",
        ".app",
        ".msi",
        ".dmg",
        ".rpm"
    ]

    archives_ext = [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2"
        
    ]

    subtitles_ext = [
        ".srt", 
        ".sub", 
        ".ass", 
        ".vtt", 
        ".stl"
    ]

    ebooks_ext = [
        ".epub",
        ".mobi",
        ".djv",
        ".azw", 
        ".azw3", 
        ".prc"
    ]

    files = os.listdir(path)

    for file in files:

        filepath = f"{path}/{file}"
        ext = os.path.splitext(filepath)[1].lower()

        try:
            if ext in music_ext:
                shutil.move(filepath, music)
            elif ext in videos_ext:
                shutil.move(filepath, loose_videos)
            elif ext in pictures_ext:
                shutil.move(filepath, pictures)
            elif ext in programs_ext:
                shutil.move(filepath, programs)
            elif ext in documents_ext:
                shutil.move(filepath, documents)
            elif ext in applications_ext:
                shutil.move(filepath, applications)
            elif ext in archives_ext:
                shutil.move(filepath, archives)
            elif ext in subtitles_ext:
                shutil.move(filepath, subtitles)
            elif ext in ebooks_ext:
                shutil.move(filepath, ebooks)

        except shutil.Error as e:
            # If name collision, split the file name and extension, rename the file with current date & time
            new_filepath = f"{path}/{os.path.splitext(file)[0]} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}){ext}"
            shutil.move(filepath, new_filepath)

    return 0
