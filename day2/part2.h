//
// Created by chris on 13/12/2023.
//

#ifndef DAY2_PART2_H
#define DAY2_PART2_H

#endif //DAY2_PART2_H


#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <sstream>

using namespace std;

//int getGameNumber(const string& line) {
//    char* val;
//    int n;
//    size_t i = line.find(':');
//    string beginning = line.substr(0, i);
//    cout << beginning << "\n";
//    sscanf(line.c_str(), "%s %d", val, &n);
//    cout << "n value:" << n << "\n";
//    return n;
//}

int calcMinSquare(const string& game) {
    stringstream draws(game);
    string draw;

    int r = 0;
    int g = 0;
    int b = 0;



    // read draw-by-draw
    while (getline(draws, draw, ';')) {
        stringstream values(draw);
        string value;

        // read colour-by-colour
        while (getline(values, value, ',')) {
            char colour[6];
            int n;
            sscanf(value.c_str(), " %d %s", &n, colour);

            if (strcmp(colour, "red") == 0) {
                if (n > r) r = n;
            }
            else if (strcmp(colour, "green") == 0) {
                if (n > g) g = n;
            }
            else {
                if (n > b) b = n;
            }
        }
    }

    return (r*g*b);
}

int part2() {
    int total = 0;

    // open file
    ifstream infile(R"(C:\Users\chris\Documents\Coding\AOC_2023\day2\record.txt)");
    // check file has opened
    if (!infile.is_open()) {
        cout << "Error opening file!" << endl;
        return 1;
    }

    // read line-by-line
    string game;
    while (getline(infile, game)) {
        size_t i = game.find(':');

        total += calcMinSquare(game.substr(i + 1));
    }

    cout << "The total is: " << total << endl;
    infile.close();
    return 0;
}
