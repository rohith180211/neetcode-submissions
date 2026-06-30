class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> st=new Stack<>();
        int n=heights.length;
        int maxi=0;
        for(int i=0;i<n;i++){
            while(!st.isEmpty() && heights[st.peek()]>=heights[i]){
                int element=heights[st.peek()];
                st.pop();
                int nse=i;
                int pse=st.isEmpty() ?  -1 : st.peek();
                maxi=Math.max(maxi,element*(nse-pse-1));
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            int newE=st.pop();
            int nse=n;
            int pse=st.isEmpty() ?  -1 : st.peek();
            maxi=Math.max(maxi,heights[newE]*(nse-pse-1));
        }
        return maxi;
    }
}
