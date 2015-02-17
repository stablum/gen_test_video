import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 4 # duration of the clip, in seconds

def make_frame(t):
    print "t",t
    surface = gizeh.Surface(W,H)
    radius = 30
    circle = gizeh.circle(radius, xy = (t*float(W)/duration,50), fill=(1,0,0))
    circle.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_videofile('one_moving_dot.avi',fps=10,codec='mpeg4')
