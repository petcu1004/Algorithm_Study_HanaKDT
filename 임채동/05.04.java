import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        Set<String> set = new HashSet<>();
        for (int i = 1; i < words.length; i++) {
            String prevWord = words[i - 1];
            String curWord = words[i];
            
            // 이전 단어를 나왔던 단어셋에 넣어준다.
            set.add(prevWord);
            
            // 검사
            if (prevWord.charAt(prevWord.length() - 1) != curWord.charAt(0)
                || set.contains(curWord)) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                return answer;
            }
        }
        
        return answer;
    }
}