#!/bin/bash

# The commit hash of cf
CF_COMMIT="efbd3ff3085c60579113a13fdae21ca23432b9ab"

# Function to recreate repository state at a given commit
recreate_state() {
    commit=$1
    git checkout $commit -- .
    git add .
    GIT_COMMITTER_DATE="$(git show -s --format=%ci $commit)" \
    git commit -c $commit
}

# Start with an empty state
git checkout --orphan new_history
git rm -rf .

# Recreate the state just before cf
PARENT_COMMIT=$(git rev-parse $CF_COMMIT^)
recreate_state $PARENT_COMMIT

# Get all commits from cf onwards
COMMITS=$(git rev-list --reverse $CF_COMMIT..v4)

# Recreate state for each commit from cf onwards
for commit in $CF_COMMIT $COMMITS
do
    recreate_state $commit
done
