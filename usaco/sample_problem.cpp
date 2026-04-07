#include <iostream>
#include <tuple>

using namespace std;

int main() {
    tuple<int, int, int> t{3, 4, 5};
    cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
    return 0;
}
