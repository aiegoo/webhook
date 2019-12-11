import git
from git.refs.tag import TagReference
from sendemail import send_email

repo = git.Repo('/home/pawan/Desktop/DEMO/')

remote = repo.remotes.origin
remote.fetch()
print(repo.head.commit == remote.refs.master.commit)
if repo.head.commit != remote.refs.master.commit:
    remote.pull()
    print('pulled')
print(repo.head.commit == remote.refs.master.commit)
# print(remote.refs.master.commit)
# print(repo.head.commit)
# print(repo.head.commit.message)
tagref = TagReference.list_items(repo)[-1]
print(tagref.tag.message)
