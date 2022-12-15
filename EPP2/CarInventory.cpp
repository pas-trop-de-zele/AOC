#include "CarInventory.h"
#include <numeric>
#include <sstream>
void CarInventory::readFile(std::string filename) {
    std::string line;
    std::ifstream myfile("data.txt");
    std::string model, license;
    double mileage;
    while (std::getline(myfile, line)) {
        if (line.empty()) {
            break;
        }
        std::stringstream ss(line);
        ss >> model >> license >> mileage;
        std::cout << "Reading in " << model << " " << license << " " << mileage << std::endl;
        // Check if currently there is a record for this model
        if (mileage_lookup.find(model) == mileage_lookup.end()) {
            mileage_lookup[model] = std::vector<double>();
        }
        mileage_lookup[model].push_back(mileage);
    }
    std::cout << "...finish reading file!" << std::endl;
}

double CarInventory::averageMileage(std::string model) {
    // NO RECORD FOR THIS MODEL!
    if (mileage_lookup.find(model) == mileage_lookup.end()) {
        return -1;
    }
    double mileage_sum = std::accumulate(mileage_lookup[model].begin(), mileage_lookup[model].end(), 0);
    int count = mileage_lookup[model].size();
    return mileage_sum / count;
}