#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <set>
#include <map>
using namespace std;

class Graph{
    int t;
    int s;
    int V;
    vector<int> bk_explore;
    vector<int> leader;
    vector<int> ft;
    vector<double> distance; //shortest distance from vertex 1 to other vertices
    map<int, double> min_dis;
    vector<int> X;
    vector< vector< pair<int, double> > > adj;
    void DFS(int v);
    set<int> leaderset;
public:
    Graph(int V);
    //void addEdge(int v, int w);
    void addEdge(int v, int w, double length);
    //void DFS_loop();
    //void print_ft();
    //void print_leader();
    //void print_scc10();
    void print_ans();
    void print_test();
    void dijkstra_search();
    //vector<int> getFt();
};

Graph::Graph(int nV) : t(-1), s(0), V(nV), bk_explore(nV, 0), leader(nV, -1), ft(nV, -1), distance(nV, 1000000), adj(nV, vector< pair<int,double> >(0)){}

void Graph::addEdge(int v, int w, double len){
    adj[v].push_back(std::make_pair(w, len));
}
 
void Graph::dijkstra_search(){
    double smallest_leng = 10000000;
    int smallest_vtx = -1;
    int count = 0;
    X.push_back(0);
    min_dis[0] = 0.;
    while(X.size() != V){
	smallest_leng = 1000000;
	smallest_vtx = count;

        //traves edges
        for(int i = 0; i < V; i++){
	    if(std::find(X.begin(), X.end(), i) == X.end()) continue; 
            for(vector< pair<int, double> >::iterator j = adj[i].begin(); j != adj[i].end(); j++){
		if(std::find(X.begin(), X.end(), (*j).first) == X.end()){
//                      cout<<(*j).second<<endl;
	            if((min_dis[i] + (*j).second) < smallest_leng){
			smallest_leng = min_dis[i] + (*j).second;  
			smallest_vtx = (*j).first;
	            }
	        }
		else continue;
	    }
	}
        X.push_back(smallest_vtx);
        min_dis[smallest_vtx] = smallest_leng;
        cout << "smallest_len " << smallest_leng << endl;
        count++;
    }
}

void Graph::print_ans(){
    std::cout << "1 = " << min_dis[0] << endl;
    std::cout << "80 = " << min_dis[79] << endl;
    std::cout << "7 = " << min_dis[6] << endl;
    std::cout << "37 = " << min_dis[36] << endl;
    std::cout << "59 = " << min_dis[58] << endl;
    std::cout << "82 = " << min_dis[81] << endl;
    std::cout << "99 = " << min_dis[98] << endl;
    std::cout << "115 = " << min_dis[114] << endl;
    std::cout << "133 = " << min_dis[132] << endl;
    std::cout << "165 = " << min_dis[164] << endl;
    std::cout << "188 = " << min_dis[187] << endl;
    std::cout << "197 = " << min_dis[196] << endl;
}

void Graph::print_test(){

    cout << "1 = " << min_dis[0] << endl;
    cout << "2 = " << min_dis[1] << endl;
    cout << "3 = " << min_dis[2] << endl;
    cout << "4 = " << min_dis[3] << endl;

}

int main(){
    //ifstream afile("testData.txt");
    ifstream afile("new_dijkstraData.txt");
    int v = 0;
    int w = 0;
    double length = 0;
    int nV = 200;
    //int nV = 4;
    Graph graph(nV);
    double templen = 0;
    while(afile >> v){
        afile >> w >> templen; 
        graph.addEdge(v-1, w-1, templen); 
	cout<<"happy "<< templen <<endl;
        //graph.addEdgeLength(v-1, w-1, length);
        //rev_graph.addEdge(w-1, v-1);
        //cout << w  << endl;
    }
   
    afile.close();

    graph.dijkstra_search();
    //graph.print_test();
    graph.print_ans();
    //rev_graph.DFS_loop();
    //rev_graph.print_ft();
    
    //vector<int> kFt = rev_graph.getFt();
    //Graph new_graph(nV);
    //ifstream aafile("test.txt"); 
    //ifstream aafile("SCC.txt"); 

    //cout << "second time" << endl;
    //while(aafile >> v){
    //    aafile >> w;
    //    new_graph.addEdge(kFt[v-1], kFt[w-1]); 
   // }
    //new_graph.DFS_loop();
    //new_graph.print_leader(); 
    //new_graph.print_scc10();
 
    return 0;
}
