
## Introduction

*Nerfherder* is a collection of Python hacks for grading GitHub Classroom
repositories. ([So-named](http://starwars.wikia.com/wiki/Nerf_herder) because
it is a flaky thing that wrangles other flaky things.)

## Requirements

 - Python 3
 - git commandline tools
 - PyGithub <https://pypi.python.org/pypi/PyGithub/1.35>
 - TravisPy <https://pypi.python.org/pypi/TravisPy>

## Dependency Installation

You need the `git` command-line tools. On Debian- or Ubuntu-based Linux
environments, use

`[~]$ sudo apt install git`

The following command should prepare your Python environment:

`[~]$ pip3 install PyGithub TravisPy keyring`

## Cloning Student Repositories

Assuming we have cloned the nerherder repo to `~/nerfherder`, and we
already created a directory for grading at `~/grading`,

`[~/grading]$ ~/nerfherder/clone-organization kevinwortman CSUF-CPSC-335-FA18`

(Note: the first argument is a GitHub username, **not email address**, so there
  is no @domain.com; and, give the **organization name**, not the URL
  to the organization, so there is **no https://** .)

This will prompt you for your GitHub password once, and then pull each
repo owned by the GitHub organization `CSUF-CPSC-335-FA18`.

By default this command will skip repos that are already present locally. This
is an optimization to avoid re-downloading old submissions which are unlikely
to change after they have already been graded. If instead you want to download
**every** repository, including ones that are already here, use the `--replace`
switch.


`[~/grading]$ ~/nerfherder/clone-organization kevinwortman CSUF-CPSC-335-FA18 --replace`
