package chapter7;

import  java.lang.Math;

/*
 * Write methods to implement the multiply, subtract, and divide operations for integers. 
 * Use only the add operator.
 * 
 * Note: I didn't bother, but there should be additional checks for valid input (not dividing by a larger number, 0, etc)
 */
public class MathematicalOperators {

	public static void main(String[] args) {		
		int a = 6;
		int b = 4;
		int c = 12;
		int d = 2;
		int e = 5;
		int f = 2;
		int g = 40;
		int h = 4;

		System.out.println("Addition:");
		System.out.println(a + " + " + b + " = " + add(a, b));
		System.out.println(-a + " + " + b + " = " + add(-a, b));
		System.out.println(-a + " + " + -b + " = " + add(-a, -b));
		System.out.println(a + " + " + -b + " = " + add(a, -b));

		System.out.println("\nSubtraction:");
		System.out.println(c + " - " + d + " = " + subtract(c, d));
		System.out.println(-c + " - " + d + " = " + subtract(-c, d));
		System.out.println(-c + " - " + -d + " = " + subtract(-c, -d));
		System.out.println(c + " - " + -d + " = " + subtract(c, -d));

		System.out.println("\nMultiplication:");
		System.out.println(e + " x " + f + " = " + multiply(e, f));
		System.out.println(-e + " x " + f + " = " + multiply(-e, f));
		System.out.println(-e + " x " + -f + " = " + multiply(-e, -f));
		System.out.println(e + " x " + -f + " = " + multiply(e, -f));

		System.out.println("\nDivision:");
		System.out.println(g + " / " + h + " = " + divide(g, h));
		System.out.println(-g + " / " + h + " = " + divide(-g, h));
		System.out.println(-g + " / " + -h + " = " + divide(-g, -h));
		System.out.println(g + " / " + -h + " = " + divide(g, -h));
	}
	
	// Add a and b
	private static int add (int a, int b) {
		return a + b;
	}
	
	// Subtract b from a
	// Note that this does not support an input where a is negative
	// Where this function is used in the multiply() and divide() functions, it has been commented out
	//     and replaced with a negation.
	private static int subtract (int a, int b) {
		int difference = 0;
		
		// Get count of digits in a
		int digits = Integer.toString(a).length();

		// Get the difference between b and the next power of 10 greater than a
		while (b < (Math.pow(10, digits))) {
			b++;
			difference++;
		}

		// Add that difference to a
		a += difference;
		
		// Discard first digit from a to get the final result (by converting to string, taking the substring, and converting back)
		return Integer.parseInt(Integer.toString(a).substring(1));
		
		// For example, 12 - 2 becomes 12 + 98 = [1]10
	}
	
	// Multiply a and b
	private static int multiply (int a, int b) {
		int total = 0;
		boolean negA = false;
		
		if (a < 0) {
			negA = true;
//			a = subtract(0, a);
			a = -a;
		}
		
		for (int i = 0; i < a; i++) {
			total += b;
		}
		
		if (negA) {
//			total = subtract(0, total);
			total = -total;
		}
		
		return total;
	}
	
	// Divide a by b
	//TODO: Add support for negatives
	private static int divide (int a, int b) {		
		int count = 0;
		int divisor = b;
		
		if (a > 0) {
			if (b > 0) {
				while (b <= a) {
					count += 1;
					b += divisor;
				}
			} else {
//				b = subtract(b, count);
				b = -b;
				divisor = b;
				
				while (b <= a) {
					count += 1;
					b += divisor;
				}
				
//				count = subtract(0, count);
				count = -count;
			}
		} else {
			if (b > 0) {
//				a = subtract(a, count);
				a = -a;
				
				while (b <= a) {
					count += 1;
					b += divisor;
				}
				
//				count = subtract(0, count);
				count = -count;
			} else {
//				a = subtract(a, count);
				a = -a;
//				b = subtract(b, count);
				b = -b;
				divisor = b;
				
				while (b <= a) {
					count += 1;
					b += divisor;
				}
			}
		}
		
		return count;
	}

}
