#!/usr/bin/env python

"""
Script to generate one or more cubes of "impress.js" slides.
Edit the code at the end of this file to generate the number 
of slides you need (in multiples of 6)

Copy impress.js (from https://github.com/impress/impress.js) 
into the current directory.

Documentation about impress.js at:
    -> https://github.com/impress/impress.js (by Bartek Szopka)
    -> http://impress.github.io/impress.js 
    
Further inspiration from 
    -> Circular slides generator (by Hunter Wu)
       http://wmh.github.io/circular-slides-generator/ 
    
    -> A cube in impress.js (by Dmitry Sviridenko)
    -> http://codepen.io/letehaha/pen/JKXdzr

"""

# Slide positions around a cube. Organised
# to make transitions look smooth.
POSITIONS = [
    (   0,    0,    0),
    ( 0.5,    0, -0.5),
    (   0, -0.5, -0.5),
    (-0.5,    0, -0.5),
    (   0,  0.5, -0.5),
    (   0,    0,   -1),

]

# Rotations in Degrees. Organised to make
# transitions look smooth (hence some 360s)
ROTATIONS = [
    (0,  0,   0),
    (0, 90,   0),
    (90, 0, -90),
    (180, -90, 0),
    (90,-180,-90),
    (0, -180, -90),

]


def print_one_cube(width, id_offset=0, offset=(0,0,0)):
    """ 
        Prints a set of 6 impress.js slides in a cube.
        
        @param width: slide width (we assume this is the larger slide dimension)
        @param id_offset: integer saying how many to add to each slide number 
            (the number that is visible in the slide and the HTML comment)
        @param offset: (xyz-tuple) Offset position of the cube: allows
            multiple cubes to be drawn.
        
        Only the width is supplied; slides ought to be square!
    """
    # These values will be multiplied by the side_size
    
    for i in range(0,6):
        id = i + 1 + id_offset 
        print '<!-- Slide %d -->' % id
        print '<div class="step slide" data-x="%d" data-y="%d" data-z="%d"' % (
            width*POSITIONS[i][0] + offset[0], 
            width*POSITIONS[i][1] + offset[1], 
            width*POSITIONS[i][2] + offset[2]),
        print 'data-rotate-x="%d" data-rotate-y="%d" data-rotate-z="%d"' % (
            ROTATIONS[i][0], 
            ROTATIONS[i][1], 
            ROTATIONS[i][2]),
        print '>'
        print '  <q>Slide %d</q>' % id
        print '</div>\n'


def print_overview_slide():
    """
    Print the overview slide as per impress.js)
    """
    print '<div id="overview" class="step" data-x="3000" data-y="1500" data-scale="10">'
    print '</div>'

if __name__ == "__main__":
    # specify the width of your slides.
    slide_width = 900

    # print the first cube
    print_one_cube(slide_width)

    # print a second cube
    offset = 3*slide_width
    print_one_cube(slide_width, 6, (offset, offset, 0))

    # print the overview slide
    print_overview_slide()
