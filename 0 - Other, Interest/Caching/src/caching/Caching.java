package caching;

import java.util.Arrays;

/* Author: Michael */

public class Caching {
	
	private static boolean __CACHING_ENABLED = true;
	//private static List<Integer> __CACHE = new ArrayList<Integer>();
	private static int[] __CACHE = new int[100];
	
	public static void main(String[] args) {		
		Arrays.fill(__CACHE, -1);

		System.out.println(fibonacci(25));
	}
	
	public static int fibonacci(int n) {
		int fib = 0;
		
		if (__CACHING_ENABLED) {
			if (__CACHE[n] != -1) {
				return __CACHE[n];
			}
		}
		
		if (n == 0) {
		} else if (n == 1) {
			fib = 1;
		} else {
			fib = fibonacci(n - 1) + fibonacci(n - 2);
		}	
		
		__CACHE[n] = fib;
		
		return fib;
	}

}
