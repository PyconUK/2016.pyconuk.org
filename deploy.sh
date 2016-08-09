#!/bin/bash

set -e

if [[ $TRAVIS = "true" ]]; then
	if [[ $TRAVIS_BRANCH != "master" || $TRAVIS_PULL_REQUEST != "false" ]]; then
		# Bail out if Travis is building a branch or is building a Pull Request.
		echo "Not deploying!"
		exit 0
	fi

	REPO_URL="https://PyConUK-user@github.com/PyconUK/2016.pyconuk.org"

	# Set up credentials for pushing to GitHub.  $GH_TOKEN is configured via Travis web UI.
	git config --global credential.helper "store --file=$TRAVIS_BUILD_DIR/git-credentials"
	echo "https://PyConUK-user:$GH_TOKEN@github.com" > $TRAVIS_BUILD_DIR/git-credentials

	# Set up config for committing.
	git config --global user.name "Travis"
	git config --global user.email "no-reply@pyconuk.org"
else
	REPO_URL="git@github.com:PyconUK/2016.pyconuk.org.git"
fi

echo "Deploying!"

# Build the site into the output directory
make build

# Remove gh-pages directory and replace it with the current tip of the gh-pages branch.
rm -rf gh-pages
git clone $REPO_URL --branch gh-pages --single-branch gh-pages

# Replace the contents of the gh-pages directory with the newly-built site
rm -rf gh-pages/*
cp -r output/* gh-pages

# Add, commit, and push any changes.
cd gh-pages
git add .
git commit -m "[skip ci]  Auto-commit.  Built latest changes."
git push $REPO_URL gh-pages
