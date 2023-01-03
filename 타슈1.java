import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        
        for(int i = 0; i<t; i++){
            
            int n = sc.nextInt();
            int[] array = new int[n];
            
            for(int j =0; j<n; j++){
                array[j] = sc.nextInt();
            }
            int m = sc.nextInt();
            for(int j =0; j<m; j++){
                int u = sc.nextInt();
                int v = sc.nextInt();
                array[u-1]--;
                array[v-1]++;
            }
            for(int j =0; j<n; j++){
                System.out.print(array[j]+" ");
            }
            System.out.println();
        }
    }
}
