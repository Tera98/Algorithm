import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for(int i = 0; i<t; i++){
            
            int n = sc.nextInt();
            int[] array = new int[n+1];
            
            for(int j = 0; j<n; j++){
                array[j] = sc.nextInt();
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
