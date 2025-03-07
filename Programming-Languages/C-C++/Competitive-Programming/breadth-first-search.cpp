#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(vector<vector<int>> &graph, int start)
{
    vector<bool> visited(graph.size(), false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : graph[node])
        {
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main()
{
    vector<vector<int>> graph = {
        {1, 2},    // Node 0 connected to 1, 2
        {0, 3, 4}, // Node 1 connected to 0, 3, 4
        {0, 5},    // Node 2 connected to 0, 5
        {1},       // Node 3 connected to 1
        {1, 5},    // Node 4 connected to 1, 5
        {2, 4}     // Node 5 connected to 2, 4
    };

    cout << "BFS Traversal: ";
    bfs(graph, 0);
    return 0;
}
