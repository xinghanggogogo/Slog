//动态规划, 求从顶部到底部最大
//http://blog.csdn.net/baidu_28312631/article/details/47418773
7
3   8
8   1   0
2   7   4   4
4   5   2   6   5
//way1, 递归解法:
// if (r == N)
// MaxSum(r, j) = D(r, j)
// else
// MaxSum(r, j) = Max{MaxSum(r＋1, j), MaxSum(r+1, j+1)} + D(r, j)
#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;

int D[MAX][MAX];
int n;
int MaxSum(int i, int j){
	if(i == n)
		return D[i][j];
	int x = MaxSum(i+1, j);
	int y = MaxSum(i+1, j+1);
	return max(x, y)+D[i][j];
}
int main(){
	int i, j;
	cin >> n;
	for(i=1; i<=n; i++)
		for(j=1; j<=i; j++)
			cin >> D[i][j];
	cout << MaxSum(1, 1) << endl;
}
//way2, 动态规划解法:
#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;
int D[MAX][MAX];
int maxSum[MAX][MAX];
int n;
int main(){
	int i, j;
	cin >> n;
	for(i=1; i<=n; i++)
		for(j=1; j<=i; j++)
			cin >> D[i][j];
	for(int i = 1;i <= n; ++ i)
		maxSum[n][i] = D[n][i];
	for(int i = n-1; i>= 1; --i)
		for(int j = 1; j <= i; ++j)
			maxSum[i][j] = max(maxSum[i+1][j], maxSum[i+1][j+1]) + D[i][j];
	cout << maxSum[1][1] << endl;
}
