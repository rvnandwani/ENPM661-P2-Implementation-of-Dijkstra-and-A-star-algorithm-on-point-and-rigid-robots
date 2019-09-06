## Problem statement :-  
1. Implement Dijkstra and A* algorithm to find a path between start and end point on following map for a point robot and rigid robot.  
![Map](https://user-images.githubusercontent.com/47286001/62080075-e9ee1200-b21d-11e9-91a1-d472bbbd1332.png)
2. Robot can move in up, down, left, right & diagonally between up-left, up-right, down-left and down-right directions with following cost.  
![Cost](https://user-images.githubusercontent.com/47286001/62079951-b3b09280-b21d-11e9-8bcf-0d4068547e46.png)
3. Difference between point and rigid robot is that rigid robot will have some radius and clearence from the obstacle(The rigid robot considered in this problem is in shape of cylinder).   
![pointrobot](https://user-images.githubusercontent.com/47286001/62080616-02126100-b21f-11e9-8eff-11d6ae875fb9.PNG)  
## Implementation
The libraries being imported to run the code are:  
1. numpy
2. math
3. pygame
4. sys  
  
So for point robot the input required is initial coordinates, final coordinates and resolution, but for rigid robot apart from coordinates and resolution required input is of robot radius and its clearence from the obstacle.   
Obstacle space for the robot is created using half-planes equations and then applying Minkowski sum.
### Note:-
1. All the inputs have to be numbers(non-negative integers); not letters, symbols or blank input.
2. Resolution is for GUI and node generation only i.e. Nodes must be entered in real world cordinates(x in between 0 and 250, y in between 0 and 150)
3. Approximate runtime in my computer was  
	Dijkstra point robot from (0,0) to (250,150) in resolution 1 - 1 minute 35 seconds  
	A-star point robot from (0,0) to (250,150) in resolution 1 - 20 seconds
4. Make sure that the resolution entered did not make the cordinates non integers (i.e. a cordinate either x or y = 25 and resolution = 2) will throw an anonymous error. So make sure that (cordinates_entered % resolution == 0)
## Result

* Black area is the area that is not explored
* Blue area is the obstacle space
* White area is the explored area
* The path generated is in red color
### A-star for point robot :-   
![Picture2](https://user-images.githubusercontent.com/47286001/62079610-105f7d80-b21d-11e9-8f53-f7027c9265a2.png)   
### Dijkstra for point robot :-   
![Picture1](https://user-images.githubusercontent.com/47286001/62079531-ead27400-b21c-11e9-8f7f-91582507236e.png)
### A-star for rigid robot :-   
![Picture3](https://user-images.githubusercontent.com/47286001/62237977-0914ad00-b3a0-11e9-9e7a-41c7935bf2c9.png)
### Dijkstra for rigid robot :-   
![Picture4](https://user-images.githubusercontent.com/47286001/62238958-fb602700-b3a1-11e9-8f35-e53f71172393.png)
