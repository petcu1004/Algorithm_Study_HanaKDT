import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        String[] strs = new String[n];

        int m = 0;
        while (n-- > 0) {
            strs[m++] = br.readLine();
        }

        System.out.println(solution(strs));

        br.close();
    }

    private static Map<String, Boolean> map;

    static int solution(String[] strs) {
        // ENTER가 나오는지 체크,
        // ENTER가 나오면 map초기화,
        // 아이디가 map에 없으면 count++
        // 아이디가 map에 있으면 continue;
        int count = 0;
        for (int i = 0; i < strs.length; i++) {
            String id = strs[i];
            if (strs[i].equals("ENTER")) {
                map = new HashMap();
                continue;
            }

            if (map.getOrDefault(id, true)) {
                count++;
            }
            map.put(id, false);
        }

        return count;
    }
}

