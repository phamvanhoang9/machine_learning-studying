#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        vector<string> line;
        int width = 0;

        for (const string& w : words) {
            if (width + line.size() + w.length() > maxWidth) {
                for (int i = 0; i < maxWidth - width; ++i) {
                    line[i % (line.size() - 1 == 0 ? 1 : line.size() - 1)] += ' ';
                }
                res.push_back(join(line, ""));
                line.clear();
                width = 0;
            }
            line.push_back(w);
            width += w.length();
        }
        res.push_back(leftJustify(line, maxWidth));
        return res;
    }

private:
    string join(const vector<string>& line, const string& delim) {
        ostringstream os; // this allows us to construct a string by inserting various elements into the stream
        // size_t is an unsigned integral type, commonly used for array indexing and loop counting
        for (size_t i = 0; i < line.size(); ++i) {
            if (i != 0) os << delim;
            os << line[i];
        }
        return os.str(); // converts the contents of the output string stream into a single 
    }

    string leftJustify(const vector<string>& line, int maxWidth) {
        ostringstream os;
        for (size_t i = 0; i < line.size(); ++i) {
            if (i != 0) os << ' ';
            os << line[i];
        }
        string result = os.str();
        result.append(maxWidth - result.length(), ' ');
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> words = {"This", "is", "an", "example", "of", "text", "justification."};
    int maxWidth = 16;
    vector<string> justifiedText = solution.fullJustify(words, maxWidth);

    for (const string& line : justifiedText) {
        cout << "'" << line << "'" << endl;
    }

    return 0;
}