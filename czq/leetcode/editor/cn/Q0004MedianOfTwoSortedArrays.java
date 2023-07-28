  //给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
//
// 
//
// 示例 1： 
//
// 
//输入：nums1 = [1,3], nums2 = [2]
//输出：2.00000
//解释：合并数组 = [1,2,3] ，中位数 2
// 
//
// 示例 2： 
//
// 
//输入：nums1 = [1,2], nums2 = [3,4]
//输出：2.50000
//解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
// 
//
// 示例 3： 
//
// 
//输入：nums1 = [0,0], nums2 = [0,0]
//输出：0.00000
// 
//
// 示例 4： 
//
// 
//输入：nums1 = [], nums2 = [1]
//输出：1.00000
// 
//
// 示例 5： 
//
// 
//输入：nums1 = [2], nums2 = []
//输出：2.00000
// 
//
// 
//
// 提示： 
//
// 
// nums1.length == m 
// nums2.length == n 
// 0 <= m <= 1000 
// 0 <= n <= 1000 
// 1 <= m + n <= 2000 
// -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
// 
//
// 
//
// 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？ 
// Related Topics 数组 二分查找 分治 👍 4594 👎 0

  
  package czq.leetcode.editor.cn;
  public class Q0004MedianOfTwoSortedArrays{
      public static void main(String[] args) {
          Solution solution = new Q0004MedianOfTwoSortedArrays().new Solution();
          int[] a = {1, 2}, b = {3, 4};
          solution.findMedianSortedArrays(a, b);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int i = 0, j = 0, cnt = 0;
        int[] arr = new int[m+n];
        while (cnt < (m+n)) {
            if (i >= m) arr[cnt++] = nums2[j++];
            else if (j >= n) arr[cnt++] = nums1[i++];
            else if (nums1[i] < nums2[j]) arr[cnt++] = nums1[i++];
            else arr[cnt++] = nums2[j++];
        }
        int mid = (m+n)/2;//left
        return ((m+n)%2 != 0)? (double)arr[mid]: (arr[mid] + arr[mid+1])/2.0;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }
