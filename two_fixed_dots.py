import gizeh
surface = gizeh.Surface(width=320, height=260)
rect = gizeh.rectangle(lx=320, ly=260, xy=(160,130), fill=(1,1,1), angle=0)

circle_red = gizeh.circle (r=30, xy= [100,100], fill= (1,0,0))
circle_blue= gizeh.circle (r=30, xy= [200,100], fill= (0,0,1))

rect.draw( surface )
circle_red.draw( surface )
circle_blue.draw( surface )
surface.get_npimage()
surface.write_to_png("two_fixed_dots.png")
