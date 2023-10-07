#include <ros.h>
#include <std_msgs/Int16MultiArray.h>
#include <Wire.h>
#include <MPU6050.h>

// Create instance of MPU6050
MPU6050 mpu_1;


ros::NodeHandle nh;

std_msgs::Int16MultiArray imu_msg_1;

ros::Publisher imu_publisher_1("imu_1", &imu_msg_1);



void setup()
{
  
  mpu_1.initialize();


  nh.initNode();
  nh.advertise(imu_publisher_1);

}

void loop()
{
  // Read raw sensor data from MPU6050
  int16_t ax_1, ay_1, az_1, gx_1, gy_1, gz_1;
 
  mpu_1.getMotion6(&ax_1, &ay_1, &az_1, &gx_1, &gy_1, &gz_1);
  
  

  // Populate the IMU data array
  int16_t imu_data_1[] = {ax_1, ay_1, az_1, gx_1, gy_1, gz_1};
 
  imu_msg_1.data_length = 6;
  imu_msg_1.data = imu_data_1;

  // Publish the IMU data
  imu_publisher_1.publish(&imu_msg_1);
 

  nh.spinOnce();
  delay(1000); // Adjust the delay according to your desired publishing rate
}
