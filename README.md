# Forganiser

A nifty tool to sort your messy folders. Originally created by [@Cheesemaafia/@Jigyasu](https://github.com/cheesemaafia/forganiser). Current version: 1.2

This fork improves upon it a bit in the following ways:

- includes more file extensions that will be automatically sorted
- more default folder categories/names such as ebooks, comics, & subtitles.
- refactored to be a easier to add/remove folders if you want to customise it
- file name collision error handling inserts current date & time into the file name (e.g. `duplicate title.jpg` would become `duplicate title (2023-01-01 12:00:00).jpg`
- stronger cross OS compatibility written into it,
- more documentation (the original was easy to understand & customise; I hope to keep it that way).

## Screenshots

![App Screenshot](https://i.postimg.cc/bNn0gxW9/Screenshot-from-2022-09-02-17-57-49.png)

## Documentation

Forganiser is a fast and lightweight folder sorter. It is written entirely in Python and mostly uses modules that come pre-installed with it.

It sorts the downloads folder or to sort some other folder depending on user input.

If the user chooses to sort the downloads folder, it automatically detects the path on the operating system and prompts to enter the path to downloads manually if it's not located at the default location.

Users can choose the second option and directly provide the path to any other folder that they want to sort, any path provided passes through some checks to confirm if the destination actually exists on the system and if it doesn't then the user gets a reprompt.

After a path is selected, the program creates several subfolders inside the folder namely Music, Videos, Pictures, Documents, Application and Archives, etc.

It then sorts all the files present in the parent folder into several different groups based on their extensions and moves them in the respective subfolders.
