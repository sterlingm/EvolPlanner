#ifndef POPULATION_H
#define POPULATION_H

#include "nav_msgs/Path.h"
#include "planner_pkg/evaluation.h"

class Population {
  public:
	// Struct to store data about the nav_msgs/Path
	struct path
	{
		nav_msgs::Path navPath;
		int fitness;
	};

	// Constructors
    Population() {}
    Population(std::vector<nav_msgs::Path> pathList);

	// Methods
    int getBestIndex();
	void replace(int i, nav_msgs::Path p);
	void evaluate();

	// Fields
	std::vector<path> paths;
};

#endif
