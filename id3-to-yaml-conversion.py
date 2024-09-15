import os  # For file and directory operations
from mutagen import File  # For handling audio files
from mutagen.easyid3 import EasyID3  # For reading ID3 tags
from mutagen.id3 import ID3, COMM  # For handling ID3 comments
import yaml  # For reading and writing YAML files
import datetime  # For formatting duration

def read_id3_data():
    """
    Reads ID3 metadata from MP3 files in the specified directory and returns a list of metadata dictionaries.
    """
    audio_directory = 'audio'  # Directory containing MP3 files
    id3_data = []  # List to store metadata dictionaries

    # Iterate over all files in the audio directory
    for file in os.listdir(audio_directory):
        if file.endswith('.mp3'):  # Process only MP3 files
            file_path = os.path.join(audio_directory, file)  # Full path to the MP3 file
            audio_file = File(file_path)  # Load the audio file using mutagen
            audio = EasyID3(file_path)  # Load ID3 tags using EasyID3
            id3 = ID3(file_path)  # Load ID3 tags using ID3
            
            title = audio.get('title', ['Unknown'])[0]  # Extract the title from the ID3 tags
            
            comments = 'Unknown'  # Extract comments from the ID3 tags
            if 'COMM::eng' in id3:
                comm_frame = id3.getall('COMM::eng')
                if comm_frame and isinstance(comm_frame[0], COMM):
                    comments = comm_frame[0].text[0]
            
            duration_seconds = audio_file.info.length if audio_file.info else 0  # Get the duration of the audio file in seconds
            duration = str(datetime.timedelta(seconds=int(duration_seconds)))  # Format duration as HH:MM:SS
            
            file_size = os.path.getsize(file_path)  # Get the file size in bytes
            formatted_file_size = f"{file_size:,}"  # Format file size with commas

            creation_time = os.path.getctime(file_path)  # Get the creation time of the file
            creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')  # Format creation date

            # Create a dictionary with the extracted metadata
            data = {
                'title': title,
                'description': comments,
                'creation_at': creation_date,
                'file': file_path,
                'duration': duration,
                'length': formatted_file_size
            }
            id3_data.append(data)  # Add the metadata dictionary to the list

    return id3_data

def write_to_yaml(data, filename='id3-metadata.yaml'):
    """
    Writes the given data to a YAML file.
    
    Parameters:
    data (list): List of metadata dictionaries to write to the file.
    filename (str): Name of the YAML file to write to.
    """
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

# Read ID3 data from MP3 files
metadata = read_id3_data()

# Write the metadata to a YAML file
write_to_yaml(metadata)