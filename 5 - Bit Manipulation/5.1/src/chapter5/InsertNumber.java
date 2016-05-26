package chapter5;

public class InsertNumber {
/*	You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
 *  Write a method to insert M into N such that M starts at bit j and ends at bit i. 
 *  You can assume that the bits j through i have enough space to fit all of M. 
 *  That is, if M = 10011, you can assume that there are at least 5 bits between j and i. 
 *  You would not, for example, have j = 3 and i = 2, because M could not fully fit	between bit 3 and bit 2.
 *  
 *  EXAMPLE
 *  Input: N = 10000000000, M = 10011, i = 2, j = 6
 *  Output: N = 10001001100 */

	public static void main(String[] args) {
		int M = 0b1_0011; // 19
		int N = 0b100_0000_0000; // 1024
		int i = 2;
		int j = 6;
		
		insertBinary(M, N, i, j);
		System.out.println(getBit(N, i));
		printBinary(setBit(N, i));
		printBinary(clearBit(N, i));
	}

	private static int insertBinary(int M, int N, int i, int j) {
		System.out.println("About to insert " + M + " into " + N + " at bits " + i + " through " + j);
		
		// TODO: Shift bits N[i+] left by numBits(M)
		// TODO: Set bits j through i to the bits of M
		for (int x = j; x > 0; x--) {
			if (x >= i) {
				//copy bit from M
			} else {
				//copy bit from N
			}
		}
		return 0;
	}
	
	private static int getBit(int num, int i) {
		// Makes a mask of pattern 1[i 0s]
		int mask = (1 << i);
		
		// The 0s will always return false when ANDed, so only the bit at position i will be checked
		boolean isSet = ((num & mask) != 0);
		
		// Convert back to an integer (1 = true, 0 = false)
		return isSet ? 1 : 0;
	}
	
	private static int setBit(int num, int i) {
		// Makes a mask of pattern 1[i 0s]
		int mask = (1 << i);
		
		// The 0s do nothing when ORed, so only the single bit at position i will change
		int result = num | mask;
		
		return result;
	}
	
	private static int clearBit(int num, int i) {
		// Makes a mask of pattern 0[i 1s]
		int mask = ~(1 << i);
		
		// The 1s do nothing when ANDed, so only the single bit at position i will change
		int result = num & mask;
		
		return result;
	}
	
	private static void printBinary(int num) {
		System.out.println(Integer.toBinaryString(num));
	}
}
