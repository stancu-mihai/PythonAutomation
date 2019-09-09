import glob, os, shutil, subprocess, winreg, zipfile

# Gets data by name for a previously opened registry key
def GetDataForKeyAndName (regConn, registryKey, searchName):
    try:
        row = 0
        while 1:
            reg_key = winreg.OpenKey(regConn, registryKey)
            name, value, type = winreg.EnumValue(reg_key, row)
            if(name == searchName):
                return value
            row +=1
    except:
        return ""

# Checks if a program is installed
def IsInstalled( program ):
    x86 = False
    x64 = False
    locations = [
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall", 
        r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    regConn = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    for location in locations:
        try:
            programItem = 0
            while 1:
                reg_key = winreg.OpenKey(regConn, location)
                regKeyName = winreg.EnumKey(reg_key, programItem)
                programDisplayName = GetDataForKeyAndName(regConn, location + "\\" + regKeyName, "DisplayName")
                if program in programDisplayName:
                    x86 = True
                programItem += 1
        except WindowsError:
            print()

    return [x86] or [x64]

# Installs an app with given arguments
def InstallWithArgs(fullpath, arguments):
    subprocess.run(fullpath + arguments, shell = True)

# Obtains full path of a file with a certain mask in a specified directory
def GetLatestZipFileWithMaskInDir(mask, dir):
    fileList = glob.glob(dir + "\\" + mask)
    ret = max(fileList, key = os.path.getctime)
    return ret

# Copies a file to a directory
def CopyFileToDir(file, dir):
    shutil.copy2(file, dir)

# Unzips into a directory
def Unzip(fullZipPath, dir):
    zipRef = zipfile.ZipFile(fullZipPath, 'r')
    zipRef.extractall(dir)
    zipRef.close()

# Combines paths
def CombinePath(path1, path2):
    return os.path.join(path1, path2)

# Delete folder and contents
def DeleteFolderAndContents(fullFolderPath):
    shutil.rmtree(fullFolderPath)

# Creates a directory
def CreateDirectory(fullDirPath):
    os.mkdir(fullDirPath)