# Overview
Here, we need to configure two things (for each clone on slaves) - 
1. A python server on the client (system which will have the clone of the repository, assuming it is at the IP 54.180.86.51) with a bash script to do 'git pull'
2. A webhook on gitlab to tell the python server created in the previous step that it is now time to pull

# Step 1
Download git_hook.py and git_pull.sh on your client system.

Place the files in a folder called 'python_pull' inside /root/repos folder - this path can be changed if required. If not required, move on to Step 2.
Instructions on changing it are as follows - 
1. In git_hook.py, Line 26 - change the path of the `subprocess.call` function
Currently, the value here is
``` subprocess.call(["/root/repos/python_pull/git_pull.sh", repo_name]) ```
Here, `"/root/repos/python_pull/git_pull.sh"` denotes the path of the git_pull.sh file. If you have placed this file at some other location, then you can mention that path here.

# Step 2
Clone your target repository on the client system

Assuming your target repository is `http://206.189.40.80/root/gitlabpw`, clone it using access token as follows -
```git clone http://root:1JBH2XWxv9Btx4RbbnF1@206.189.40.80/root/gitlabpw.git```

You can create this token at http://206.189.40.80/profile/personal_access_tokens

You have to clone it in the folder /root/repos - this path can be changed if required. If not required, move on to the next step.
Instructions on changing it are as follows -
1. In git_pull.sh, Line 3 - change the path of the `cd` command
```cd /root/repos/$1 && git fetch --all && git checkout --force "origin/master"```

Here `cd /root/repos/$1` denotes the path where `git_pull.sh` expects the cloned repository to be present in a folder denoted by `$1` which is explained in the next step.

# Step 3
Set up the webhook by following the steps in the image below

![Add Gitlab Webhook](add_gitlab_webhook.png)

In this image, the value after `payload`, in this case `gitlabpw` i.e. the name of the repository, becomes $1 in git_pull.sh of the previous step.


