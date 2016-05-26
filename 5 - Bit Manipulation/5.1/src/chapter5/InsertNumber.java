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
		int N = 0b100_0000_1111; // 1024
		int i = 2;
		int j = 6;
		
		printBinary(insertBinary(M, N, i, j));
	}

	// There's probably a way to make a mask and do this more efficiently all in one go, but this will do for now
	private static int insertBinary(int M, int N, int i, int j) {
		// Sanity checks
		if (i < 1) {
			System.out.println("Invalid input! i cannot be less than 1");
			return -1;
		} else if (j > numBits(N)) {
			System.out.println("Invalid input! j cannot be larger than the length of N in binary (" + numBits(N) + ")");
			return -1;
		} else if (((j - i) + 1) != numBits(M)) {
			System.out.println("Invalid input! i - j must equal the length of M in binary (" + numBits(M) + ")");
			return -1;
		}
		
		int y = numBits(M) - 1;
		
		// Replace bits i through j
		for (int x = j; x >= 0; x--) {
			N = copyBit(N, x, getBit(M, y));
			y -= 1;
		}
		
		return N;
	}
	
	private static int getBit(int num, int i) {
		// Makes a mask of pattern 1[i 0s]
		int mask = (1 << i);
		
		// The 0s will always return false when ANDed, so only the bit at position i will be checked
		boolean isSet = ((num & mask) != 0);
		
		// Convert back to an integer (1 = true, 0 = false)
		return isSet ? 1 : 0;
	}
	
	// I'm allowing i > number of bits in num - just extends the length of the number
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
	
	private static int copyBit(int num, int i, int bit) {	
		return (bit == 1) ? setBit(num, i) : clearBit(num, i);
	}
	
	private static void printBinary(int num) {
		System.out.println(Integer.toBinaryString(num));
	}
	
	private static int numBits(int num) {
		return (int) (Math.floor(Math.log(num) / Math.log(2)) + 1);
	}
}
