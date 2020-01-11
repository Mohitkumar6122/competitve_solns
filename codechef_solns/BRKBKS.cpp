#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define fr(i,x,y) for(int i=x;i<y;i++)

int main() {
    fastio;
    int t,s,w[3];
    cin>>t;
    while(t--)
    {
        int l=0,r=2;
        cin>>s;
        fr(i,0,3){cin>>w[i];}
        int hit=0;
        while(l<=r)
        {
            int t1=0,t2=0;
            int tl=l,tr=r;
            while(tl<=r && (t1+=w[tl])<=s){tl++;}
            while(tr>=l && (t2+=w[tr])<=s){tr--;}
            if(tl-l >=r-tr)
            {l=tl;}
            else
            {r=tr;}
            hit++;
        }
        cout<<hit<<endl;
    }
	return 0;
}
