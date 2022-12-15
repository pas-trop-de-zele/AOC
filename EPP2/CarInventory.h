#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

/**
 * Use a hashmap (unordered_map<std::string, std::vector<double>>) to map between car model and a list of the mileages
 *
 * Then for the averageMileage(), simply loop over all the recorded
 *      mileages for the model and compute the average
 */

class CarInventory {
private:
    // Store each model with a vector of all mileages
    std::unordered_map<std::string, std::vector<double>> mileage_lookup;

public:
    CarInventory() = default;
    void readFile(std::string filename);
    double averageMileage(std::string model);
};