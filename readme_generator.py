# SOURCE expanding upon Tralehtek


"""Automating README.md generation."""
import glob
import os
from argparse import ArgumentParser

# TODO update to include repo purpose or a blurb about its goal
# TODO update script to prompt user to input repository_name
# TODO update to include reference of data folders vs datafiles
# TODO update to include '#TODO' parsing as future features
# TODO update to include tree of code


repository_name = 'Compositional Notebook'


class GitRepoReadMe:
	"""
	a class to ingest github and user data from project code and create README.md file
	"""
	github_user_name = 'datatalking'
	version = '0.0.1'
	"A Github Repository ReadMe Generator. "
	_header = f"""[![Build Status](https://travis-ci.com/{1}/{0}.svg?branch=master)](https://travis-ci.com/{1}/{0})
    [![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
    [![Organization](https://img.shields.io/badge/Org-{github_user_name}-blue.svg)](https://github.com/datatalking)
    [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
    [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](
    https://pypi.python.org/pypi/ansicolortags/)
    [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/
    {1}/pull/)
    [![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/
    {1}/{0}/pull/)
    [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/{1}/{0}).

    # {0}.
    """
	_author = "[![{1}](https://img.shields.io/badge/Author-{1}-cyan.svg?style=for-the-badge)](https://github.com/{1})"
	_purpose = """# Purpose ###  PurposeTo automatically create README.md files for project"""
	_cloning = """
    ### Setup and Usage

	open bash or zsh terminal
    ```
    git clone https://github.com/{1}/{0}.git
    cd {0}
    pip install -r requirements.txt
    ```
    """

	_scripts = "\n".join(glob.glob("*", recursive=True))

	def add_contribs(self):
		"""
		Add contributors from a list of github usernames
		:return:
		"""
		contribs = ['datatalking', '{1}']
		h = "\n\n# Contributors. \n\n"
		return h + "\n".join(["* [%s](%s)" % (r, "https://github.com/" + r) for r in contribs])

	def link_scripts(self):
		"""
		generate links to files in the Github project.
		:return:
		"""
		base_url = "https://github.com/{1}/{0}/blob/master/"
		return "\n".join(["* [%s](%s)" % (r, base_url + r) for r in glob.glob("*", recursive=True)])

	_scripts = link_scripts()

	def future_features(self):
		"""
		parse # T O D O from document
		:return:
		"""
		pass

	print("""[ ] - TODO update to include repo purpose or a blurb about its goal

	[ ] - TODO update script to prompt user to input repository_name
	
	[ ] - TODO update to include reference of data folders vs datafiles
	
	[ ] - TODO update to include '#TODO' parsing as future features
	
	[ ] - TODO update to display tree of code
	
	[ ] - TODO update to autoparse '# TODO' into README.md
		""")

	def gen_RMe(rp_name, rp_author):
		"""
		generate markdown text with the defined templates and repo_name and author_username.
		:return:
		"""
		content = GitRepoReadMe._header + "\n\n" + GitRepoReadMe._author + "\n" + GitRepoReadMe._purpose + "\n" + \
		          GitRepoReadMe._cloning
		content += "\n## Scripts Herein.\n" + GitRepoReadMe._scripts + "\n" + GitRepoReadMe.add_contribs()
		content += "\n##  Future Features.\n"  # GitRepoReadMe.future_features
		content = content.format(rp_name, rp_author)
		with open("README.md", 'w') as f:
			f.write(content)
		print("Initialized ReadMe.md")
		print(content)


if __name__ == '__main__':
	github_user_name = 'datatalking'
	repository_name = 'Compositional_Notebook'
	ps = ArgumentParser(description="Generate a README.md file in markdown for any github repository.")
	ps.add_argument('-n', '--name',
	                action='store',
	                dest='name',
	                help="The name of your github repository.",
	                default=os.path.abspath('.').split('/')[-1])
	ps.add_argument('-a', '--author',
	                action='store',
	                dest='author',
	                help="Your github username",
	                default=f"{github_user_name}")
	psd = ps.parse_args()
	GitRepoReadMe.gen_RMe(psd.name, psd.author)
