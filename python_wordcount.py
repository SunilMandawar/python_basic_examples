"""" Word count program """

txt = 'This is my some kind of test text. It may not be best as best or as good as fine or fine but but is reapeting the the'
line_split = txt.split()
lst = []
for item in line_split:
    lst.append( (item,line_split.count(item)) )

print( lst )






