## Git Cheat Sheet

### Initializing a repository
- `git init`: Initializes a new repository in the current directory

### Staging changes
- `git add`: Adds changes to the staging area
- `git reset`: Removes changes from the staging area

### Committing changes
- `git commit -m "message"`: Commits changes with the specified message
- `git commit -a -m "message"`: Commits all changes, including deletions, with the specified message

### Viewing the commit history
- `git log`: Shows the commit history
- `git diff`: Shows the difference between the working directory and the last commit

### Working with branches
- `git branch`: Lists all branches
- `git branch branch_name`: Creates a new branch with the specified name
- `git checkout -b branch_name`: same as git branch branch_name && git checkout branch_name
- `git checkout branch_name`: Switches to the specified branch
- `git merge branch_name`: Merges the specified branch into the current branch
- `git branch -d branch_name`: Deletes the specified branch

### Synchronizing with a remote repository
- `git clone`: Clones a remote repository
- `git pull`: Fetches changes from the remote repository and merges them into the current branch
- `git push`: Pushes changes to the remote repository

### Push an existing repository
- `git remote add origin git_link`: add the current local repository to the remote one
- `git push -u origin --all`: push the files and changes to the remote repository

You can find more information and options for each command by running `git [command] --help`.
