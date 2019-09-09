import sys, os
# Import helper functions
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'Functions'))
import Factory
# Import user configuration
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'Config'))
import Config

# Obtains latest Revit Dev Sandbox
def CopyAndUnzipLatestDevSandbox():
    fullSourcePath = Factory.CombinePath(Config.RevitDevSandboxDestination, Config.RevitDevSandboxFolderName)
    Factory.DeleteFolderAndContents(fullSourcePath)
    Factory.CreateDirectory(fullSourcePath)
    zipfile = Factory.GetLatestZipFileWithMaskInDir(Config.RevitDevSandboxMask, Config.RevitDevSandboxSource)
    fullzippath = Factory.CombinePath(Config.RevitDevSandboxSource, zipfile)
    Factory.CopyFileToDir(fullzippath, Config.RevitDevSandboxDestination)
    Factory.Unzip(fullzippath, fullSourcePath)
    journalsFolder = Factory.CombinePath(fullSourcePath, "Journals")
    Factory.CreateDirectory(journalsFolder)

def InstallRevit2019():
    if not Factory.IsInstalled("Autodesk Revit 2019"):
        Factory.InstallWithArgs(Config.Revit2019InstallPath, Config.Revit2019InstallArgs)