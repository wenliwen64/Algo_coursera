#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <set>
using namespace std;

class Graph{
    int t;
    int s;
    int V;
    vector<int> bk_explore;
    vector<int> leader;
    vector<int> ft;
    vector< vector<int> > adj;
    void DFS(int v);
    set<int> leaderset;
public:
    Graph(int V);
    void addEdge(int v, int w);
    void DFS_loop();
    void print_ft();
    void print_leader();
    void print_scc10();
    vector<int> getFt();
};

Graph::Graph(int nV) : t(-1), s(0), V(nV), bk_explore(nV, 0), leader(nV, -1), ft(nV, -1), adj(nV, vector<int>(0)) {
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
}
 
void Graph::DFS(int i){
    bk_explore[i] = 1;
    leader[i] = s;
    for(int j = 0; j < adj[i].size(); j++){
        int edge_head = adj[i][j];
        if(bk_explore[edge_head] == 0)
            DFS(edge_head);
    }
    t = t + 1;
    ft[i] = t;
}

void Graph::DFS_loop(){
    int i = V - 1; 
    while(i > -1){
        if(i%10 == 0)
            cout << i << " out of total " << V << " vetecies" << endl;
        if(bk_explore[i] == 0){
            s = i;    
            DFS(i);
	} 
        i--;
    } }

void Graph::print_ft(){
    for(int i = 0; i < V; i++){
        cout << i << " " << ft[i] << endl;
    }
}

void Graph::print_leader(){
    for(int i = 0; i < V; i++){
        cout << i << " " << leader[i] << endl;
    }

}

void Graph::print_scc10(){
    multiset<int> mult_leaderset;
    vector<int> count_scc;
    for(int k = 0; k < V; k++){
	leaderset.insert(leader[k]);
        mult_leaderset.insert(leader[k]);
    }
    for(set<int>::iterator it = leaderset.begin(); it != leaderset.end(); it++){
        count_scc.push_back(mult_leaderset.count(*it));
    }
    sort(count_scc.begin(), count_scc.end());

    vector<int>::iterator it_scc = count_scc.end();
    for(int k = 0; k < 10; k++){
        it_scc--;
        cout << *it_scc << endl;
    } 
}

vector<int> Graph::getFt(){
    return ft;
}

int main(){
    //ifstream afile("test.txt");
    ifstream afile("SCC.txt");
    int v = 0;
    int w = 0;
    int nV = 875714;
    Graph graph(nV);
    Graph rev_graph(nV);
    while(afile >> v){
        afile >> w; 
        graph.addEdge(v-1, w-1); 
        rev_graph.addEdge(w-1, v-1);
        //cout << w  << endl;
    }
    afile.close();

    rev_graph.DFS_loop();
    rev_graph.print_ft();
    
    vector<int> kFt = rev_graph.getFt();
    Graph new_graph(nV);
    //ifstream aafile("test.txt"); 
    ifstream aafile("SCC.txt"); 

    cout << "second time" << endl;
    while(aafile >> v){
        aafile >> w;
        new_graph.addEdge(kFt[v-1], kFt[w-1]); 
    }
    new_graph.DFS_loop();
    new_graph.print_leader(); 
    new_graph.print_scc10();
 
    return 0;
}
