// Maksymilian Lazarewicz
#include "extra.h"
using namespace std;

struct Edge{
    int to;
    long long cost;

    bool operator>(const Edge &other) const{
        return cost > other.cost;
    }
};

void dijkstra(const vector<vector<Edge>> &graph, vector<long long> &dist, vector<int> &prev, int start, int finish){
    int n = graph.size();
    dist.assign(n, (long long)1000000000000000000);
    dist[start] = 0;
    prev.assign(n, -1);


    priority_queue<Edge, vector<Edge>, greater<Edge>> queue;
    Edge startPoint;
    startPoint.to = start;
    startPoint.cost = 0;
    queue.push(startPoint);

    while(!queue.empty()){
        Edge topPoint = queue.top();
        queue.pop();
        int u = topPoint.to;
        long long d = topPoint.cost;

        if(d > dist[u]){
            continue;
        }
        if(u == finish){
            break;
        }

        for(size_t i = 0; i < graph[u].size(); ++i){
            int v = graph[u][i].to;
            long long cost = graph[u][i].cost;

            if(dist[u] + cost < dist[v]){
                dist[v] = dist[u] + cost;
                prev[v] = u;

                Edge nextPoint;
                nextPoint.to = v;
                nextPoint.cost = dist[v];
                queue.push(nextPoint);
            }
        }
    }
}

int main(){
    int n, m;
    int start, finish;
    cin >> n >> m;
    vector<bool> isCity(n);
    vector<vector<Edge>> graph(n);

    for(int i = 0; i < n; ++i){
        int c;
        cin >> c;
        isCity[i] = c;
    }

    for(int i = 0; i < m; ++i){
        int u, v;
        long long d;
        cin >> u >> v >> d;

        long long mpg = (isCity[u] && isCity[v]) ? (long long)80 : (long long)50;
        long long cost = d*mpg;
        
        Edge e1,e2;
        e1.to = v;
        e1.cost = cost;
        e2.to = u;
        e2.cost = cost;
        graph[u].push_back(e1);
        graph[v].push_back(e2);
    }

    cin >> start >> finish;
    vector<long long> dist;
    vector<int> prev;
    dijkstra(graph, dist, prev, start, finish);

    if(dist[finish] == (long long)1000000000000000000){
        cout << -1 << "\n";
        cout << -1 << "\n";
        return 0;
    }
    cout << dist[finish]/(long long)1000 << "\n";

    vector<int> path;
    for(int i = finish; i != -1; i = prev[i]){
        path.push_back(i);
    }

    cout << path[path.size() - 1];
    for(int i = (long long)path.size() - 2; i >= 0; --i){
        cout << " " << path[i];
    }
    cout << "\n";
    return 0;
}
