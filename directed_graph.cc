#import <iostream>
#import <vector>
#include <fstream>

using namespace std;


struct edge{
	int edge_weight;
	int dest_node;
};


struct node{
	int id;
	vector<edge*> out_edges;
};


void handler(string f, vector<node*> &n){

	ifstream infile;

	infile.open(f);

	int no_of_nodes;
	infile >> no_of_nodes;

	for(int i = 0; i < no_of_nodes; i++){
		node * temp_node = new(node);
		temp_node -> id = i;
		n.push_back(temp_node);
	}

	for(int i = 0; i < no_of_nodes; i++){

		int dest = 0;
		int weight = 0;

		vector<edge*> out_edges_temp;
	
		while(infile >> dest){
			if(dest == -1){
				break;
			}
			else if(dest != i){

				infile >> weight;

				edge * new_edge = new(edge);

				new_edge -> dest_node = dest;

				new_edge -> edge_weight = weight;

				out_edges_temp.push_back(new_edge);
			}
		}

		n[i] -> out_edges = out_edges_temp;
	}

	infile.close();
}


int main(void){
	string filename;
	cin >> filename;

	vector<node*> nodes;

	handler(filename, nodes);

	for(int i = 0; i < nodes.size(); i++){
		cout << nodes[i] -> id << endl;
	}

	return 0;
}