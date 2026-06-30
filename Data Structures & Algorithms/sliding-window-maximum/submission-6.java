class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        if (n == 0 || k == 0) return new int[0];
        int res[]=new int [n-k+1];
        int count=0;
        PriorityQueue<Integer> pq=new PriorityQueue<>((a,b)->b-a);
        for(int i=0;i<k;i++){
            pq.offer(nums[i]);
        }
        res[count++]=pq.peek();
        for(int i=k;i<n;i++){
            pq.remove(nums[i-k]);
            pq.offer(nums[i]);
            res[count++]=pq.peek();
        }
        return res;
    }
}
