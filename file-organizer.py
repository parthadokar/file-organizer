import os,shutil
from pathlib import Path

def organizer():
    # File Path
    path = r'C:\Users\adoka\Downloads'
    # Specify Extensions to check
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
        '.webp', '.svg', '.ico', '.heic', '.heif', '.raw', '.arw',
        '.cr2', '.nef', '.orf', '.sr2', '.psd', '.ai', '.eps',
        '.indd','.pdf', '.doc', '.docx', '.odt', '.rtf', '.txt', '.md',
        '.tex', '.wpd', '.xls', '.xlsx', '.ods', '.csv',
        '.ppt', '.pptx', '.odp', '.epub', '.mobi')
    # Loop to check for individual file matching the extension
    for file in os.listdir(path):
        if file.endswith(extensions):
            print(f'File found: {file}')
        else:
            print(f'File not found: {file}')

    # Specify Folders to check
    folders = ('Images', 'Docs')
    # Loop to check for individual folder
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
            print(f'Folder Created: {folder}')
        else:
            print(f'Folder Already Exists: {folder}')

    # Copy files to folder 
    for file in os.listdir(path):
        # Extensions to check for 
        image_extensions = (
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
        '.webp', '.svg', '.ico', '.heic', '.heif', '.raw', '.arw',
        '.cr2', '.nef', '.orf', '.sr2', '.psd', '.ai', '.eps', '.indd')
        document_extensions = (
        '.pdf', '.doc', '.docx', '.odt', '.rtf', '.txt', '.md',
        '.tex', '.wpd', '.xls', '.xlsx', '.ods', '.csv',
        '.ppt', '.pptx', '.odp', '.epub', '.mobi')
        # Loop and copy the file with appropraite files to desired folders
        if file.endswith(document_extensions):
            src = os.path.join(path,file)
            dest = os.path.join(path,'Docs',file)
            shutil.copy(src,dest)
            print(f'File moved: {file}')
        elif file.endswith(image_extensions):
            src = os.path.join(path,file)
            dest = os.path.join(path,'Images',file)
            shutil.copy(src,dest)
            print(f'File moved: {file}')
        else:
            print('No change')

if __name__ == '__main__':
    organizer()