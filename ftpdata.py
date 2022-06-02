from ftplib import FTP
import os

# 1. Set the directory you would like to download the files to
# Colocar o caminho da pasta onde os arquivos ficarão armazenados.
destdir = ''

# 2. Set the path to the FTP directory that contains the data you wish to download.
# https://nsidc.org/data/g02135
directory = '/DATASETS/NOAA/G02135/north/daily/data'

# 3. Set the password which will be your email address
# Colocar o email para realizar o donwload dos arquivos
password = ''

# FTP server
ftpdir = 'sidads.colorado.edu'

#Connect and log in to the FTP
print('Logging in')
ftp = FTP(ftpdir)
ftp.login('anonymous',password)

# Change to the directory where the files are on the FTP
print('Changing to '+ directory)
ftp.cwd(directory)

# Get a list of the files in the FTP directory
files = ftp.nlst()
files = files[2:]
print(files)

#Change to the destination directory on own computer where you want to save the files
os.chdir(destdir)

#Download all the files within the FTP directory
for file in files:
    print('Downloading...' + file)
    ftp.retrbinary('RETR ' + file, open(file, 'wb').write)

#Close the FTP connection
ftp.quit()