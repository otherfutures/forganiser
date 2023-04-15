import os


def create_folders(path):
    music = f"{path}/Music"
    if not os.path.exists(music):
        os.mkdir(music)
    
    videos = f"{path}/Videos"
    if not os.path.exists(videos):
        os.mkdir(videos)
    
    pictures = f"{path}/Pictures"
    if not os.path.exists(pictures):
        os.mkdir(pictures)
    
    programs = f"{path}\\Apps\\Programs"
    if not os.path.exists(programs):
        os.mkdir(programs)
    
    documents = f"{path}/Documents"
    if not os.path.exists(documents):
        os.mkdir(documents)
    
    applications = f"{path}/Apps"
    if not os.path.exists(applications):
        os.mkdir(applications)
    
    archives = f"{path}/Archives"
    if not os.path.exists(archives):
        os.mkdir(archives)
    
    subtitles = f"{path}/TV Series/Subtitles"
    if not os.path.exists(subtitles):
        os.mkdir(subtitles)   
    
    ebooks = f"{path}/Documents/eBooks" 
    if not os.path.exists(ebooks):
        os.mkdir(ebooks) 

    return (music, videos, pictures, programs, documents, applications, archives, subtitles, ebooks)
