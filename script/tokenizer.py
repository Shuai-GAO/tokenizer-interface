import jieba


def clean_text(text):
    cleaned_text = text.strip(' ').rstrip('\n ').replace('\n', '')
    return cleaned_text


def tokenize_text(path_to_text, encoding='utf-8', cut_all=False, HMM=True):
    with open(path_to_text, 'r', encoding=encoding) as instream:
        list_lines = []
        dict_tokens = {}

        for line in instream:
            if line == '\n': continue
            list_tokens = []

            cleaned_text = clean_text(line)

            seg_list_hmmtrue = jieba.cut(cleaned_text, cut_all=cut_all, HMM=HMM)
            for token in seg_list_hmmtrue:
                list_tokens.append(token)
                dict_tokens[token] = dict_tokens.get(token, 0) + 1
            list_lines.append(list_tokens)
    return list_lines, dict_tokens