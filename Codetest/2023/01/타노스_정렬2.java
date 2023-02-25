import java.io.BufferedReader;          // 시간 초과
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i<t; i++){

            int n = Integer.parseInt(br.readLine());

            String inNumber = br.readLine();
            StringTokenizer st = new StringTokenizer(inNumber);

            int[] array = new int[n+1];

            for(int j = 0; j<n; j++){
                array[j] = Integer.parseInt(st.nextToken());
            }

            int j = 0, count = 0;

            while(j<n-1){
                if(array[j] > array[j+1]){
                    array[j] = array[j] / 2;
                    count += 1;
                }
                j++;
                if(count != 0 && j == n-1){
                    j = 0;
                    count = 0;
                }
            }

            for(int k = 0; k<n; k++){
                bw.write(array[k]+" ");
                bw.flush();
            }
            bw.write("\n");
            bw.flush();

        }
        br.close();
        bw.close();
    }
}
