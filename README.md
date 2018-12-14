
## Introduction

*Nerfherder* is a collection of Python hacks for grading GitHub Classroom
repositories. ([So-named](http://starwars.wikia.com/wiki/Nerf_herder) because
it is a flaky thing that wrangles other flaky things.)

## Requirements

 - Python 3
 - git commandline tools
 - PyGithub <https://pypi.python.org/pypi/PyGithub/1.35>

## Dependency Installation

You need the `git` command-line tools. On Debian- or Ubuntu-based Linux
environments, use

`[~]$ sudo apt install git`

The following command should prepare your Python environment:

`[~]$ pip3 install PyGithub keyring`

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

## Importing Groups to Moodle

Our workflow uses GitHub Classroom to assign and collect programming projects,
and [Moodle](https://moodle.org/) for grade calculation and distribution.
Ordinarily we allow students to work in groups of 1-3 on these projects.
Moodle supports team assignments, but there is no direct link between the
user account and group information in GitHub, and the notion of teams in
Moodle. It might be possible to create such a link using
[Moodle`s PHP API](https://docs.moodle.org/dev/Core_APIs), but we presently
do not have the resources to undertake that project.

In the mean time, the `create-groups-csv` and `group-member-emails` scripts
semi-automate the process of exporting GitHub group information into a format
that Moodle understands.

We require students to indicate their chosen groups by editing a README.md
that contains their school-issued email addresses, and no other email addresses.
This approach is not quite ideal since it involves unstructured data, but
it works.

These tools expect that you use either GitHub Classroom Assistant, or the
`clone-organization` script in this repository, to download submissions.
These tools create a **submission directory** which is a directory that
contains cloned student repositories.

`create-groups-csv` examines a submission directory, filters for actual
git repos that contain a .git, and creates a CSV file that lists each
repo name as a Moodle group name. You may give an optional prefix that is
applied to all group names, we use something like project-1 and project-2 so that
groups for each project are separated alphabetically. This CSV file is
understood by the Import Groups feature in Moodle.

Importing these groups will make them exist in Moodle, but each group will
be empty with no students in the group. You need to use the Moodle web
interface to assign students into these groups.

`group-member-emails` finds apparent git repos inside a submission directory,
and for each, searches `README.md` for email addresses (matched by a regular
  expression), and prints out the results in a compact format.

You can run `group-member-emails`, leave the results in a terminal window,
open a browser to the groups page in Moodle, and use the email addresses to
find student accounts and assign them into groups. While this is somewhat
tedious, it is still more agreeable than doing this entire process manually,
or leaving Moodle unaware of groups.

## MOSS Plagiarism Detection

[MOSS](http://theory.stanford.edu/~aiken/moss/) is a web service that identifies
similarities in source code which might indicate plagiarism.

In order to use
MOSS, you will need to create an account, and in the last step of that process
the server will email a submission script. The MOSS authors
ask for that script to not be publicized, so we are not duplicating the
script's functionality. Instead we created `moss-submit` which is a lightweight
glue-code script that makes it easier to
submit code from a GitHub-based submission directory.

Per the [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)
principle, `moss-submit` is based upon some simplifying assumptions:

* student submissions are organized in a submission directory (as defined above)
* there is a repo with starter code, outside the submission directory,
  that has been cloned locally
* only one source file (per repo) is checked for similarity, i.e. there is
  one file such as `main.cpp` that contains all substantial student work
* you have already created a MOSS account and followed their instructions
  to save the submission script locally

If you are checking a C++ assignment, where students edit `implementation.hpp`,
your MOSS script is in `~/Documents/moss`, your starter code is cloned to
`~/Documents/project1-starter`, and you have downoaded student submission repos
to `~/Documents/project1-submissions`, then the following command will submit
to MOSS:

  `[~]$ ~/nerfherder/moss-submit --filename implementation.hpp --moss ~/Documents/moss --skeleton ~/Documents/project1-starter --dir ~/Documents/project1-submissions`

As described in the online help, you can override the programming language with
the `--language` flag.
