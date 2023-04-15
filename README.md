
# Forganiser

A nifty tool to sort your messy folders. Created by [@Cheesemaafia/@Jigyasu](https://github.com/cheesemaafia/forganiser). 

This fork improves upon it a bit, by including more file extensions that will be automatically sorted & some more default folder categories/names such as ebooks & subtitles. It also has file name collision error handling that inserts the current date & time into the file name. 

These changes are mostly done for my own use case, & I thought I might as well share them.


## Screenshots

![App Screenshot](https://i.postimg.cc/bNn0gxW9/Screenshot-from-2022-09-02-17-57-49.png)


## Documentation

Forganiser is a fast and lightweight folder sorter. It is written entirely in Python and uses most of the modules that comes pre-installed with it.

It provides the user with two options, that are, to sort the downloads folder or to sort some other folder.

If the user chooses to sort the downloads folder, it automatically detects the path on the operating system and prompts to enter the path manually if it's not located at the default location.

Users can even choose the second option and directly provide the path to any other folder that they want to sort, any path provided passes through some checks to confirm if the destination actually exists on the system and if it doesn't then the user gets a reprompt.

After a path is selected, the program creates several subfolders inside the folder namely Music, Videos, Pictures, Documents, Application and Archives.

It then sorts all the files present in the parent folder into several different groups based on their extensions and moves them in the respective subfolders.
