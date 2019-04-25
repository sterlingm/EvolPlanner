#include "planner_pkg/crossover.h"

Crossover::Crossover(const ramp_msgs::Path p1, const ramp_msgs::Path p2) : path1_(p1), path2_(p2) {} 


const std::vector<ramp_msgs::Path> Crossover::perform() 
{
  std::vector<ramp_msgs::Path> result;

  //Randomly choose a configuration in each path to split on
  unsigned int i_knotPoint1 = rand() % (path1_.points.size()-1); 
  unsigned int i_knotPoint2 = rand() % (path2_.points.size()-1); 

  //ROS_INFO("i_knotPoint1: %i i_knotPoint2: %i", i_knotPoint1, i_knotPoint2);

  ramp_msgs::Path r1;
  //Push on the first part of the first path
  for(unsigned int i=0; i<=i_knotPoint1; i++) 
  {
    r1.points.push_back(path1_.points.at(i));
  }


  //Push on the second part of the second path
  for(unsigned int i=i_knotPoint2+1; i<path2_.points.size(); i++) 
  {
    r1.points.push_back(path2_.points.at(i));
  }


  ramp_msgs::Path r2;
  //Push on the first part of the second path
  for(unsigned int i=0; i<=i_knotPoint2; i++) 
  {
    r2.points.push_back(path2_.points.at(i));
  }
  
  
  //Push on the second part of the first path
  for(unsigned int i=i_knotPoint1+1; i<path1_.points.size(); i++) 
  {
    r2.points.push_back(path1_.points.at(i));
  }

  result.push_back(r1);
  result.push_back(r2);

  return result;
}



const std::vector<nav_msgs::Path> Crossover::navPerform() 
{
  std::vector<nav_msgs::Path> result;

  //Randomly choose a configuration in each path to split on
  unsigned int i_point1 = rand() % (navPath1_.poses.size()-1); 
  unsigned int i_point2 = rand() % (navPath2_.poses.size()-1); 

  //ROS_INFO("i_knotPoint1: %i i_knotPoint2: %i", i_knotPoint1, i_knotPoint2);

  nav_msgs::Path r1;
  //Push on the first part of the first path
  for(unsigned int i=0; i<=i_point1; i++) 
  {
    r1.poses.push_back(navPath1_.poses[i]);
  }


  //Push on the second part of the second path
  for(unsigned int i=i_point2+1; i<navPath2_.poses.size(); i++) 
  {
    r1.poses.push_back(navPath2_.poses[i]);
  }


  nav_msgs::Path r2;
  //Push on the first part of the second path
  for(unsigned int i=0; i<=i_point2; i++) 
  {
    r2.poses.push_back(navPath2_.poses[i]);
  }
  
  
  //Push on the second part of the first path
  for(unsigned int i=i_point1+1; i<navPath1_.poses.size(); i++) 
  {
    r2.poses.push_back(navPath1_.poses[i]);
  }

  result.push_back(r1);
  result.push_back(r2);

  return result;
}


