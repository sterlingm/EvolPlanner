#include "planner_pkg/evaluation.h"

double Evaluation::eval(nav_msgs::Path path)
{
	double dist = 0;	

	for (int i = 0; i < path.poses.size()-1; i++)
	{
		dist += calculateDist(path.poses[i].pose, path.poses[i+1].pose);
	}

	return dist;
}

double Evaluation::calculateDist(geometry_msgs::Pose a, geometry_msgs::Pose b)
{
	return sqrt(pow((a.position.x - b.position.x), 2) + pow((a.position.y, b.position.y), 2));
}
