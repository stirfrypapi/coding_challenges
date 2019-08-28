//
//  main.cpp
//  playground
//
//  Created by Raymond Pang on 8/28/19.
//  Copyright © 2019 Raymond Pang. All rights reserved.
//

#include <iostream>
#include <utility>      // std::pair, std::make_pair
#include <string>       // std::string
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	int numIslands(vector<vector<char>>& grid) {
		if (grid.size() == 0) {
			return 0;
		}
		int count = 0;
		int rows = (int)grid.size();
		int cols = (int)grid[0].size();
		
		vector<vector<int>> visited;
		for (int i=0; i<rows; ++i) {
			vector<int> cols_vec;
			for (int j=0; j<cols; ++j) {
				cols_vec.push_back(0);
			}
			visited.push_back(cols_vec);
		}
		
		for (int i=0; i < grid.size(); ++i) {
			for (int j=0; j < grid[i].size(); ++j) {
				if (visited[i][j] == 0 && grid[i][j] == '1') {
					vector<pair<int, int>> queue;
					queue.push_back(make_pair(i, j));
					while (queue.size() > 0) {
						cout << "while" << endl;
						pair<int, int> p = queue[0];
						int x = p.first;
						int y = p.second;
						queue.erase(queue.begin());
						// right
						if (y+1 < cols && visited[x][y+1] == 0 && grid[x][y+1] == '1') {
							visited[x][y+1] = 1;
							queue.push_back(make_pair(x, y+1));
						} // if
						// bottom
						if (x+1 < rows and visited[x+1][y] == 0 and grid[x+1][y] == '1') {
							visited[x+1][y] = 1;
							queue.push_back(make_pair(x+1, y));
						}
						// left
						if (y-1 >= 0 and visited[x][y-1] == 0 and grid[x][y-1] == '1') {
							visited[x][y-1] = 1;
							queue.push_back(make_pair(x, y-1));
						}
						// top
						if (x-1 >= 0 and visited[x-1][y] == 0 and grid[x-1][y] == '1') {
							visited[x-1][y] = 1;
							queue.push_back(make_pair(x-1, y));
						}
					} // while
					count += 1;
				} // if
			} // for
		} // for
		return count;
	}
};

int main(int argc, const char * argv[]) {
	Solution s;
	vector<vector<char>> grid = {{'1', '1', '1', '1', '0'},
								 {'1', '1', '0', '1', '0'},
								 {'1', '1', '0', '0', '0'},
								 {'0', '0', '0', '0', '0'}};
	cout << s.numIslands(grid) << endl;
	return 0;
}
