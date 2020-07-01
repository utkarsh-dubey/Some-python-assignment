"""
CSE101: Introduction to Programming
Assignment 3

Name        :Utkarsh Dubey
Roll-no     :2019213
"""



import math
import random


def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    distance=math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    return distance



def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    for i in range(1, len(points)):         #sorting is done via insertion sort for speed
  
        pos = points[i]  
        j = i-1
        while j >=0 and pos[0] < points[j][0] : 
                points[j+1] = points[j] 
                j -= 1
        points[j+1] = pos 

    return points
                



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    for i in range(1, len(points)): 
  
        pos = points[i]  
        j = i-1
        while j >=0 and pos[1] < points[j][1] : 
                points[j+1] = points[j] 
                j -= 1
        points[j+1] = pos 

    return points



def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    needed=[]
    close=math.inf


    for x in plane:
        for i in plane:
            if(i!=x):

                distance=dist(x,i)
                if(close>distance):
                    close=distance
                    needed=[]
                    needed.append(close)
                    needed.append(x)
                    needed.append(i)

    return needed


            





def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    test=0
    temp=d
    points=sort_points_by_Y(points)
    needed=[]
    for i in points:
        for j in points:

            if(j[1]-i[1]>=temp and i!=j):
                break;

            if(dist(i,j)<d and i!=j):
                needed=[]
                needed.append(dist(i,j))
                needed.append(i)
                needed.append(j)
                d=dist(i,j)
                test=1
            
            


    if(test==0):
        return -1
    return needed
    





def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    if(len(points)<=2):
        if(len(points)==2):
            needed=[]
            needed.append(dist(points[0],points[1]))
            needed.append(points[0])
            needed.append(points[1])

            return needed
        else:
            needed=[]
            needed.append(0)
            needed.append(points[0])
            return needed    
    
    one=efficient_closest_pair_routine(points[:len(points)//2])
    two=efficient_closest_pair_routine(points[len(points)//2:])
    
    if(one[0]==0):
        d=two[0]
    elif(two[0]==0):
        d=one[0]
    else:
        d=min(one[0],two[0])
    strip=[]
    for i in range(len(points)):
        if(abs(points[i][0]-points[len(points)//2][0])<d):
            strip.append(points[i])

    

    if(closest_pair_in_strip(strip,d)!=-1):
        needed=closest_pair_in_strip(strip,d)
        return needed
    else:
        if(d==one[0]):
            return one

        if(d==two[0]):
            return two



        


   
 




def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points=sort_points_by_X(points)            

    return efficient_closest_pair_routine(points)



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10000
    #size of plane for generation of points
    plane_size = (100, 100) 
    plane = generate_plane(plane_size, num_pts)
    #print(plane)
    #print(naive_closest_pair(plane))
    print(efficient_closest_pair(plane))

