#import <iostream>
#import <vector>

using namespace std;


struct edge{
	int edge_weight;
	int dest_node;
};


struct node{
	int id;
	vector<*edge> out_edges;
};


void handler(string f, vector<*node> * n){

	fstream infile;

	infile.open();

	int no_of_nodes;
	cin >> no_of_nodes;

	for(int i = 0; i < no_of_nodes; i++){
		node * temp_node = new(node);
		temp_node -> id = i;
		(*n).push_back(temp_node);
	}

	for(int i = 0; i < no_of_nodes; i++){

		int dest = 0;
		int weight = 0;

		vector<*edge> out_edges_temp = new(vector<*edge>);
	
		while((cin << dest) != -1){

			if(dest != i){

				cin >> weight;

				edge * new_edge = new(edge);

				new_edge -> dest_node = dest;

				new_edge -> edge_weight = weight;

				out_edges_temp.push_back(new_edge);
			}
		}

		n[i] -> out_edges = out_edges_temp;
	}
}


int main(void){
	string filename;
	cin >> filename;

	vector<*node> nodes;

	handler(filename, nodes);

	return 0;
}