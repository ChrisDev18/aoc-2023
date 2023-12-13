//
// Created by chris on 13/12/2023.
//

#ifndef DAY2_PART1_H
#define DAY2_PART1_H

#endif //DAY2_PART1_H


#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <sstream>

using namespace std;

const int R = 12;
const int G = 13;
const int B = 14;

int getGameNumber(const string& line) {
    char* val;
    int n;
    size_t i = line.find(':');
    string beginning = line.substr(0, i);
    sscanf(line.c_str(), "%s %d", val, &n);
    return n;
}

bool checkGame(const string& game) {
    stringstream draws(game);
    string draw;

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
                if (n > R) return false;
            }
            else if (strcmp(colour, "green") == 0) {
                if (n > G) return false;
            }
            else {
                if (n > B) return false;
            }
        }
    }

    return true;
}

int part1() {
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

        if (checkGame(game.substr(i + 1))) {
            total += getGameNumber(game);
        }
    }

    cout << "The total is: " << total << endl;
    infile.close();
    return 0;
}


