from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def plot_implicit(fn, bbox=(-2,2)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100) # resolution of the contour
    B = np.linspace(xmin, xmax, 200) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X,Y = A1,A2
        Z = fn(X,Y,z)
        #cset = ax.contour(X, Y, Z+z, [z],cmap=cm.BuPu, zdir='z', frame = False)
        cset = ax.contour(X, Y, Z+z, [z],colors = 'green', zdir='Z',label = 'Citrus')
        # [z] defines the only level to plot for this contour for this value of z

    for y in B: # plot contours in the XZ plane
        X,Z = A1,A2
        Y = fn(X,y,Z)
        #cset = ax.contour(X, Y+y, Z, [y], cmap=cm.winter,zdir='y', frame = False)
        cset = ax.contour(X, Y+y, Z, [y], colors = 'green',zdir='y', label = 'Citrus')
     

    for x in B: # plot contours in the YZ plane
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        #cset = ax.contour(X+x, Y, Z, [x],cmap=cm.coolwarm, zdir='x', frame = False)
        cset = ax.contour(X+x, Y, Z, [x],colors = 'green', zdir='x', label = 'Citrus')

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    #ax.set_zlim3d(zmin,zmax)
    ax.set_xlabel('X')
    ax.set_xlim3d(-1./2,1./2)
    ax.set_ylabel('Y')
    ax.set_ylim3d(0,1)
    ax.set_zlabel('Z')
    ax.set_zlim3d(-1./4,1./4)
    #plt.legend(r'Citrus')
    ax.set_title(r'Zitrus: $x^2 + z^2= y^3(1-y)^3$', va='bottom')
    #ax.view_init(elev=25, azim=-58)           # elevation and angle
    ax.dist= 7      
    ax.set_axis_off()

    plt.show()

def hyp_part1(x,y,z):
    return -(x**2) - (y**2) + (z**2) - 1
   
def Citrus(x,y,z):
	return x**2 + z**2 -(y**3)*(1-y)**3
def Hummol(x,y,z):
	return x**2-y**2*(z**2)
   

#if __name__ == 'main':
#plot_implicit(hyp_part1, bbox=(-100.,100.))
plot_implicit(Hummol, bbox=(0.,1))
#	P.show()
