#ifndef PLANNER_H
#define PLANNER_H

#include "planner_pkg/insert.h"
#include "nav_msgs/OccupancyGrid.h"
#include "planner_pkg/population.h"
#include "planner_pkg/insert.h"
#include "planner_pkg/delete.h"
#include "planner_pkg/change.h"
#include "planner_pkg/crossover.h"
#include "planner_pkg/swap.h"
#include "nav_msgs/Path.h"
#include <stdlib.h>

class Planner {
  public:
	Planner() {}
	Planner(Population p);

	void init(nav_msgs::OccupancyGrid map);
	void runGeneration();
	void run(int runs);

	Population* pop;
};

#endif
