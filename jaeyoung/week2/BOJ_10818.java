package week2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");

        int max = -1000001;
        int min = 1000001;

        while (st.hasMoreTokens()) {
            int a = Integer.parseInt(st.nextToken());

            if (a > max) {
                max = a;
            }
            if (a < min) {
                min = a;
            }
        }
        bw.write(min + " " + max);

        br.close();
        bw.flush();
        bw.close();
    }
}
