// 프로그래머스_Lv2_최댓값과 최솟값

// sstream을 사용해 공백을 기준으로 숫자를 추출해 풀이했다.

#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    
    stringstream num(s);
    string tmp;
    int min, max;
    int min_flag =0;
    int max_flag =0;
    
    while(num >> tmp) {
        if (min_flag !=0) {
            if (stoi(tmp) < min) {
                min = stoi(tmp);
            }
        }
        else {
            min = stoi(tmp);
            min_flag = 1;
        }
        
        if (max_flag!=0) {
            if (stoi(tmp) > max) {
                max = stoi(tmp);
            }
        }
        else {
            max = stoi(tmp);
            max_flag = 1;
        }
    }
    
    answer = to_string(min) + " " + to_string(max);
    
    return answer;
}
