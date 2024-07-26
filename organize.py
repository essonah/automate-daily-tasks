import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"{directory} does not exist")
        return
    
    file_types = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css'],
    }
    
    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    
    # Create the "Others" folder if it doesn't exist
    others_folder = os.path.join(directory, 'Others')
    if not os.path.exists(others_folder):
        os.mkdir(others_folder)
    
    # Move files to their respective folders
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            moved = False
            for folder, extensions in file_types.items():
                if item.endswith(tuple(extensions)):
                    destination = os.path.join(directory, folder, item)
                    shutil.move(item_path, destination)
                    moved = True
                    break

            if not moved:
                destination = os.path.join(others_folder, item)
                shutil.move(item_path, destination)

    print("Files organized successfully!")

if __name__ == '__main__':
    directory = os.path.expanduser("~/Downloads")
    organize_files(directory)
