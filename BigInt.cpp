#include <iostream>

using namespace std;

struct BigIntNode {

	short digit;
	BigIntNode *next;

	BigIntNode(short _digit, BigIntNode *_next = nullptr): digit(_digit), next(_next) {}

	~BigIntNode() {
		if(next)
			delete next;
	}

};

/* ------------------------------------------------------------------------------- */

struct BigInt {

	friend ostream& operator<<(ostream&, const BigInt&);

public:

	BigInt() {
		root = nullptr;
	}

	BigInt(const string &s) { /* s is supposed to contain chars from '0' to '9' only, a previous check is needed. */
		root = nullptr;
		for(char c : s)
			root = new BigIntNode(c - '0', root);
	}

	BigInt(const BigInt &bi) {
		root = nullptr;
		*this = bi;
	}

	BigInt& operator=(const BigInt &bi) {

		if(this->root)
			delete this->root;

		root = new BigIntNode(bi.root->digit);

		for(auto p = bi.root->next, t = root; p != nullptr; p = p->next, t = t->next)
			t->next = new BigIntNode(p->digit);

		return *this;

	}

	BigInt operator+(const BigInt &bi) const {

		BigIntNode *p = this->root;
		BigIntNode *t = bi.root;
		short tmpResult, carry = 0;
		BigInt result;
		BigIntNode *resultPtr = result.root = new BigIntNode('0'); // Temporary node

		while(p != nullptr and t != nullptr) {
			tmpResult = p->digit + t->digit + carry;
			carry = tmpResult / 10;
			tmpResult %= 10;
			resultPtr->next = new BigIntNode(tmpResult);
			resultPtr = resultPtr->next;
			p = p->next, t = t->next;
		}

		if(p != nullptr)
			while(p != nullptr) {
				tmpResult = p->digit + carry;
				carry = tmpResult / 10;
				tmpResult %= 10;
				resultPtr->next = new BigIntNode(tmpResult);
				resultPtr = resultPtr->next;
				p = p->next;
			}
		else
			while(t != nullptr) {
				tmpResult = t->digit + carry;
				carry = tmpResult / 10;
				tmpResult %= 10;
				resultPtr->next = new BigIntNode(tmpResult);
				resultPtr = resultPtr->next;
				t = t->next;
			}

		if(carry)
			resultPtr->next = new BigIntNode(carry);

		/* Deleting the temporary node */
		resultPtr = result.root;
		result.root = resultPtr->next;
		resultPtr->next = 0;
		delete resultPtr;

		return result;
	}

	BigInt operator-(const BigInt &bi) const; // To be done.
	BigInt operator*(const BigInt &bi) const; // To be done.
	BigInt operator/(const BigInt &bi) const; // To be done.
	BigInt operator%(const BigInt &bi) const; // To be done.
	BigInt& operator+=(const BigInt &bi); // To be done.
	BigInt& operator-=(const BigInt &bi); // To be done.
	BigInt& operator*=(const BigInt &bi); // To be done.
	BigInt& operator/=(const BigInt &bi); // To be done.
	BigInt& operator%=(const BigInt &bi); // To be done.
	// And so on...

private:

	BigIntNode *root;

	void recursive_print(const BigIntNode *node) const {

		if(node == nullptr)
			return;

		recursive_print(node->next);
		cout << node->digit;

	}

	void print() const {
		recursive_print(this->root);
	}
	
};

/* ------------------------------------------------------------------------------- */

ostream& operator<<(ostream &out, const BigInt &bi) {
	bi.print();
	return out;
}

/* ------------------------------------------------------------------------------- */

int main() {

	BigInt i1("999");
	BigInt i2("1");

	cout << "i1 = " << i1 << "\ni2 = " << i2 << endl;

	BigInt i3(i1 + i2);
	cout << "i3 = i1 + i2 = " << i3 << endl;

	BigInt i4;

	i4 = i3 + i1;

	cout << "i4 = i1 + i3 " << i4 << endl;
	cout << "i4 + i2 = " << i4 + i2 << endl;

	return 0;

}
