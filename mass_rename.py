import os

# This script renames every file in a given folder from l_english.yml to l_gernam.yml
# Currently only works in the specified folder, not subfolders
pathSpecified = "C:/Users/PUT_YOUR_USER_HERE/Documents/Paradox Interactive/Crusader Kings III/mod/ek2german/localization/replace/german/struggles"

def replace(fpath):
    filenames = os.listdir(pathSpecified)
    os.chdir(fpath)
    for file in filenames:
        if '.' not in file:
            replace(file)
        os.rename(file, file.replace('l_english', 'l_german'))

fpath = pathSpecified
replace(fpath)