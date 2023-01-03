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
        
        int t = Integer.parseInt(br.readLine());
        
        for(int i = 0; i<t; i++){
            
            int n = Integer.parseInt(br.readLine());
            
            String inNumber = br.readLine();
            StringTokenizer st = new StringTokenizer(inNumber);
            
            int[] array = new int[n+1];
            
            for(int j = 0; j<n; j++){
                array[j] = Integer.parseInt(st.nextToken());
            }
            
            int max = array[0];
            
            for(int j = 0; j<n; j++){
                if(max > array[j+1]){
                    array[j+1] = 0;
                } else{
                    max = array[j+1];
                }
            }
            for(int j = 0; j<n; j++){
                System.out.print(array[j] == 0 ? "" : array[j] + " ");
            }
            System.out.println();
        }
    }
}
