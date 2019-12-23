# Auto Backup

This script is setup to listen to a Folder and automatically backup any file when a modification is made to the filesystem. Allowing for simple Version Control to be kept on files on a local filesystem/network file system. 

Files are successfully renamed with the following format: 
```
[timestamp]_[original_filename].[extension]
```

Example: 

```
10-12-2019 22.50.00_mattncott.docx
```

## Required Dependencies
Please install the following via pip before using the App
* [Watchgod](https://github.com/samuelcolvin/watchgod)

## Contributing
If you wish to contribute to this project, then your help is very welcome! 