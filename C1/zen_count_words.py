import operator
import collections
from pprint import pprint


zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# dict_count = dict()
# zen = zen.lower()
# for word in zen.split():
#     cleaned_word = word.strip('!./--')
#     if cleaned_word not in dict_count:
#         dict_count[cleaned_word] = 0
#     dict_count[cleaned_word] += 1

# zen_items = dict_count.items()
# sorted_zen_items = sorted(zen_items, key=operator.itemgetter(1), reverse=True)
# print(sorted_zen_items[:3:])

zen_key = []
for word in zen.split():
    cleaned_word = word.strip('!./--')
    zen_key.append(cleaned_word)

count_zen_words = collections.Counter(zen_key).most_common(3)
print(count_zen_words)


