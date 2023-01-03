import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String inNumber = br.readLine();
        
        StringTokenizer st = new StringTokenizer(inNumber);
        int[] array = new int[100000];
        
        for(int i = 0 ; i<n;i++){
            array[i] = Integer.parseInt(st.nextToken());
        }
        
        int q = Integer.parseInt(br.readLine());
        int A,B,count = 0;
        
        for(int j = 0; j<q ; j++){
            String inCount = br.readLine();
            StringTokenizer st1 = new StringTokenizer(inCount);
            A = Integer.parseInt(st1.nextToken());
            B = Integer.parseInt(st1.nextToken());
            
            for(int k=A;k<=B;k++){
                count += array[k-1];
            }
            System.out.println(count);
            count = 0;
        }
        bw.flush();
        bw.close(); 
    }
}
