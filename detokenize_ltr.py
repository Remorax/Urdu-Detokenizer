import sys

# Urdu detokenizer
input_corpus = sys.argv[1]
output_corpus = sys.argv[2]

corpus = open(input_corpus).read().split("\n")

corpus_filt = []
for line_orig in corpus:
    if line_orig.strip() and is_nonlatin_script(line_orig):
        
        line = str(line_orig)
        
        # Handle quotes
        line = line.replace(" ’", "’")
        line = line.replace("‘ ", "’")

        line = line.replace(" ”", "”")
        line = line.replace("“ ", "“")

        line = line.replace(" '", "'")
        line = line.replace("' ", "'")

        line = line.replace(" ❞", "❞")
        line = line.replace("❝ ", "❝")

        # Handle brackets
        line = line.replace(" )", ")")
        line = line.replace("( ", "(")

        line = line.replace(" ]", "]")
        line = line.replace("[ ", "[")

        line = line.replace(" >", ">")
        line = line.replace("< ", "<")

        # Handle EOL characters and delimiters
        line = line.replace(" ۔", "۔")
        line = line.replace(" ؟", "؟")
        line = line.replace(" ?", "?")
        line = line.replace(" !", "!")
        line = line.replace(" ،", "،")
        line = line.replace(" ;", ";")
        line = line.replace(" ™", "™")
        line = line.replace(" :", ":")
        line = line.replace(" -", "-")
        line = line.replace(" %", "%")

        # Remove empty quotes
        line = line.replace("\"", "")

        # Handle prefix symbols
        line = line.replace("∑ ", "∑")
        line = line.replace("$ ", "$")
        line = line.replace("€ ", "€")
        line = line.replace("£ ", "£")
        line = line.replace("± ", "±")
        line = line.replace("@ ", "@")
        line = line.replace("# ", "#")
    
        # Handle backslashes
        line = line.replace("/ ", "/")
        line = line.replace(" /", "/")

        # Remove special characters
        line = line.replace("\u06dd", "")
        line = line.replace("\xad", "")
        line = line.replace("\u0600", "")
        line = line.replace("\u0603", "")
        line = line.replace("\uffe7", "")
        line = line.replace("\ufdfe", "")
        line = line.replace("\u200e", "")

        corpus_filt.append(line)
        
corpus_filt = list(set(corpus_filt))

open(output_corpus,"w+").write("\n".join(corpus_filt))
