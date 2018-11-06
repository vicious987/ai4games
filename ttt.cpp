#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


//TODO CONSTS LIKE MIN, BOARD STATUSES ( ADD DRAW AND ONGOING), PLAYER TOGLE?, CLASS METHODS?
// CHOSING CHILDREN BY UTC, CODINGAME INPUT INTERACTION
// ???
struct Tboard {
	int board [3][3] = {0};
	bool finished = false;
	int winner = 0;

	int check_win_row(int row){
		return board[row][0] + board[row][1] + board[row][2];
	}

	int check_win_col(int col){
		return board[0][col] + board[1][col] + board[2][col];
	}
	int check_win_diag(int diag){
		if (diag % 2 == 0)
			return board[2][0] + board[1][1] + board[0][2];
		else
			return board[0][0] + board[1][1] + board[2][0];
	}

	int check_win_cond(){
		for (int i = 0; i < 3; i++){
			switch(check_win_row(i)){
				case 3: 	return 1;
				case -3: 	return -1;
			}
			switch(check_win_col(i)){
				case 3: 	return 1;
				case -3:  	return -1;
					 
			}
			switch(check_win_row(i)){
				case 3: 	return 1;
				case -3:	return -1;
			}
		}
		return 0;
	}

	public:
	//int[3][3] get_board(){
	//	return board;
	//}

	int check_winner(){
		winner = check_win_cond();
		finished = true;
		return winner;
	}

	void make_move(int row, int col, int player_id){
		board[row][col] = player_id;
	}
	
	bool check_status(){
		return winner;
	}
};

			//return Collections.max(
			//		node.getChildArray(),
			//		Comparator.comparing(c -> uct_value(parentVisit, c.get_state().get_score(), c.get_state().get_visit_count())));



class State {
	Tboard board;
	int player_id;
	int visit_count = 0;
	double score = 0;
	
	State(Tboard b, int pid){
		board = b;
		player_id = pid;
	}
	public:

	int get_player_id(){
		return player_id;
	}
	int get_visit_count(){
		return visit_count;
	}
	double get_score(){
		return score;
	}

	Tboard get_board(){
		return board;
	}

	void set_player_id(int pid){
		player_id = pid;
	}
	void inc_visit_count(){
		visit_count += 1;
	}
	void set_score(double sc){
		score = sc;
	}
	void set_board(Tboard b){
		board = b;
	}

	void make_move(int row, int col, int player_id){
		board.make_move(row, col, player_id);
	}
	void add_score(double sc){
		score += sc;
	}
};

struct None;

struct Node{
	State state;
	Node & parent;
	vector<Node> children;
	
	Node(State st, Node pr){
		state = st;
		parent = pr;
	}

	public:
	
	State get_state(){
		return state;
	}
	Node get_parent(){
		return parent;
	}
	vector<Node> get_children(){
		return children;
	}
	void set_state(State st){
		state =st;
	}
	void set_parent(Node pr) {
		parent = pr;
	}
	void add_child(Node child){
		children.push(child);
	}
};

class Tree{
	Node root;
	
	Node(Node r){
		root = r;
	}
	public:
	Node get_root(){
		return root;
	}
	void set_root(Node r){
		root = r;
	}

}

double uct_value(int total_visit, double node_score, int node_visit) {
	if (node_visit == 0) 
		return MAX_VALUE;
	return ((double) node_score/ (double) node_visit) + 1.41 * math.sqrt(math.log(total_visit) / (double) node_visit);

}
class UCT {
	public:


		bool utc_comp(const Node& a, const Node& b, int parent_visit){
			return (	utc_value(parent_visit, a.get_state().get_score(), a.get_state().get_visit_count()) <
					utc_value(parent_visit, b.get_state().get_score(), b.get_state().get_visit_count()))	
		}

		// java -> cpp
		Node find_best(Node node) {
			const int parent_visit = node.get_state().get_visit_count();
			auto x = max_element(children_list.begin(), children_list.end(), [parent_visit](const auto & child1, const auto & child2) {
				return uct_value(parent_visit, child2.e1, child1.e2) < uct_value(parent_visit, child2.e1, child2.e2);
			});
			
		}

}

//TODO MIN
class MCTS {
	int WIN_SCORE = 10;
	int level;
	int enemy;
	int MIN;
 
	Node select_promising_node(Node root_node) {
	    Node node = root_node;
	    while (node.get_children().size() != 0) {
		node = UCT.find_best(node);
	    }
	    return node;
	}

	//TODO finish this 
	void expand_node(Node node) {
	    List<State> possible_states = node.get_state().get_all_possible_states();
	    for each possible state:
	    {
		Node new_node = new Node(state);
		new_node.set_parent(node);
		new_node.get_state().set_player_id(node.get_state().get_enemy());
		node.get_children().push(new_node);
	    };
	}
	void back_propogation(node node_to_explore, int player_id) {
		node temp_node = node_to_explore;
		while (temp_node != null) {
			temp_node.get_state().inc_visit();
			if (temp_node.get_state().get_player_id() == player_id)
				temp_node.get_state().add_score(win_score);
			temp_node = temp_node.get_parent();
		}
	}

	int simulate_random_playout(node node) {
		node temp_node = new node(node);
		state temp_state = tem_pnode.get_state();
		int board_status = temp_state.get_board().get_status();
		if (board_status == enemy) {
			temp_node.get_parent().get_state().set_winscore(MIN);
			return board_status;
		}
		while (board_status == IN_PROGRESS) {
			temp_state.toggle_player();
			temp_state.random_play();
			board_status = temp_state.get_board().check_status();
		}
		return board_status;
	}



	public:
	Board find_next_move(Tboard board, int player_id) {

        // define an end time which will act as a terminating condition
	
		enemy = player_id * (-1);
		Tree tree = new Tree();
		Node root_node = tree.get_root();
		root_node.get_state().set_roard(board);
		root_node.get_state().set_player_id(enemy);

		while (System.currentTimeMillis() < end) {
			Node promising_node = select_promising_node(root_node);
		    	if (promising_node.get_state().get_board().check_status() == IN_PROGRESS)
				expand_node(promising_node);
			Node node_to_explore = promising_node;
			if (promising_node.get_children().size() > 0) 
				node_to_explore = promising_node.get_random_child();
			int playout_result = simulate_random_playout(node_to_explore);
			back_propogation(node_to_explore, playout_result);
		}
 
		Node winner_node = root_node.get_Child_With_Max_Score();
		Node winner_node = root_node.get_bestchild();
		tree.set_root(winner_node);
		return winner_node.get_state().get_board();
	}


}

	

int main()
{
    while (1) {
        int enemy_row, enemy_col;
        cin >> enemy_row >> enemy_col; cin.ignore();
        int action_count;
        cin >> action_count; cin.ignore();
        for (int i = 0; i < action_count; i++) {
            int row, col;
            cin >> row >> col; cin.ignore();
        }

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        cout << "0 0" << endl;
    }
}
