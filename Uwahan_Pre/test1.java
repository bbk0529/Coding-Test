package uwahan;

public class test1 {
	public static void main(String[] args) {
		String bNum=Integer.toBinaryString(15);
		System.out.println(bNum);
		int idx=0;
		int max=0;
		idx = bNum.indexOf('1');
		int old_idx=0;
		while(idx!=-1) {
			old_idx = idx; 
			idx = bNum.indexOf('1',idx+1);
			System.out.println(idx);
			if (max<(idx-old_idx-1)) { 
				max = idx-old_idx-1;
			}
		}
		System.out.println(max); 
	}
}
