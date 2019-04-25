#include "ros/ros.h"
#include "nav_msgs/OccupancyGrid.h"
#include "planner_pkg/planner.h"

using namespace ros;

Planner planner;

void callback(const nav_msgs::OccupancyGrid map)
{
	planner.init(map);
	planner.run(100);
}

int main(int argc, char **argv)
{
	// Initialize ROS node
	init(argc, argv, "listener");
	NodeHandle n;

	// Create subscriber
	Subscriber sub = n.subscribe("map", 1000, callback);
	
	// Run the callback function only once 
	spinOnce();
}
