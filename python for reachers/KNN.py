import numpy as np
import scipy.stats as ss
from sklearn import datasets
import matplotlib.pyplot as plt

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

def generate_synth_data(n=50):
    """Create two sets of points from bivariate normal distribution"""
    points=np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,2).rvs((n,2))),axis=0)
    outcomes=np.concatenate( (np.repeat(0,n), np.repeat(1,n)) )
    return(points,outcomes)

def make_prediction_grid(predictors, outcomes,limits,h,k=5):
    """Classify each point on the prediction grid"""
    (x_min,x_max,y_min,y_max)=limits
    xs=np.arange(x_min,x_max,h)
    ys=np.arange(y_min,y_max,h)
    xx,yy=np.meshgrid(xs,ys)
    prediction_grid=np.zeros(xx.shape)#,dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p=np.array([x,y])
            prediction_grid[j,i]=knn_prediction(p,predictors,outcomes,k)
    return (xx,yy,prediction_grid)
    
def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2-p1,2)))

def majority_vote(votes):
    mode,count = ss.mstats.mode(votes)
    return mode
      
def find_nearest_neighbor(p, points, k=5): #Return the k nearest point
    distances=np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i]=distance(p,points[i])
    index=np.argsort(distances)
    return index[0:k]

def knn_prediction(p, points, outcomes, k=5):
    index=find_nearest_neighbor(p,points,k)
    return majority_vote(outcomes[index])
 
irish=datasets.load_iris()
predictors=irish.data[: , :2]
outcomes=irish.target

plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1],"ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1],"go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1],"bo")
plt.savefig("irish.pdf")

k=5; filename="irish.pdf"; limits=(4,8,1.5,4.5); h=0.1
(xx, yy, prediction_grid)= make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx,yy,prediction_grid,filename)  
