from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move

import logging

# Describing the source folder and the folder to move in the files
source_dir = "C:\Users\windowsz\Downloads"
dest_dir_sfx = "D:\Downloads\Sounds"
dest_dir_music = "D:\Downloads\Music"
dest_dir_video = "D:\Downloads\Videos"
dest_dir_image = "D:\Downloads\Images"
dest_dir_documents = "D:\Downloads\Documents"

# Suppoeted Image extensions
image_extensions = [
    '.jpg', '.jpeg', '.png', '.gif', '.tiff', '.tif', '.bmp', '.raw',
    '.psd', '.ai', '.eps', '.svg', '.pdf', '.ico', '.webp', '.heic', '.heif',
    '.jp2', '.nef', '.cr2', '.arw', '.dng', '.pbm', '.pgm', '.ppm'
]

audio_extensions = [
    '.mp3', '.wav', '.flac', '.aac', '.wma', '.ogg', '.m4a', '.mp4', '.webm', '.mid', '.midi'
]

video_extensions = [
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp', '.rm', '.swf'
]

document_extensions = [
    '.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.csv', '.ppt', '.pptx'
]


def make_unique(dest, name):
    filename, extensions = splitext(name)
    counter = 1
    # if file exists all number to the end of the file name
    while exists(f"(dest)/(name)"):
        name = f"{filname}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(f"(dest)/(name)"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

def on_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_audio_files(entry, name)
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)

#Checks all audio files
def check_audio_files(entry, name):
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            if entry.stat().st_size < 10_000_000 or "SFX" in name: # 10 Megabytes
                dest = dest_dir_sfx
            else:
                dest = dest_dir_music
            move_file(dest, entry, name)
            logging.info(f"Moved audio file: {name}")

#Checks all video files
def check_video_files(entry, name):
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")


#Checks all Image files
def check_image_files(entry, name):
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

#Checks all Document files
def check_document_files(entry, name):
    for document_extension in document_extensions:
        if name.endswith(document_extension) or name.endswith(document_extension.upper()):
            move_file(dest_dir_documents, entry, name)
            logging.info(f"Moved document file: {name}")
        