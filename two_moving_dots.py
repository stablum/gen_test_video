import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 4 # duration of the clip, in seconds

def make_frame(t):
    print "t",t
    surface = gizeh.Surface(W,H)
    radius = 20
    circle_red = gizeh.circle(radius, xy = (t*float(W)/duration,30), fill=(1,0,0))
    circle_blue = gizeh.circle(radius, xy = (W-(t*float(W)/duration),95), fill=(0,0,1))
    circle_red.draw(surface)
    circle_blue.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_videofile('two_moving_dots.avi',fps=10,codec='mpeg4')
