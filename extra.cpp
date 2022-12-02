vs split_str(const string &s, char delim)
{
    vs ret;
    string cur;
    for (auto c : s)
    {
        if (c == delim)
        {
            ret.push_back(cur);
            cur = "";
        }
        else
        {
            cur += c;
        }
    }
    ret.push_back(cur);
    return ret;
}

vi split_nums(const string &s, char delim)
{
    vi ret;
    string cur;
    for (auto c : s)
    {
        if (c == delim && !cur.empty())
        {
            ret.push_back(stoi(cur));
            cur = "";
        }
        else
        {
            cur += c;
        }
    }
    ret.push_back(stoi(cur));
    return ret;
}
