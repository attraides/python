#Git Essentials

#### ensure git installed and pc enviroment has acccess to directory where git is installed ie    $env:PATH += ";C:\Program Files\Git\cmd"

# Main Commands

## git init
<details>
<summary>Running this command will create a new directory .git in the root of your project. This .git directory contains all the information and objects required for your repository.</summary>
Functionality
The git init command sets up all the necessary files and directories that Git uses to keep track of things. The command initializes a new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.

Options
git init <directory>: Initializes a repository in the specified directory.
git init --bare: Creates a bare repository, generally used for hosting. No working directory is created.
Important Notes
After running git init, you'll still need to run git add to stage files and git commit to save the snapshot to your history.
The git init command is safe to run multiple times. If the repository already exists, running git init again won’t overwrite things.
Best Practices
It's a good idea to run git status after initialization to confirm that everything is set up correctly.
Typically, you only need to run git init once per repository, usually at the start of your project.
In summary, git init is the gateway to Git functionality. It’s what you run to get the ball rolling when you want to start tracking a new or existing project with Git. It's a crucial step for setting up a new repository or for adding version control features to a project that didn't previously have them.

Example:
PS C:\Users\t821306\OneDrive - Spark New Zealand\Vaughan\Scripts\gitTest2> git init
Initialized empty Git repository in C:/Users/t821306/OneDrive - Spark New Zealand/Vaughan/Scripts/gitTest2/.git/
</details>


## git add .
<details>
<summary>The period . tells Git to stage all changes in all files.</summary>

Functionality
When you make changes to your working directory, Git views these changes as unstaged. The git add command moves these changes to the staging area, preparing them for inclusion in the next commit. This allows you to group related changes into focused snapshots before sharing them.

Options
git add -A or git add --all: Stage all changes (modified, deleted, and new files)
git add -u: Stage modifications and deletions, but not new files
git add -p: Stage chunks of changes interactively
Important Notes
You can stage parts of a file instead of the entire file.
Using git add on an already staged file will update the staging area with the latest changes.
If you stage a file and then make additional changes, you'll need to run git add again to stage the latest changes.
Best Practices
Use git status before git add to see all changes that are unstaged.
Use git diff --staged after git add to see what has been staged (i.e., what will go into the next commit).


</details>


## git commit -m "Your commit message here"
<details>
<summary>The -m flag allows you to include a short message describing the changes you've made. This message is stored alongside the commit, making it easier to understand the intent of the changes later.</summary>
Functionality
The git commit command takes all staged changes (those added via git add) and packages them into a new commit. This new commit is a snapshot of your codebase at that point and becomes a part of the project history. Commits serve as checkpoints where individual files or an entire project can be safely reverted to when necessary.

Options
git commit -a: This will automatically stage all modified and deleted files before the commit.
git commit --amend: This allows you to modify the last commit. Be cautious when using this on shared branches.
git commit --squash: Combine several commits into a single commit for cleaner history.
Important Notes
Commit messages are crucial for understanding the codebase's history.
A commit is a local operation; it will not affect the remote repository until you run git push.
Best Practices
Use meaningful commit messages that clarify what changes were made and why.
Keep commits focused and small, capturing a single logical change.
Always run git status and git diff --staged before committing to review what will be included in the commit.
In summary, git commit serves as the mechanism for capturing versions or snapshots of your code, making it possible to track changes, revert to previous states, or collaborate with others. It’s the command that gives Git its power, enabling you to track the progress of your project and collaborate effectively with others.
</details>


## git log
<details>
<summary>Click to expand</summary>

displays the commit history

</details>

Example:
commit f2f3189255569912efa61e239edbda2e32780335 (HEAD)
Author: Vaughan Taylor <T821306@spark.co.nz>
Date:   Tue Sep 12 00:11:27 2023 +1200

    1st test delete commit

commit 40e1efdf3cb69bb0890c54b331d630694fc1c994 (master)
Author: Vaughan Taylor <T821306@spark.co.nz>
Date:   Mon Sep 11 23:59:32 2023 +1200

    1st test commit

## git checkout
<details>
<summary>Click to expand</summary>

The `git checkout` command is often used to switch between different branches, tags, or commits in a Git repository. However, it can also be used to manipulate the state of individual files or even the entire working directory. When you perform a `git checkout` to an older commit, you essentially move the `HEAD` pointer, which points to the latest commit on the current branch, to that older commit.

</details>


### What `git checkout` Does

- **Changes the HEAD**: The `HEAD` pointer changes to point to the commit hash you specify.
- **Updates the Working Directory**: The files in your working directory are updated to match the state of the repository at that commit.
- **Detaches HEAD**: If you checkout a specific commit (not a branch), the `HEAD` becomes "detached," meaning it's pointing directly to a commit and not a branch.

#### Why Deleted Files Aren't Returned

When you do a `git checkout` to an older commit, Git modifies your working directory to match the state of that older commit. This involves:

- **Updating Existing Files**: Any files that exist in both the older commit and the current commit are updated to their older versions.
- **Ignoring New Files**: Any files that didn't exist in the older commit but do exist now are left untouched.
- **Removing Files**: Interestingly, files that existed in the current commit but not in the older commit are not automatically deleted.
- **Not Restoring Deleted Files**: Files that were present in the older commit but have been deleted in the current commit are not automatically restored.

The reason deleted files are not returned is that the checkout operation only updates the tracked files that still exist in your working directory to match the state of the older commit. Git retains the changes you've made since that older commit but does not proactively restore deleted files.


## git restore
<details>
<summary>Click to expand</summary>

restoring files in the working directory or staging index to a particular state

</details>

Example:
git restore --source=404e4341238f4870230be7e5f72d68501adf5018 youtube_DL_GUI_+progressbar.py      
