# FILENAME Compositional_Notebook.py
# SOURCE https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python

import os
import pwd
import readme_generator


# TODO will need to parse /data/raw_notebooks.txt into csv then database
# TODO will need to enter these into a csv file, then parquet then a database
# TODO database will include notebook name as a number 2 throughk 41
# TODO will need to create a dictionary of classes as key and value as MMDDYY
# TODO create a class for the notebooks? Type compositional, Moleskin, Binders, subjects, related projects, tasks etc


def main():
    """
    a script to greet user and
    :return:
    """
    get_username()
    print_hi(user_name=user_name)
    script_purpose()
    # TODO run "exec.readme_generator() from here"


def get_username():
    machine_name = pwd.getpwuid(os.getuid())[0]
    print(f'This machines name is {machine_name}')


def print_hi(user_name):
    """
    Use a breakpoint in the code line below to debug your script
    :param user_name:
    :return:
    """
    print(f'Hi, {user_name}')  # Press ⌘F8 to toggle the breakpoint.


def script_purpose():
    """
    inform user as to script goal to organize compositional notebooks
    :return:
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_name = 'Andrew'
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
