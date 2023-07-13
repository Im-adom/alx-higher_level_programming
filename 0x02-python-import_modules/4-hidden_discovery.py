#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for a_name in names:
        if a_name[:2] != "__":
            print(a_name)
