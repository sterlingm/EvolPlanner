#include "planner_pkg/planner.h"

void Planner::init(nav_msgs::OccupancyGrid map) 
{
	// Generate a vector with a random number of paths
	std::vector<nav_msgs::Path> paths;
	nav_msgs::Path temp;

	int numPaths = rand() % 100 + 1;
	int numPoints;

	// For each path in the paths vector - Initialization of paths vector
	for (int i = 0; i < numPaths; i++)
	{
		// Generate a random number of points in the current path
		numPoints = rand() % 100 + 1; 
		
		// For each point in the current path
		for (int k = 0; k < numPoints; k++)
		{
			// Set the coordinates of the current point within the map
			temp.poses[k].pose.position.x = rand() % map.info.width;
			temp.poses[k].pose.position.y = rand() % map.info.height;
			temp.poses[k].pose.position.z = 0;
		}

		paths.push_back(temp);
	} 
	// End of initialization of paths

	// Create new population using these paths
	pop = new Population(paths);
}

void Planner::runGeneration()
{
	// Create and set random nav_msgs/Paths based on current population
	int index1 = rand() % pop->paths.size();
	int index2 = rand() % pop->paths.size();
	nav_msgs::Path path1 = pop->paths.at(index1).navPath;
	nav_msgs::Path path2 = pop->paths.at(index2).navPath;

	// Create variables to be used in modifications
	std::vector<nav_msgs::Path> result;
	Insert in_;
    Delete del_;
    Change chg_;
    Crossover cross_;
    Swap swap_;

	// Choose a random modification
	int mod = rand() % 5;

	// If insert
	if (mod == 0)
	{
		in_.navPath_ = path1;
		result.push_back(in_.navPerform());
	}
	// If delete
	else if (mod == 1)
	{
		del_.navPath_ = path1;
		result.push_back(del_.navPerform());
	}
	// If change
	else if (mod == 2)
	{
		chg_.navPath_ = path1;
		result.push_back(chg_.navPerform());
	}
	// If swap
	else if (mod == 3)
	{
		swap_.navPath_ = path1;
		result.push_back(swap_.navPerform());
	}
	// If crossover
	else if (mod == 4)
	{
		cross_.navPath1_ = path1;
		cross_.navPath2_ = path2;
		result = cross_.navPerform();
	}

	// If only one path was modified
	if (result.size() == 1)
	{
		pop->replace(index1, result.at(0));
	}
	// If two paths were modified (crossover)
	else if (result.size() == 2)
	{
		pop->replace(index1, result.at(0));
		pop->replace(index2, result.at(1));
	}

	// Update the fitness of the paths in the new population
	pop->evaluate();
}

void Planner::run(int runs)
{
	for (int i = 0; i < runs; i++)
	{
		runGeneration();
	}
}
