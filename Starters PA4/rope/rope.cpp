#include <cstdio>
#include <string>
#include <iostream>
#include <stack>

using namespace std;

// Vertex of a splay tree
struct Vertex {
  int key;
  // size of all the keys in the subtree - remember to update
  // it after each operation that changes the tree.
  long long size;
  Vertex* left;
  Vertex* right;
  Vertex* parent;

  Vertex(char key, long long size, Vertex* left, Vertex* right, Vertex* parent) 
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
  if (parent->left == v) {
    Vertex* m = v->right;
    v->right = parent;
    parent->left = m;
  } else {
    Vertex* m = v->left;
    v->left = parent;
    parent->right = m;
  }
  update(parent);
  update(v);
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
	long long cur_index = 0;
	if (v->left != NULL) {
		cur_index = v->left->size;
	}
  	while (cur_index != index_to_find) {
		last = v;
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
  splay(root, right);
  if (right == NULL) {
    left = root;
    return;
  }
  left = right->left;
  right->left = NULL;
  if (left != NULL) {
    left->parent = NULL;
  }
  update(left);
  update(right);
}

Vertex* merge(Vertex* left, Vertex* right) {
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
		for (int i=1; i < s.length(); ++i) {
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
		Vertex* right = NULL;
		Vertex* new_left = NULL;
		Vertex* new_vertex = NULL;  
		split(root, j+1, middle, right);
		split(middle, i, left, middle2);
		new_left = merge(left, right);
		split(new_left, k, left, right);
		new_left = merge(left, middle2);
		root = merge(new_left, right);
	}
	
	std::string traverseTree(Vertex* root) {
		string new_s = "";
		stack<Vertex*> st;
		Vertex* v = root;
		while (v != NULL) {
			st.push(v);
			v = v->left;
		}
		while (!st.empty()) {
			v = st.top();
			st.pop();
			new_s += v->key;
			v = v->right;
			while (v != NULL) {
				st.push(v);
				v = v->left;
			}
		}
		return new_s;
	}

	std::string result() {
		return traverseTree(root);
	}
};

int main() {
	std::ios_base::sync_with_stdio(0);
	std::string s;
	std::cin >> s;
	Rope rope(s);
	//std::cout << "read rope!" << endl;
	//cout << "INT_MAX = " << INT_MAX << endl;
	int actions;
	std::cin >> actions;
	int i, j, k;
    for (int action_index = 0; action_index < actions; ++action_index) {
		std::cin >> i >> j >> k;
		//cout << i << "," << j << ", " << k << endl;
		rope.process(i, j, k);
	}
	std::cout << rope.result() << std::endl;
}
