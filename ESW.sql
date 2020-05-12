CREATE DATABASE IF NOT EXISTS ESW;
use ESW;

drop table if exists Data;
create table Stadiums(
	Temperature VARCHAR(30) NOT NULL, 
	Humidity VARCHAR(30) NOT NULL, 
	PowerIN VARCHAR(30) NOT NULL, 
	PowerOUT VARCHAR(30) NOT NULL, 
	EnergyIN VARCHAR(30) NOT NULL, 
	EnergyOUT VARCHAR(30) NOT NULL, 
	EnergyDiff VARCHAR(30) NOT NULL, 
 );

