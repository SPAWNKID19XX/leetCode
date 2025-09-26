'''

Check DOM
Have the function CheckDOM(strParam) read the strParam parameter being passed, which will be a string of HTML elements and plain text.
The elements that will be used are:
b, i, em, div, p
Your program should support 3 cases:
Correct nesting
If the string is a correct sequence of nested HTML elements, return "true".
Almost correct nesting
If changing a single tag can make it correct, return the first tag to change.
Changing a tag means altering its tag name (e.g., <div> → <b>), not adding or removing tags, and not switching from opening to closing tags.

Incorrect nesting
If it would require changing more than one element to make it correct, return "false".
Examples
Input: "<div><b><p>hello world</p></b></div>" Output: true Reason: the HTML is nested correctly
Input: "<div><i>hello</i>world</b>" Output: div Reason: if the first <div> element were changed into a <b>, the HTML would be correct
Input: "</div><p></p><div>" Output: false Reason: the order of opening and closing tags is not respected
Do you want me to also create a couple of extra tricky examples for this challenge so it’s harder to solve?

'''
import re

sol1 = '<div><b><p>hello world</p></b></div>'
sol2 = '<div><i>hello</i>world</b>'
sol3 = '</div><p></p><div>'
axcept_tags = ['b', 'i', 'em', 'div', 'p']

def validation_tags(l: list):
    print(l, type(l), len(l), len(l)%2 == 0)
    if (len(l)%2 == 0):
        for tag in l:
            print('+-+-+-+-+-',tag[1]=='/', )
    else:
        return False



def checkDOM(strParam):
    matches = re.findall(r'</?\w+>', strParam)
    is_avaliable_tags = validation_tags(matches)
    open_tags = re.findall(r'<\w+>', strParam)
    close_tags=re.findall(r'</\w+>', strParam)
    return matches


print(checkDOM(sol1))