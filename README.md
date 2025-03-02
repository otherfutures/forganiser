# Forganiser

A nifty tool to sort your messy files. Originally created by [@Cheesemaafia/@Jigyasu](https://github.com/cheesemaafia/forganiser). Current version: 1.6

This fork improves a bit upon the original in the following ways:

- includes more file extensions that will be automatically sorted
- more default folder categories/names such as ebooks, comics, & subtitles.
- refactored to be a easier to add/remove folders if you want to customise it
- file name collision error handling
- error handling for folder name typos/mismatches
- stronger cross OS compatibility written into it,
- imports only native libraries
- uses sets instead of lists (in practice, however, the original felt instantaneous)
- more documentation (the original was easy to understand; I hope to keep it that way).

## Screenshots

![App Screenshot](https://i.postimg.cc/bNn0gxW9/Screenshot-from-2022-09-02-17-57-49.png)

## Documentation

Forganiser is a fast and lightweight folder sorter. It is written entirely in Python and uses native libraries.

It sorts the downloads folder or some other folder depending on user input.

If the user chooses to sort the downloads folder, it automatically detects the path on the operating system and prompts to enter the path to downloads manually if it's not located at the default location.

Users can choose the second option and directly provide the path to any other folder that they want to sort, any path provided passes through some checks to confirm if the destination actually exists on the system and if it doesn't then the user gets a reprompt.

After a path is selected, the program creates several subfolders inside the folder namely Music, Videos, Pictures, Documents, Application, and Archives, etc.

It then sorts all the files present in the parent folder into several different groups based on their extensions and moves them in the respective subfolders.
