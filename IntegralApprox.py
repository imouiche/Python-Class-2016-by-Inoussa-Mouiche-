import pylab as p
# we import this module for the plotting
import random as r
# we import this module to generate the random points
import scipy.integrate as s
# we import this module to compute the integrale using
# the function quad()

# we define the function f
def f(x):
        return 2*p.exp(-0.5*((x-3)**2))

if __name__=='__main__':
        a = 1
        b = 5
        x = p.linspace(a,b,1001)
        # we discretize the interval [a,b]
        y = f(x)
        # we compute the image of the vector x by the function f
        
        p.plot(x,y,'r-',label=r"$2\exp(-0.5(x-2)^2)$")
        #we plot the curve of f
        p.title("Graph of f(x) for $1\leq x \leq 5$")
        p.hold('on')
        p.xlabel("x")
        p.ylabel("f(x)")
        
        p.xlim((0,6))
        p.xticks((a,b))
        #p.xticklabels(('$a=1$', '$b=5$'))
        p.yticks((0, 2))
        #p.ytickslabels(('$y_min$', '$Max_f= 2$'))
        
        # we label the axis 
        p.fill_between(x,y)
        p.legend()
        #p.show()
        # we display the legend
        p.savefig("Grah_of_f.png")
        # we save the figure 
        Max_f = f(3)
        #we compute the maximum 
        #N = int(input('Enter the number of points you want to generate randomly:')
        N=input("Please enter the number of point you want to generate .\n")
        X = []
        Y=[]
        # we initialize the list X as a empty list to store
        # the generated points
        for k in range(N):
                X.append(r.uniform(a,b))
                Y.append(r.uniform(0,Max_f))
        z =zip(X,Y)
        #print z
        # each times we add a new generated point
        X_f = []
        # we initialize the list X_f to store the points
        # on the shade area
        for k in range(N):
                if z[k][1] <= f(z[k][0]):
                        X_f.append(X[k])
        # we store the point on the shade area
        n = len(X_f)
        print "%d points fall on the shade area.\n"%n
        # we print the number of points fall on the shade area
        A_f = (n/float(N))*(b-a)*Max_f
        # we compute the integrale A_f
        Error = p.fabs(A_f - s.quad(f,a,b)[0])
        # we compute the error by considered the exact value
        # of the integrale is the result given by the 
        # function quad() of the submodule scipy.integrate
        print "The absolute value of the error committed (while approaching the"
        print "real value  of the integrale using the function quad())is around"
        print  "%0.10f"%Error
        # we print the error.
        print 'the integrale computed is %f '%A_f
        #we print the result of the integrale computed
        
