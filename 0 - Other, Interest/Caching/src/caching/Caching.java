package caching;

import java.util.Arrays;

/* Author: Michael */

public class Caching {
	
	private static boolean __CACHING_ENABLED = true;
	private static int[] __CACHE = new int[100];
	private static int __NUM = 40;
	
	public static void main(String[] args) {
		__CACHING_ENABLED = true;
		Arrays.fill(__CACHE, -1);
		runAndTime();
		
		Arrays.fill(__CACHE, -1);
		__CACHING_ENABLED = false;
		runAndTime();
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

	public static void runAndTime() {	
		long startTime, endTime;
		
		startTime = System.nanoTime();
		System.out.println(fibonacci(__NUM));
		endTime = System.nanoTime();
		
		System.out.println("Took " + (endTime - startTime) / 1000000 + "ms with caching " + (__CACHING_ENABLED ? "enabled." : "disabled."));
	}
}
