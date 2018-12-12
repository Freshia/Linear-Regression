from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use('fivethirtyeight')


def create_dataset(hm,variance, step=2,correlation=False):
    val=1
    ys=[]
    for i in range(hm):
        y = val + random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation =='pos':
            val+=step
        elif correlation and correlation =='neg':
            val-=step
    xs=[i for i in range(len(ys))]
    return np.array (xs,dtype= np.float64),np.array(ys, dtype=np.float64)

def best_fit_slope_and_b(xs,ys):
    m=(mean(xs)*mean(ys))-mean(xs*ys)
    m=m/((mean(xs)**2)-mean(xs**2))
    b=mean(ys)-(m*mean(xs))

    return m,b

def squared_error(y_orig,y_line):
    return sum((y_line-y_orig)**2)
def coefficient_of_det(y_orig,y_line):
    y_mean_line=[mean(y_orig) for ys in y_orig]
    squared_error_regr=squared_error(y_orig,y_line)
    squared_error_ymean=squared_error(y_orig,y_mean_line)
    return 1-(squared_error_regr/squared_error_ymean)

xs,ys = create_dataset(40,10,2,correlation='pos')

m,b=best_fit_slope_and_b(xs,ys)
print (m,b)
regression_line=[((m*x)+b) for x in xs]
predictiveX=14
predictiveY=(m*predictiveX)+b

r_squared=coefficient_of_det(ys,regression_line)
print('RSQUARED')
print(r_squared)
plt.scatter(predictiveX,predictiveY,c='red')
plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()