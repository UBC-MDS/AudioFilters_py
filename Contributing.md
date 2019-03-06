# Contributing

In this project, we will be using Github to version control our work. Individual developers should fork the main repository into their own repository, and then, clone their forked repo to work locally. In order to upload their work, developers should push changes to their forked repository and send a pull request to at least one other developer for review.

The full instructions can be found at [Github guides to forking](https://guides.github.com/activities/forking/).

For individual workflows, developers are also allowed to use branching, as described in the [GitFlow guide](https://guides.github.com/introduction/flow/).

### Example of a contributing workflow:

Fork, then clone the repo:
```
    git clone https://github.com/UBC-MDS/AudioFilters_py.git
```

Make changes and then push your updates:
```
    git add .
    git commit -m "<[meaningful_commit_message]>"
    git push
```

If the `master` branch is ahead of the forked branch:
```
    git remote add upstream <original_repo_URL>
    git fetch upstream
    git merge upstream/master
```

Push to your fork and submit a pull request.

Contributing document derived from [Thoughtbot](https://github.com/thoughtbot/factory_bot_rails/blob/master/CONTRIBUTING.md).
