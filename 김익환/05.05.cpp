//백준_실버4_map_인사성 밝은 곰곰이

#include<iostream>
#include<string>
#include<map>

using namespace std;


int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	int count = 0;
	map<string, bool> m;

	cin >> N;

	for (int i = 0; i < N; i++) {
		string str;

		cin >> str;

		if (str == "ENTER") {
			m.clear();
			continue;
		}

		if (m.find(str) == m.end()) {
			m.insert({ str,1 });
			count++;
		}

	}

	cout << count;

	return 0;
}
