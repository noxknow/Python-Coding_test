import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String args[]) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.valueOf(br.readLine());
		int k = Integer.valueOf(br.readLine());
		
		/*List<Integer> sensors = new ArrayList<Integer>();
		List<Integer> distances = new ArrayList<Integer>();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			int num = Integer.valueOf(st.nextToken());
			sensors.add(num);
		}
		
		Collections.sort(sensors);
		
		for(int i = 0; i < n - 1; i++) {
			int distance = sensors.get(i + 1) - sensors.get(i);
			distances.add(distance);
		}
		Collections.sort(distances);
		
		int len = distances.size();	// n - 1개
		int sum = 0;
		for(int i = 0; i < len - (k - 1); i++) {
			sum += distances.get(i);
		}*/
		
		int[] sensors = new int[n];
		int[] distances = new int[n - 1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			int num = Integer.valueOf(st.nextToken());
			sensors[i] = num;
		}
        
		Arrays.sort(sensors);
	
		for(int i = 0; i < n - 1; i++) {
			int distance = sensors[i + 1] - sensors[i];
			distances[i] = distance;
		}
		Arrays.sort(distances);
		
		int sum = 0;
		for(int i = 0; i < n - k; i++) {
			sum += distances[i];
		}
				
		System.out.println(sum);
	}
}
