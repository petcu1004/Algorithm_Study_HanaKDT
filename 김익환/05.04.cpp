// 프로그래머스_Lv2_영어 끝말잇기

#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    
    char last_char;
    int count = 0;
    int flag=0;
    
    ++count;
    last_char = words[0][words[0].size()-1];
    
    for(int i=1; i<words.size(); i++) {
        
        ++count;
        
        if(words[i-1][words[i-1].size() -1] != words[i][0]) {
            flag = 1;
            break;
        }
        
        for (int j=0; j<i; j++) {
            if (words[j] == words[i]) {
                flag = 1;
                break;
            }
        }
        
        if (flag == 1) {
            break;
        }
        
        last_char = words[i][words[i].size()-1];
    }
    
    if (flag == 1) {
        int people_num;
        int try_num;
        
        if (count % n == 0) {
            people_num = n;
            try_num = count/n;
        }
        else {
            people_num = count % n;
            try_num = count/n+1;
        }
        answer.push_back(people_num);
        answer.push_back(try_num);
    }
    else {
        answer.push_back(0);
        answer.push_back(0);
    }


    return answer;
}
