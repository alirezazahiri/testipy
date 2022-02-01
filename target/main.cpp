#include <iostream>

using namespace std;

int main()
{

	int n, m;

	cin >> n >> m;

	int mat[n][m];

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> mat[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (i >= 1)
				mat[i][j] += mat[0][j];
			cout << mat[i][j];
			if (j == m - 1)
				cout << endl;
			else
				cout << " ";
		}
	}

	return 0;
}
