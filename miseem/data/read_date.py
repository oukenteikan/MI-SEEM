#! /usr/bin/python3

#txt1 = "/data/website/MI-SEEM/miseem/data/formality_annotation.txt"
txt2 = "/data/website/MI-SEEM/miseem/data/human_eval.txt"
#with open(txt1, 'r') as f:
#    l1 = f.readlines()
#print(len(l1))
with open(txt2, 'r') as f:
    l2 = f.readlines()
print(len(l2))
#lines = l1 + l2
lines = l2

results = ["Ties", "Wins", "Loses", "Tie", "Win", "Loss", "Lose"]
data = []
for i in range(0, len(lines), 4):
    question = lines[i].strip()
    answer1 = lines[i+1].strip()
    answer2 = lines[i+2].strip()
    end1 = max(answer1.rfind(' '), answer1.rfind('	'))
    end2 = max(answer2.rfind(' '), answer2.rfind('	'))
    result1 = answer1[end1+1:]
    result2 = answer2[end2+1:]
    if result1 not in results or result2 not in results:
        print(result1, result2)
    answer1 = answer1[:end1]
    answer2 = answer2[:end2]
    data.append({"Question":question, "Answer1":answer1, "Answer2":answer2, "Result1":result1, "Result2":result2})
for d in data:
    print("Question is {}".format(d['Question']))
    print("Answer1 is {}".format(d['Answer1']))
    print("Answer2 is {}".format(d['Answer2']))
    print("Result1 is {}".format(d['Result1']))
    print("Result2 is {}".format(d['Result2']))
