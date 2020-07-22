# Git commands

- Manages set of tracked repositories: `git remote`
- Shows remote url of the tracked repositories: `git remote -v`
- Adds a remote (`origin` it's a default term for the remote repo alias, but it can be anything): `git remote add origin https://github.com/user/repo.git`
- Adds an upstream (`upstream` it's a default term for the forked repo alias, but it can be anything): `git remote add upstream git@github.com:user/repo.git`
- Remove files from the working tree and from the index (ideal when you change .gitignore): `git rm --cached -r .`
- Move repo from a server to another:
```
git clone --mirror <url_of_old_repo>
cd <name_of_old_repo>
git remote add new-origin <url_of_new_repo>
git push new-origin --mirror
```

[<- Go Back](README.md)