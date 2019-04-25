#include "planner_pkg/population.h"

// Constructor to set the paths vector using a vector of nav_msgs/Path
Population::Population(std::vector<nav_msgs::Path> pathList)
{
	path temp;

	for (int i = 0; i < pathList.size(); i++)
	{
		temp.navPath = pathList.at(i);
		paths.push_back(temp);
	}

	evaluate();
}

// Finds the index of the shortest path
int Population::getBestIndex()
{
	int minIndex = 0;
		
	evaluate();

	for (int i = 1; i < paths.size(); i++)
	{
		if (paths.at(i).fitness < paths.at(minIndex).fitness)
		{
			minIndex = i;
		}
	}

	return minIndex;
}

// Replaces a path at a specific index i with a path p
void Population::replace(int i, nav_msgs::Path p)
{
	paths.at(i).navPath = p;
	evaluate();
}

// Updates the fitness of all paths
void Population::evaluate()
{
	for (int i = 0; i < paths.size(); i++)
	{
		paths.at(i).fitness = Evaluation::eval(paths.at(i).navPath);
	}
}
