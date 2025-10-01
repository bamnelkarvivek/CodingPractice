def reverse(s):
    """ Reverse a string using recursion """
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

if __name__ == "__main__":
    print(reverse("hello"))  # output: "olleh"