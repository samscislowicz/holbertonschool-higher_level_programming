Population script for Holberton School projects
By Tim Britton, updated 11/Oct/2016

Population script touches out empty files, based on the project names given on the intranet, and adds u+x permissions to each. Then, it creates your README.md, and appends the project names to the README.md, meaning you'll just need to write a description.

Populate needs to take the HTML source of the project page (the page with the automated check buttons) as an argument. Easiest way is to just go to the project page, view source, select all, and paste them into a file. Then, run populate against the file, in the directory you want to create files in.

Automatic directory check and automatic page downloading coming next.