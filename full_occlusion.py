import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 4 # duration of the clip, in seconds

def make_frame(t):
    print "t",t
    surface = gizeh.Surface(W,H)
    radius_red = 20
    radius_blue = 30
    circle_red = gizeh.circle(radius_red, xy = (t*float(W)/duration,40), fill=(1,0,0))
    circle_blue = gizeh.circle(radius_blue, xy = (W-(t*float(W)/duration),40), fill=(0,0,1))
    circle_red.draw(surface)
    circle_blue.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_videofile('full_occlusion.avi',fps=10,codec='mpeg4')
