class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            if ch==')':
                if len(st)==0:return False
                top=st.pop()
                if top!='(' :return False
            if ch=='}':
                if len(st)==0:return False
                top=st.pop()
                if top!='{' :return False
            if ch==']':
                if len(st)==0:return False
                top=st.pop()
                if top!='[' :return False
        if len(st)==0:return True
        return False
