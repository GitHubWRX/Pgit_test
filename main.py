# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# maybe, the head is the current branch, and master pointed to itself version, 
# if new branch not modified, it will point to master's version too.

# now modify test again, I predict the head will still point to the test, but newest version.

# the above is right, 
# if we just create a new branch, the head will point master and new branch both.
# if we modify the new branch to new branch2, then head can only point new branch2
# so, when I reset the version to new branch, the head again point to both and there is not symbol 'Head-> XXXX'

# now, I predict if I modify the branch2 to branch3, then the head will point to branch3,
# and, I predict if I reset the branch3 to branch2, then the head will only point to branch2, with symbol 'head->branch2'
# Let's TRY!
