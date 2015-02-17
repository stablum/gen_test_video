import gizeh
surface = gizeh.Surface(width=320, height=260) # dimensions in pixel
circle = gizeh.circle (r=30, # radius, in pixels
                       xy= [100,100], # coordinates of the center
                       fill= (0,0,0)) # RGB coordinates
rect = gizeh.rectangle(lx=320, ly=260, xy=(160,130), fill=(1,1,1), angle=0)
rect.draw( surface ) # draw the rectangle on the surface
circle.draw( surface ) # draw the circle on the surface
surface.get_npimage() # export as a numpy array (we will use that)
surface.write_to_png("one_fixed_dot.png") # export as a PNG
