#ifndef EVALUATION_H
#define EVALUATION_H

#include <math.h>
#include "nav_msgs/Path.h"
#include "geometry_msgs/Pose.h"

class Evaluation {
  public:
	// Constructors
	Evaluation() {}

	// Methods
	static double eval(nav_msgs::Path path);

  private:
	static double calculateDist(geometry_msgs::Pose a, geometry_msgs::Pose b);
};

#endif
