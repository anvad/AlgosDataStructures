#include <cstdio>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
#include <chrono>
#include <ctime>

using namespace std;

// Vertex of a splay tree
struct Vertex {
  char key;
  // size of all the keys in the subtree - remember to update
  // it after each operation that changes the tree.
  int size;
  Vertex* left;
  Vertex* right;
  Vertex* parent;

  Vertex(char key, int size, Vertex* left, Vertex* right, Vertex* parent) 
  : key(key), size(size), left(left), right(right), parent(parent) {}
};



void update(Vertex* v) {
  if (v == NULL) return;
  v->size = 1 + (v->left != NULL ? v->left->size : 0ll) + (v->right != NULL ? v->right->size : 0ll);
  if (v->left != NULL) {
    v->left->parent = v;
  }
  if (v->right != NULL) {
    v->right->parent = v;
  }
}

void small_rotation(Vertex* v) {
  Vertex* parent = v->parent;
  if (parent == NULL) {
    return;
  }
  Vertex* grandparent = v->parent->parent;
  Vertex* m = NULL;
  int vsize = v->size;
  int psize = parent->size;
  int msize = 0;
  if (parent->left == v) {
    m = v->right;
    v->right = parent;
    parent->left = m;
  } else {
    m = v->left;
    v->left = parent;
    parent->right = m;
  }
  //update(parent);
  if (m != NULL) {
	  m->parent = parent;
	  msize = m->size;
  }
  parent->size = psize - vsize + msize;
  //update(v);
  parent->parent = v;
  v->size = psize;
  
  v->parent = grandparent;
  if (grandparent != NULL) {
    if (grandparent->left == parent) {
      grandparent->left = v;
    } else {
      grandparent->right = v;
    }
  }
}

void big_rotation(Vertex* v) {
  if (v->parent->left == v && v->parent->parent->left == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } else if (v->parent->right == v && v->parent->parent->right == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } else {
    // Zig-zag
    small_rotation(v);
    small_rotation(v);
  }  
}

// Makes splay of the given vertex and makes
// it the new root.
void splay(Vertex*& root, Vertex* v) {
  if (v == NULL) return;
  while (v->parent != NULL) {
    if (v->parent->parent == NULL) {
      small_rotation(v);
      break;
    }
    big_rotation(v);
  }
  root = v;
}

// Searches for the given key in the tree with the given root
// and calls splay for the deepest visited node after that.
// If found, returns a pointer to the node with the given key.
// Otherwise, returns a pointer to the node with the smallest
// bigger key (next value in the order).
// If the key is bigger than all keys in the tree, 
// returns NULL.
Vertex* find_orig(Vertex*& root, int key) {
  Vertex* v = root;
  Vertex* last = root;
  Vertex* next = NULL;
  while (v != NULL) {
    if (v->key >= key && (next == NULL || v->key < next->key)) {
      next = v;
    }
    last = v;
    if (v->key == key) {
      break;      
    }
    if (v->key < key) {
      v = v->right;
    } else {
      v = v->left;
    }
  }
  splay(root, last);
  return next;
}

Vertex* findi(Vertex*& root, int index_to_find) {
	Vertex* v = root;
	Vertex* last = root;
	Vertex* next = NULL;
	int cur_index = 0;
	if (v->left != NULL) {
		cur_index = v->left->size;
	}
  	while (cur_index != index_to_find) {
		if (index_to_find < cur_index) {
			v = v->left;
		}
		else {
			v = v->right;
			index_to_find -= (++cur_index);
		}
		if (v == NULL) {
			break;
		}
		last = v;
		if (v->left != NULL) {
			cur_index = v->left->size;
		}
		else {
			cur_index = 0;
		}
	}
	next = v;
	splay(root, last);
	return next;
}

void split(Vertex* root, int key, Vertex*& left, Vertex*& right) {
  right = findi(root, key);
  //splay(root, right);
  if (right == NULL) {
    left = root;
    return;
  }
  left = right->left;
  right->left = NULL;
  if (left != NULL) {
    left->parent = NULL;
	right->size -= left->size;
  }
  //update(left);
  //update(right);
}

Vertex* merge_orig(Vertex* left, Vertex* right) {
  if (left == NULL) return right;
  if (right == NULL) return left;
  Vertex* min_right = right;
  while (min_right->left != NULL) {
    min_right = min_right->left;
  }
  splay(right, min_right);
  right->left = left;
  update(right);
  return right;
}

Vertex* merge(Vertex* left, Vertex* right) {
  if (left == NULL) return right;
  if (right == NULL) return left;
  Vertex* min_right = right;

  right->left = left;
  //update(right);
  left->parent = right;
  right->size += left->size;
  return right;
}

Vertex* insert_special(Vertex* root, char c, int i) {
	Vertex* v = new Vertex(c, i+1, root, NULL, NULL);
	root->parent = v;
	return v;
}

class Rope {
	std::string s;
	Vertex* root;
public:
	Rope(const std::string &s) : s(s) {
		root = new Vertex(s[0], 1, NULL, NULL, NULL);
		int slen = s.length();
		for (int i=1; i < slen; ++i) {
			root = insert_special(root, s[i], i);
		}
	}

	void process_naive( int i, int j, int k ) {
		// Replace this code with a faster implementation
		if (j >= s.length()) {
			j = s.length() - 1;
		}
		std::string t = s.substr(0, i) + s.substr(j + 1);
		s = t.substr(0, k) + s.substr(i, j - i + 1) + t.substr(k);
	}
	
	void process( int i, int j, int k ) {
		Vertex* left = NULL;
		Vertex* middle = NULL;
		Vertex* middle2 = NULL;
		Vertex* middle3 = NULL;
		Vertex* right = NULL;
		Vertex* new_left = NULL;
		Vertex* new_vertex = NULL;  
		split(root, j+1, middle, right);
		split(middle, i, left, middle);
		//new_left = merge(left, right);
		if (i > k) {
			split(left, k, left, middle2);
			root = merge(merge(merge(left, middle), middle2), right);
		}
		else {
			split(right, k - i, middle2, right);
			if (middle2 != NULL) {
				while (middle2->left != NULL) {
					middle2 = middle2->left;
				}
				splay(middle2, middle2);
			}
			root = merge(merge(merge(left, middle2), middle), right);
		}
		//split(new_left, k, left, right);
		//new_left = merge(left, middle);
		//root = merge(new_left, right);
	}
	
	void traverseTree(Vertex* root) {
		//string new_s = "";
		//std::stringstream ss;
		int i = 0;
		stack<Vertex*> st;
		Vertex* v = root;
		while (v != NULL) {
			st.push(v);
			v = v->left;
		}
		while (!st.empty()) {
			v = st.top();
			st.pop();
			//new_s += v->key;
			//ss << v->key;
			s[i++] = v->key;
			v = v->right;
			while (v != NULL) {
				st.push(v);
				v = v->left;
			}
		}
		//return new_s;
		//return ss.str();
	}

	std::string result() {
		traverseTree(root);
		//return traverseTree(root);
		return s;
	}
};

int main() {
	std::ios_base::sync_with_stdio(0);
	std::string s;
	std::cin >> s;
	std::chrono::time_point<std::chrono::system_clock> s0, start, end;
    start = std::chrono::system_clock::now();
	s0 = start;
	Rope rope(s);
	end = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = end-start;
	cout << "rope init took " << elapsed_seconds.count() << " seconds" << endl;
	//std::cout << "read rope!" << endl;
	//cout << "INT_MAX = " << INT_MAX << endl;
	int actions;
	std::cin >> actions;
	int i, j, k;
	start = std::chrono::system_clock::now();
    for (int action_index = 0; action_index < actions; ++action_index) {
		if ((action_index % 10000) == 0) {
			end = std::chrono::system_clock::now();
			elapsed_seconds = end-start;
			start = end;
			cout << "10K iterations took " << elapsed_seconds.count() << " seconds" << endl;
		}
		std::cin >> i >> j >> k;
		//cout << i << "," << j << ", " << k << endl;
		rope.process(i, j, k);
	}
	end = std::chrono::system_clock::now();
	elapsed_seconds = end-start;
	cout << "10K iterations took " << elapsed_seconds.count() << " seconds" << endl;
	std::cout << rope.result() << std::endl;
	end = std::chrono::system_clock::now();
	elapsed_seconds = end-start;
	cout << "final tree traversal took " << elapsed_seconds.count() << " seconds" << endl;
	elapsed_seconds = end-s0;
	cout << "total time taken " << elapsed_seconds.count() << " seconds" << endl;
}
