def reverse_string(text):
    st = []
    for ch in text:
        st.append(ch)

    reversed_text_char = []

    while st:
        ch = st.pop()
        reversed_text_char.append(ch)
    return ''.join(reversed_text_char)


input_text = input()
print(reverse_string(input_text))
