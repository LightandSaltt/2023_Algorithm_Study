package week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1924 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] month = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] days = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int m = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int sum = 0;
        for (int i = 1; i < m; i++) {
            sum += month[i];
        }
        sum += d;
        System.out.println(days[sum % 7]);
    }
}
