# Code and Documentation Update Guide

### Code Update Instructions

1. **Push Code Changes from Server to GitHub**  
   After modifying the code on your server, push the code to GitHub:
   ```bash
   git add .
   git commit -m "your comment"
   git push <your-branch>:<github-branch>
   # if it fails, try
   git push <your-branch>:<github-branch> --force

2. **Add Submodule**  
   If you want to make contributions to the PaleoDA_OL, try to add it as a submodule
   ```bash
   cd PaleoDA
   git submodule add https://github.com/<your-repository> <submodule-name>

3. **Pull Updated Code from GitHub to Server**  
    Once the code on GitHub is updated (by you or others), update the code on your server:
    ```bash
    cd PaleoDA
    git submodule update --remote <submodule-name>
    git add <submodule-name>
    git commit -m "your comment"
    git push <your-branch>:<github-branch>

### Documentation Update Instructions
1. **Preview HTML Documentation Locally**  
   Open the HTML documentation locally using a live server to review your changes:
   ```bash
    cd PaleoDA_docs/build/html
    live-server

2. **Edit Documentation Source Files**  
   To add or modify documentation content, change to the source directory, edit the relevant `.rst` files, then return to the main documentation directory to rebuild the HTML:
   ```bash
    cd PaleoDA_docs/source/pages
    # Make edits to the .rst files
    cd ../../
    make clean
    make html

3. **Deploy Updated Documentation to GitHub**  
   Copy the newly generated HTML files from `PaleoDA_docs/build/html` to `PaleoDA_docs/docs` and push the updated files to GitHub:
   ```bash
   cp -r PaleoDA_docs/build/html/* PaleoDA_docs/docs/
   git add *
   git commit -m "your comment"
   git push <your-branch>:<github-branch>